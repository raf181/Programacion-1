#!/usr/bin/env python3
"""
System Log Archiver and Manager
--------------------------------

This script automates the management and archiving of system logs on a Debian-based system.
It provides the following functionalities:

1. Daily, Weekly, and Monthly Archiving:
   - Create a daily archive of system logs (from LOG_DIR), excluding archive directories.
   - On Sundays, combine the daily archives into a weekly archive and delete the daily files.
   - On the last day of the month, combine the weekly archives into a monthly archive and delete the weekly files.
   - Archives are created using LZMA/LZMA2 compression (tar.xz).

2. Hashing and Data Integrity:
   - Compute a SHA‑256 hash for each archive and store it in a SQLite database.
   - Verify archive integrity by comparing stored and computed hashes.

3. SSH Upload Option:
   - Optionally upload archives to a remote server via SSH.
   - SSH credentials and destination paths can be configured.

4. GitHub Repository Upload:
   - Upload archives to a private GitHub repository using a local clone.
   - Uses SSH (RSA key authentication) for secure GitHub access.
   - Archives remain private in the repository.

5. Search and Extraction:
   - Search for a specific log or file within daily, weekly, or monthly archives.
   - Extract a selected file or decompress the entire archive.

6. Efficiency and Error Handling:
   - The script is modular, efficient, and extensively documented.
   - Robust error handling is provided for issues like corrupted archives, database errors, or failed uploads.

Setup and Usage Instructions:
  - Configure the SQLite database by editing DB_PATH.
  - For SSH uploads, set REMOTE_UPLOAD_ENABLED to True and configure SSH_HOST, SSH_PORT, SSH_USERNAME, etc.
  - For GitHub uploads, set GITHUB_UPLOAD_ENABLED to True, configure GITHUB_REPO_LOCAL_DIR (a local clone of your private repo),
    and ensure your SSH keys are set up.
  - Schedule the script via cron (e.g., daily) or run commands manually:
      • Archive tasks:        python3 log_manager.py archive
      • Verify integrity:      python3 log_manager.py verify <archive_file>
      • SSH upload:            python3 log_manager.py ssh-upload <archive_file>
      • GitHub upload:         python3 log_manager.py github-upload <archive_file>
      • Search for a file:     python3 log_manager.py search <filename> [--output <dir>]
      • Extract from archive:  python3 log_manager.py extract <archive_file> <filename> [--output <dir>]

Dependencies:
  - Python 3.6+
  - For SSH upload: pip3 install paramiko
  - For GitHub upload: a local Git clone and Git installed (the script calls Git commands via subprocess)

Ensure you run this script with appropriate privileges (e.g., sudo) when accessing system logs.

"""

import os
import sys
import tarfile
import logging
import sqlite3
import hashlib
import datetime
import argparse
import subprocess
import shutil

# Optional SSH upload via paramiko
try:
    import paramiko
except ImportError:
    paramiko = None

# ----------------------------------
# Configuration Variables
# ----------------------------------
# Log and archive directories
LOG_DIR = "/var/log"
ARCHIVE_BASE = "/var/log/archives"
DAILY_DIR = os.path.join(ARCHIVE_BASE, "daily")
WEEKLY_DIR = os.path.join(ARCHIVE_BASE, "weekly")
MONTHLY_DIR = os.path.join(ARCHIVE_BASE, "monthly")
DB_PATH = os.path.join(ARCHIVE_BASE, "archive.db")

# SSH upload configuration
REMOTE_UPLOAD_ENABLED = False  # Set True to enable SSH uploads
SSH_HOST = "remote.example.com"
SSH_PORT = 22
SSH_USERNAME = "username"
SSH_PASSWORD = "password"  # Alternatively, use SSH_KEY_PATH below
SSH_KEY_PATH = None         # e.g., "/home/user/.ssh/id_rsa"
REMOTE_DIR = "/remote/backup/archives"

# GitHub upload configuration (requires a local clone of your private repo)
GITHUB_UPLOAD_ENABLED = False  # Set True to enable GitHub uploads
GITHUB_REPO_LOCAL_DIR = "/path/to/local/clone"  # Local clone of the private GitHub repo
GITHUB_BRANCH = "main"   # Branch to which archives will be committed

# ----------------------------------
# Logging Setup
# ----------------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ----------------------------------
# Utility Functions
# ----------------------------------
def create_directories():
    """Ensure necessary directories exist."""
    for d in [ARCHIVE_BASE, DAILY_DIR, WEEKLY_DIR, MONTHLY_DIR]:
        if not os.path.exists(d):
            try:
                os.makedirs(d)
                logging.info(f"Created directory: {d}")
            except Exception as e:
                logging.error(f"Failed to create directory {d}: {e}")
                sys.exit(1)

