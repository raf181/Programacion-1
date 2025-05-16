# Importación de librerías necesarias
from flask import Flask, render_template, request, redirect, url_for, session, flash
# import random  # No utilizado actualmente
import time  # Para medir tiempos en el juego
import json  # Para manejar el ranking en formato JSON
import os    # Para verificar la existencia del archivo de ranking
from datetime import datetime  # Para registrar la fecha de las partidas

# Inicialización de la aplicación Flask
app = Flask(__name__)
# Clave secreta necesaria para mantener la sesión segura
app.secret_key = "just_eleven_secret_key"

# Archivo para almacenar el ranking
RANKING_FILE = "ranking.json"

# Función para cargar el ranking desde el archivo JSON
def load_ranking():
    """
    Carga la lista de mejores puntuaciones desde el archivo.
    Si el archivo no existe o está corrupto, devuelve una lista vacía.
    
    Returns:
        list: Lista de diccionarios con la información del ranking
    """
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return []
    return []

# Función para guardar el ranking
def save_ranking(ranking):
    """
    Guarda la lista de mejores puntuaciones en el archivo.
    Ordena la lista por puntuación (de mayor a menor) y
    conserva solo las 10 mejores puntuaciones.
    
    Args:
        ranking (list): Lista de diccionarios con la información del ranking
    """
    # Ordenar por puntuación (de mayor a menor)
    ranking.sort(key=lambda x: x["score"], reverse=True)
    
    # Mantener solo los 10 mejores
    ranking = ranking[:10]
    
    with open(RANKING_FILE, "w") as f:
        json.dump(ranking, f)

@app.route("/")
def index():
    """
    Ruta principal de la aplicación. Muestra la página de bienvenida.
    Reinicia el estado del juego si existe una sesión anterior.
    
    Returns:
        template: Página de inicio (index.html)
    """
    # Reiniciar el juego
    if "game_state" in session:
        session.pop("game_state")
    return render_template("index.html")

@app.route("/setup", methods=["GET", "POST"])
def setup():
    """
    Ruta para configurar el juego. Permite establecer el número de jugadores,
    sus nombres y el tiempo objetivo personalizado.
    
    Si se accede via GET: Muestra el formulario de configuración
    Si se accede via POST: Procesa los datos del formulario y comienza el juego
    
    Returns:
        template/redirect: Formulario de configuración o redirección a la página de juego
    """
    if request.method == "POST":
        num_players = int(request.form.get("num_players", 2))
        player_names = []
        
        # Recopilación de nombres de jugadores desde el formulario
        for i in range(1, num_players + 1):
            name = request.form.get(f"player_{i}", f"Jugador {i}")
            player_names.append(name)
        
        # Obtener el tiempo objetivo personalizado (mínimo 10 segundos)
        target_time = float(request.form.get("target_time", 11))
        if target_time < 10:
            target_time = 10
        
        # Inicializar el estado del juego en la sesión
        session["game_state"] = {
            "players": player_names,         # Lista de nombres de jugadores
            "scores": [0] * num_players,     # Puntuaciones inicializadas a 0
            "rounds": 3,                     # Número total de rondas
            "current_round": 1,              # Ronda actual
            "current_player": 0,             # Índice del jugador actual
            "start_time": time.time(),       # Tiempo de inicio del juego completo
            "target_time": target_time       # Tiempo objetivo personalizado
        }
        
        return redirect(url_for("play"))
    
    return render_template("setup.html")

