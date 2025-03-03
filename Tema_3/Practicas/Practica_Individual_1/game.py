import random
import time
import os

class Player:
    def __init__(self):
        self.health = True
        self.score = 0

class Outlaw:
    def __init__(self, name):
        self.name = name
        self.health = True

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_duel_status(round_number, player_roll, outlaw_roll, phase="First"):
    print(f"\n{phase} roll:")
    print(f"You rolled: {player_roll}")
    time.sleep(1)
    print(f"Outlaw rolled: {outlaw_roll}")
    time.sleep(1)

def calculate_round_score(round_number, player_health):
    base_scores = {1: 100, 2: 200, 3: 300, 4: 400, 5: 500}
    bonus_scores = {1: 50, 3: 100, 5: 250}
    
    score = base_scores[round_number]
    if player_health and round_number in bonus_scores:
        score += bonus_scores[round_number]
    return score

def play_duel(player_roll, outlaw_roll, player, outlaw, is_second_roll=False):
    display_duel_status(0, player_roll, outlaw_roll, "Second" if is_second_roll else "First")
    
    if player_roll > outlaw_roll:
        if not is_second_roll:
            outlaw.health = False
            print("You wounded the outlaw!")
        return "player_win"
    elif player_roll < outlaw_roll:
        if not is_second_roll:
            player.health = False
            print("You've been wounded!")
        return "outlaw_win"
    return "tie"

def play_round(player, outlaw, round_number):
    print(f"\nRound {round_number} - Fighting against {outlaw.name}!")
    print("Get ready for the duel...")
    time.sleep(2)

    while True:
        # First roll
        result = play_duel(roll_dice(), roll_dice(), player, outlaw)
        if result == "tie":
            print("It's a tie! Rolling again...")
            continue

        time.sleep(1)
        
        # Second roll
        result = play_duel(roll_dice(), roll_dice(), player, outlaw, True)
        
        if result == "tie":
            print("It's a tie! Both fighters reset and continue!")
            player.health = True
            outlaw.health = True
            continue
            
        if not player.health and result == "outlaw_win":
            print("You've been killed! Game Over!")
            return False
            
        if not outlaw.health and result == "player_win":
            score = calculate_round_score(round_number, player.health)
            player.score += score
            print(f"\nYou defeated {outlaw.name}!")
            print(f"Round score: {score} points")
            return True
            
        # Reset for next roll if no definitive outcome
        player.health = True
        outlaw.health = True

def main():
    outlaws = [
        "Quick-Draw McGraw", "Dead-Eye Dan", 
        "Wild Bill", "Doc Holliday", "Jesse James"
    ]
    
    while True:
        clear_screen()
        print("Welcome to Go Bullet!")
        print("Face 5 dangerous outlaws in deadly duels!")
        time.sleep(2)
        
        player = Player()
        
        for round_num in range(1, 6):
            clear_screen()
            outlaw = Outlaw(outlaws[round_num - 1])
            
            if not play_round(player, outlaw, round_num):
                print(f"\nGame Over! Final score: {player.score}")
                break
                
            if round_num < 5:
                print("\nPrepare for the next outlaw...")
                time.sleep(2)
        
        if round_num == 5 and player.health:
            print(f"\nCongratulations! You've won the game!")
            print(f"Final score: {player.score}")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()