def init_db():
    """Initialize the SQLite database for archive hashes."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS archives (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT UNIQUE,
                archive_type TEXT,
                archive_date TEXT,
                sha256 TEXT
            )
        """)
        conn.commit()
        conn.close()
        logging.info("SQLite database initialized.")
    except Exception as e:
        logging.error(f"Database initialization error: {e}")
        sys.exit(1)

def compute_file_hash(file_path):
    """Compute and return the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        logging.error(f"Error computing hash for {file_path}: {e}")
        return None

def store_archive_hash(filename, archive_type, archive_date, sha256):
    """Store the computed hash in the SQLite database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO archives (filename, archive_type, archive_date, sha256)
            VALUES (?, ?, ?, ?)
        """, (filename, archive_type, archive_date, sha256))
        conn.commit()
        conn.close()
        logging.info(f"Stored hash for {filename}.")
    except Exception as e:
        logging.error(f"Database error storing hash for {filename}: {e}")

def verify_archive_hash(filename):
    """Verify archive integrity by comparing stored and computed hashes."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT sha256 FROM archives WHERE filename = ?", (os.path.basename(filename),))
        row = cursor.fetchone()
        conn.close()
        if row is None:
            logging.error("Archive hash not found in database.")
            return False
        stored_hash = row[0]
        computed_hash = compute_file_hash(filename)
        if computed_hash is None:
            return False
        if stored_hash == computed_hash:
            logging.info(f"Archive {filename} integrity verified.")
            return True
        else:
            logging.error(f"Hash mismatch for {filename}.")
            return False
    except Exception as e:
        logging.error(f"Database error during verification for {filename}: {e}")
        return False

def create_archive(source_files, archive_path):
    """
    Create a tar.xz archive (using LZMA compression) containing source_files.
    :param source_files: List of file paths to include.
    :param archive_path: Destination archive path.
    """
    try:
        with tarfile.open(archive_path, "w:xz") as tar:
            for file_path in source_files:
                if os.path.exists(file_path):
                    # Use relative path (basename) for cleaner archive structure.
                    arcname = os.path.basename(file_path)
                    tar.add(file_path, arcname=arcname)
                else:
                    logging.warning(f"File not found: {file_path}")
        logging.info(f"Created archive: {archive_path}")
        return True
    except Exception as e:
        logging.error(f"Error creating archive {archive_path}: {e}")
        return False

# ----------------------------------
# Archiving Functions
# ----------------------------------
def create_daily_archive():
    """Create a daily archive of system logs from LOG_DIR (excluding ARCHIVE_BASE)."""
    today = datetime.date.today()
    archive_name = f"daily_{today.strftime('%Y%m%d')}.tar.xz"
    archive_path = os.path.join(DAILY_DIR, archive_name)
    logging.info(f"Creating daily archive: {archive_path}")

    source_files = []
    for root, dirs, files in os.walk(LOG_DIR):
        abs_root = os.path.abspath(root)
        if ARCHIVE_BASE in abs_root:
            continue
        for file in files:
            source_files.append(os.path.join(root, file))
    
    if create_archive(source_files, archive_path):
        file_hash = compute_file_hash(archive_path)
        store_archive_hash(archive_name, "daily", today.strftime('%Y-%m-%d'), file_hash)
    else:
        logging.error("Failed to create daily archive.")

def create_weekly_archive():
    """
    On Sundays, combine daily archives into a weekly archive and delete the daily archives.
    """
    today = datetime.date.today()
    if today.weekday() != 6:  # Sunday = 6
        logging.info("Today is not Sunday. Skipping weekly archive creation.")
        return

    start_of_week = today - datetime.timedelta(days=today.weekday())
    weekly_archive_name = f"weekly_{start_of_week.strftime('%Y%m%d')}_{today.strftime('%Y%m%d')}.tar.xz"
    weekly_archive_path = os.path.join(WEEKLY_DIR, weekly_archive_name)
    logging.info(f"Creating weekly archive: {weekly_archive_path}")

    daily_archives = []
    for n in range(7):
        day = start_of_week + datetime.timedelta(days=n)
        daily_archive_name = f"daily_{day.strftime('%Y%m%d')}.tar.xz"
        daily_archive_path = os.path.join(DAILY_DIR, daily_archive_name)
        if os.path.exists(daily_archive_path):
            daily_archives.append(daily_archive_path)
        else:
            logging.warning(f"Daily archive not found: {daily_archive_path}")
    
    if not daily_archives:
        logging.error("No daily archives found for weekly archiving.")
        return

    if create_archive(daily_archives, weekly_archive_path):
        file_hash = compute_file_hash(weekly_archive_path)
        store_archive_hash(weekly_archive_name, "weekly", today.strftime('%Y-%m-%d'), file_hash)
        # Delete daily archives now combined.
        for file in daily_archives:
            try:
                os.remove(file)
                logging.info(f"Deleted daily archive: {file}")
            except Exception as e:
                logging.error(f"Failed to delete daily archive {file}: {e}")
    else:
        logging.error("Failed to create weekly archive.")