@app.route("/play", methods=["GET", "POST"])
def play():
    """
    Ruta principal del juego. Gestiona la lógica del temporizador y las rondas.
    
    Si se accede via GET: Muestra la interfaz del juego con el temporizador
    Si se accede via POST: Procesa acciones (iniciar/detener el temporizador)
    
    Returns:
        template/redirect: Interfaz de juego o redirección según la acción
    """
    # Verificar que exista una sesión de juego
    if "game_state" not in session:
        return redirect(url_for("index"))
    
    game_state = session["game_state"]
    
    # Inicializar variables de tiempo si no existen
    if "timer_start" not in game_state:
        game_state["timer_start"] = None  # Marca de tiempo cuando se inicia el temporizador
    if "timer_result" not in game_state:
        game_state["timer_result"] = None  # Resultado del tiempo detenido
    
    if request.method == "POST":
        action = request.form.get("action", "")
        
        # Si el jugador inicia el temporizador
        if action == "start":
            game_state["timer_start"] = time.time()  # Guardar tiempo de inicio
            game_state["timer_result"] = None  # Reiniciar resultado anterior
            session["game_state"] = game_state
            return redirect(url_for("play"))
        
        # Si el jugador detiene el temporizador
        elif action == "stop" and game_state["timer_start"] is not None:
            stop_time = time.time()
            elapsed_time = stop_time - game_state["timer_start"]  # Calcular tiempo transcurrido
            game_state["timer_result"] = round(elapsed_time, 2)  # Redondear a 2 decimales
            
            # Obtener el tiempo objetivo (por defecto 11 si no se estableció)
            target_time = game_state.get("target_time", 11)
            
            # Sistema de puntuación: 
            # - Si no se pasa del objetivo: la puntuación es el tiempo exacto
            # - Si se pasa: se aplica una penalización proporcional al exceso
            if elapsed_time <= target_time:
                # Si no se pasa, la puntuación es el tiempo exacto
                game_state["scores"][game_state["current_player"]] = elapsed_time
            else:
                # Si se pasa, calculamos una penalización que disminuye la puntuación 
                # cuanto más se pase del tiempo objetivo
                over_time = elapsed_time - target_time
                # La penalización es proporcional a cuánto se pasa
                penalty_factor = 1 / (1 + over_time)  # Factor de penalización que disminuye cuanto más te pasas
                adjusted_score = elapsed_time * penalty_factor
                game_state["scores"][game_state["current_player"]] = round(adjusted_score, 2)
        
            # Lógica para pasar al siguiente jugador o ronda
            game_state["timer_start"] = None
            game_state["current_player"] += 1
            
            # Si todos los jugadores han jugado, avanzar a la siguiente ronda
            if game_state["current_player"] >= len(game_state["players"]):
                game_state["current_player"] = 0
                game_state["current_round"] += 1
            
            # Verificar si el juego ha terminado (todas las rondas jugadas)
            if game_state["current_round"] > game_state["rounds"]:
                game_state["end_time"] = time.time()
                game_state["total_time"] = game_state["end_time"] - game_state["start_time"]
                
                session["game_state"] = game_state
                return redirect(url_for("results"))
            
            session["game_state"] = game_state
            return redirect(url_for("play"))
        
        session["game_state"] = game_state
        return redirect(url_for("play"))
    
    # Renderizar la plantilla con el estado actual del juego
    return render_template("play.html", 
                          game_state=game_state, 
                          current_player=game_state["players"][game_state["current_player"]])

@app.route("/results")
def results():
    """
    Ruta para mostrar los resultados del juego.
    Calcula el ganador, actualiza el ranking y muestra la pantalla de resultados.
    
    Returns:
        template/redirect: Página de resultados o redirección a inicio si no hay juego
    """
    # Verificar que exista una sesión de juego
    if "game_state" not in session:
        return redirect(url_for("index"))
    
    game_state = session["game_state"]
    winner_idx = find_winner(game_state["scores"])  # Determinar el ganador
    
    # Obtener información del ganador para el ranking
    winner_name = game_state["players"][winner_idx]
    winner_score = game_state["scores"][winner_idx]
    
    # Actualizar el ranking con la nueva puntuación
    ranking = load_ranking()
    ranking.append({
        "name": winner_name,           # Nombre del jugador ganador
        "score": winner_score,         # Puntuación obtenida
        "time": game_state["total_time"],  # Tiempo total de juego
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")  # Fecha y hora
    })
    save_ranking(ranking)
    
    # Renderizar la plantilla de resultados
    return render_template("results.html", 
                          game_state=game_state, 
                          winner=game_state["players"][winner_idx],
                          winner_score=game_state["scores"][winner_idx])

@app.route("/ranking")
def ranking():
    """
    Ruta para mostrar la tabla de clasificación con las mejores puntuaciones.
    
    Returns:
        template: Página de ranking
    """
    ranking_list = load_ranking()
    return render_template("ranking.html", ranking=ranking_list)

@app.route("/help")
def help_page():
    """
    Ruta para mostrar la página de ayuda con las reglas del juego.
    
    Returns:
        template: Página de ayuda
    """
    return render_template("help.html")

# Función para encontrar el ganador (mayor puntuación, con penalización para los que se pasan)
def find_winner(scores):
    """
    Determina el índice del jugador ganador basado en las puntuaciones.
    El ganador es quien tenga la puntuación más alta (después de aplicar penalizaciones).
    
    Args:
        scores (list): Lista de puntuaciones de los jugadores
        
    Returns:
        int: Índice del jugador ganador
    """
    if not scores:
        return 0
    
    # Simplemente encontramos la mayor puntuación (ya aplicamos la penalización al calcular la puntuación)
    winner_idx = 0
    highest_score = scores[0]
    
    # Recorremos todas las puntuaciones buscando la más alta
    for i, score in enumerate(scores):
        if score > highest_score:
            highest_score = score
            winner_idx = i
    
    return winner_idx

@app.route("/menu")
def menu():
    """
    Ruta para mostrar el menú de opciones post-juego.
    
    Returns:
        template: Página de menú
    """
    return render_template("menu.html")

if __name__ == "__main__":
    # Ejecutar la aplicación en modo de depuración
    # Nota: En un entorno de producción, debug debería ser False
    app.run(debug=True)