def create_monthly_archive():
    """
    On the last day of the month, combine weekly archives into a monthly archive and delete them.
    """
    today = datetime.date.today()
    # If tomorrow is still in the same month, it's not the last day.
    if (today + datetime.timedelta(days=1)).month == today.month:
        logging.info("Today is not the last day of the month. Skipping monthly archive creation.")
        return

    month_year = today.strftime("%Y%m")
    monthly_archive_name = f"monthly_{month_year}.tar.xz"
    monthly_archive_path = os.path.join(MONTHLY_DIR, monthly_archive_name)
    logging.info(f"Creating monthly archive: {monthly_archive_path}")

    weekly_archives = []
    for file in os.listdir(WEEKLY_DIR):
        if file.startswith("weekly_") and file.endswith(".tar.xz") and month_year in file:
            weekly_archives.append(os.path.join(WEEKLY_DIR, file))
    
    if not weekly_archives:
        logging.error("No weekly archives found for monthly archiving.")
        return

    if create_archive(weekly_archives, monthly_archive_path):
        file_hash = compute_file_hash(monthly_archive_path)
        store_archive_hash(monthly_archive_name, "monthly", today.strftime('%Y-%m-%d'), file_hash)
        # Delete weekly archives now combined.
        for file in weekly_archives:
            try:
                os.remove(file)
                logging.info(f"Deleted weekly archive: {file}")
            except Exception as e:
                logging.error(f"Failed to delete weekly archive {file}: {e}")
    else:
        logging.error("Failed to create monthly archive.")

# ----------------------------------
# Remote Upload Functions
# ----------------------------------
def upload_archive_ssh(archive_path):
    """
    Upload an archive to a remote server using SSH.
    Returns True if successful.
    """
    if not REMOTE_UPLOAD_ENABLED:
        logging.info("SSH upload not enabled.")
        return False
    if paramiko is None:
        logging.error("Paramiko not installed. Cannot perform SSH upload.")
        return False
    if not os.path.exists(archive_path):
        logging.error(f"Archive not found: {archive_path}")
        return False

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if SSH_KEY_PATH:
            key = paramiko.RSAKey.from_private_key_file(SSH_KEY_PATH)
            ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USERNAME, pkey=key)
        else:
            ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USERNAME, password=SSH_PASSWORD)
        sftp = ssh.open_sftp()
        remote_path = os.path.join(REMOTE_DIR, os.path.basename(archive_path))
        sftp.put(archive_path, remote_path)
        sftp.close()
        ssh.close()
        logging.info(f"SSH upload successful: {archive_path} -> {remote_path}")
        return True
    except Exception as e:
        logging.error(f"SSH upload failed for {archive_path}: {e}")
        return False

def upload_archive_github(archive_path):
    """
    Upload an archive to a private GitHub repository.
    Assumes that a local clone of the repo exists and is configured to use SSH for authentication.
    """
    if not GITHUB_UPLOAD_ENABLED:
        logging.info("GitHub upload not enabled.")
        return False
    if not os.path.exists(archive_path):
        logging.error(f"Archive not found: {archive_path}")
        return False
    if not os.path.isdir(GITHUB_REPO_LOCAL_DIR):
        logging.error(f"GitHub repo directory not found: {GITHUB_REPO_LOCAL_DIR}")
        return False

    try:
        # Copy the archive into the GitHub repository directory.
        dest_path = os.path.join(GITHUB_REPO_LOCAL_DIR, os.path.basename(archive_path))
        shutil.copy2(archive_path, dest_path)
        logging.info(f"Copied archive to GitHub repo: {dest_path}")

        # Run Git commands to add, commit, and push.
        cmds = [
            ["git", "-C", GITHUB_REPO_LOCAL_DIR, "add", os.path.basename(archive_path)],
            ["git", "-C", GITHUB_REPO_LOCAL_DIR, "commit", "-m", f"Add archive {os.path.basename(archive_path)}"],
            ["git", "-C", GITHUB_REPO_LOCAL_DIR, "push", "origin", GITHUB_BRANCH]
        ]
        for cmd in cmds:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                logging.error(f"Git command failed: {' '.join(cmd)}\n{result.stderr}")
                return False
            else:
                logging.info(f"Git command succeeded: {' '.join(cmd)}")
        return True
    except Exception as e:
        logging.error(f"GitHub upload failed for {archive_path}: {e}")
        return False

# ----------------------------------
# Search and Extraction Functions
# ----------------------------------
def search_in_archive(archive_path, search_filename):
    """
    Search for a file within an archive.
    Returns the tarfile member if found.
    """
    try:
        with tarfile.open(archive_path, "r:xz") as tar:
            for member in tar.getmembers():
                if os.path.basename(member.name) == search_filename:
                    logging.info(f"Found {search_filename} in {archive_path}")
                    return member
        logging.info(f"{search_filename} not found in {archive_path}")
        return None
    except Exception as e:
        logging.error(f"Error searching in archive {archive_path}: {e}")
        return None

def extract_from_archive(archive_path, member, output_dir="."):
    """
    Extract a specific member from an archive.
    """
    try:
        with tarfile.open(archive_path, "r:xz") as tar:
            tar.extract(member, path=output_dir)
        logging.info(f"Extracted {member.name} from {archive_path} to {output_dir}")
        return True
    except Exception as e:
        logging.error(f"Error extracting {member.name} from {archive_path}: {e}")
        return False

def extract_entire_archive(archive_path, output_dir="."):
    """
    Extract the entire archive to the specified directory.
    """
    try:
        with tarfile.open(archive_path, "r:xz") as tar:
            tar.extractall(path=output_dir)
        logging.info(f"Extracted entire archive {archive_path} to {output_dir}")
        return True
    except Exception as e:
        logging.error(f"Error extracting archive {archive_path}: {e}")
        return False

def search_and_extract(search_filename, output_dir="."):
    """
    Search for a file across daily, weekly, and monthly archives.
    If found, prompt the user to extract the file or the entire archive.
    """
    for archive_dir in [DAILY_DIR, WEEKLY_DIR, MONTHLY_DIR]:
        for archive_file in os.listdir(archive_dir):
            if archive_file.endswith(".tar.xz"):
                archive_path = os.path.join(archive_dir, archive_file)
                member = search_in_archive(archive_path, search_filename)
                if member:
                    choice = input(f"Extract {search_filename} from {archive_file}? (y/n): ")
                    if choice.lower() == "y":
                        if extract_from_archive(archive_path, member, output_dir):
                            return
                    else:
                        choice_all = input(f"Extract entire archive {archive_file}? (y/n): ")
                        if choice_all.lower() == "y":
                            extract_entire_archive(archive_path, output_dir)
                            return
    logging.info(f"{search_filename} not found in any archives.")

# ----------------------------------
# Command-line Argument Parsing
# ----------------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="System Log Archiver and Manager")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Archive command: run daily, weekly, and monthly tasks.
    subparsers.add_parser("archive", help="Run archiving tasks")

    # Verify command: verify integrity of an archive.
    verify_parser = subparsers.add_parser("verify", help="Verify archive integrity")
    verify_parser.add_argument("archive_file", help="Path to the archive file")

    # SSH upload command.
    ssh_parser = subparsers.add_parser("ssh-upload", help="Upload archive via SSH")
    ssh_parser.add_argument("archive_file", help="Path to the archive file")

    # GitHub upload command.
    github_parser = subparsers.add_parser("github-upload", help="Upload archive to GitHub repository")
    github_parser.add_argument("archive_file", help="Path to the archive file")

    # Search command: search for a file within archives.
    search_parser = subparsers.add_parser("search", help="Search for a file in archives")
    search_parser.add_argument("filename", help="Filename to search for")
    search_parser.add_argument("--output", default=".", help="Directory to extract file")

    # Extract command: extract a specific file from an archive.
    extract_parser = subparsers.add_parser("extract", help="Extract file from a specific archive")
    extract_parser.add_argument("archive_file", help="Path to the archive file")
    extract_parser.add_argument("filename", help="Filename to extract")
    extract_parser.add_argument("--output", default=".", help="Directory to extract file")
    
    return parser.parse_args()

# ----------------------------------
# Main Function
# ----------------------------------
def main():
    args = parse_args()
    create_directories()
    init_db()

    if args.command == "archive":
        create_daily_archive()
        create_weekly_archive()
        create_monthly_archive()
    elif args.command == "verify":
        if verify_archive_hash(args.archive_file):
            print("Integrity verified.")
        else:
            print("Integrity verification failed.")
    elif args.command == "ssh-upload":
        if upload_archive_ssh(args.archive_file):
            print("SSH upload successful.")
        else:
            print("SSH upload failed.")
    elif args.command == "github-upload":
        if upload_archive_github(args.archive_file):
            print("GitHub upload successful.")
        else:
            print("GitHub upload failed.")
    elif args.command == "search":
        search_and_extract(args.filename, args.output)
    elif args.command == "extract":
        member = search_in_archive(args.archive_file, args.filename)
        if member:
            if extract_from_archive(args.archive_file, member, args.output):
                print(f"Extracted {args.filename} to {args.output}")
            else:
                print("Extraction failed.")
        else:
            print(f"{args.filename} not found in {args.archive_file}")
    else:
        print("No valid command provided. Use --help for usage instructions.")

if __name__ == "__main__":
    main()
