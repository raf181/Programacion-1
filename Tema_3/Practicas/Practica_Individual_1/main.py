import os
import time
import random

# Configuración de cada ronda: puntos base y puntos extra si el jugador pasa ileso.
ROUND_CONFIG = {
    1: {"base": 100, "bonus": 50},
    2: {"base": 200, "bonus": 0},
    3: {"base": 300, "bonus": 100},
    4: {"base": 400, "bonus": 0},
    5: {"base": 500, "bonus": 250}
}

# Lista de nombres de forajidos del Oeste
OUTLAW_NAMES = [
    "Billy el Niño", "Jesse James", "Butch Cassidy", "Sundance Kid", "Belle Starr",
    "Doc Holliday", "Calamity Jane", "Black Bart", "Wild Bill Hickok", "Cherokee Bill",
    "Sam Bass", "Dalton Gang", "Cole Younger", "John Wesley Hardin", "Annie Oakley",
    "El Pistolero", "Muerto Jim", "Gatillo Veloz", "Cara Cicatriz", "Pistolas Gemelas"
]

# Emojis para diferentes situaciones del juego
EMOJIS = {
    "gun": "🔫",
    "cowboy": "🤠",
    "dead": "💀",
    "star": "⭐",
    "hit": "💥",
    "win": "🏆",
    "medal": "🏅",
    "bullet": "🔸",
    "dice": "🎲",
    "heart": "❤️",
    "broken_heart": "💔",
    "score": "🏅",
    "fire": "🔥",
    "cool": "😎",
    "sad": "😢",
    "angry": "😠",
    "hat": "👒",
    "clock": "⏱️",
    "boom": "💥",
    "trophy": "🏆",
    "health_full": "█",
    "health_empty": "░"
}

# Representaciones de las caras del dado
DICE_FACES = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

def clear_screen():
    """Limpia la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_health(name, health_level):
    """
    Muestra la salud del personaje con corazones.
    health_level puede ser: 2 (salud completa), 1 (herido), 0 (muerto)
    """
    if health_level == 2:  # Completamente sano
        hearts = f"{EMOJIS['heart']} {EMOJIS['heart']}"
        status = "Sano"
    elif health_level == 1:  # Herido
        hearts = f"{EMOJIS['heart']} {EMOJIS['broken_heart']}"
        status = "Herido"
    else:  # Muerto
        hearts = f"{EMOJIS['dead']} {EMOJIS['dead']}"
        status = "Muerto"
    
    print(f"{name}: {hearts} - {status}")

def animate_dice_roll():
    """Animación para el lanzamiento de dados con las 6 caras clásicas."""
    for _ in range(8):
        # Seleccionar aleatoriamente dos caras de dado para mostrar
        face1 = random.choice(DICE_FACES)
        face2 = random.choice(DICE_FACES)
        print(f"\r{EMOJIS['dice']} {face1} {EMOJIS['dice']} {face2}", end="")
        time.sleep(0.1)
    print("\r", end="")

def roll_dice():
    """Simula el lanzamiento de dos dados y retorna la suma."""
    animate_dice_roll()
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    # Mostrar el resultado final de los dados
    print(f"{EMOJIS['dice']} {DICE_FACES[die1-1]} {EMOJIS['dice']} {DICE_FACES[die2-1]} = {die1 + die2}")
    return die1 + die2

def play_round(round_number, outlaw_name, player_name):
    """
    Ejecuta la lógica de una ronda.
    Se realizan dos lanzamientos de dados (primer y segundo lanzamiento).
    En caso de empate en cualquiera de los lanzamientos, se repite la ronda.
    
    Retorna:
      - ganado (bool): True si el jugador gana la ronda, False si muere.
      - puntos (int): Puntos obtenidos en la ronda (0 si muere).
      - intacto (bool): True si el jugador no se hirió en ningún lanzamiento.
    """
    # Inicializamos el estado de salud de ambos personajes
    # 2 = completamente sano, 1 = herido, 0 = muerto
    player_health = 2
    outlaw_health = 2
    
    while True:
        print(f"\n=== Ronda {round_number}: {player_name} {EMOJIS['cowboy']} vs {outlaw_name} {EMOJIS['gun']} ===")
        
        # Mostrar salud con corazones
        display_health(player_name, player_health)
        display_health(outlaw_name, outlaw_health)
        
        time.sleep(1)
        print(f"\n{EMOJIS['bullet']} Primer lanzamiento:")
        print(f"{player_name} lanza los dados...")
        player_roll = roll_dice()
        print(f"{outlaw_name} lanza los dados...")
        outlaw_roll = roll_dice()
        print(f"{player_name}: {player_roll} | {outlaw_name}: {outlaw_roll}")
        time.sleep(1)
        
        # Verificar empate en el primer lanzamiento
        if player_roll == outlaw_roll:
            print(f"¡Empate en el primer lanzamiento! {EMOJIS['clock']} Se repite la ronda...")
            time.sleep(1)
            continue
        
        # Determinar el estado luego del primer lanzamiento
        if player_roll > outlaw_roll:
            print(f"¡Buen tiro, {player_name}! {EMOJIS['cool']} El forajido queda herido {EMOJIS['hit']} y tú permaneces ileso.")
            outlaw_health = 1  # El forajido queda herido
            player_intacto = True
        else:
            print(f"¡Mala jugada, {player_name}! {EMOJIS['sad']} Quedas herido {EMOJIS['hit']}.")
            player_health = 1  # El jugador queda herido
            player_intacto = False
        
        # Actualizar y mostrar salud después del primer lanzamiento
        print("\nEstado de salud después del primer lanzamiento:")
        display_health(player_name, player_health)
        display_health(outlaw_name, outlaw_health)
        
        print(f"\n{EMOJIS['bullet']} Segundo lanzamiento:")
        print(f"{player_name} lanza los dados...")
        player_roll2 = roll_dice()
        print(f"{outlaw_name} lanza los dados...")
        outlaw_roll2 = roll_dice()
        print(f"{player_name}: {player_roll2} | {outlaw_name}: {outlaw_roll2}")
        time.sleep(1)
        
        # Verificar empate en el segundo lanzamiento
        if player_roll2 == outlaw_roll2:
            print(f"¡Empate en el segundo lanzamiento! {EMOJIS['clock']} Se repite la ronda...")
            # Restauramos la salud para la nueva ronda
            player_health = 2
            outlaw_health = 2
            time.sleep(1)
            continue
        
        # Resultado definitivo basado en el estado del primer lanzamiento
        if player_health == 1 and player_roll2 < outlaw_roll2:
            print(f"\nComo ya estabas herido, {player_name}, en el segundo lanzamiento sucumbes. ¡Has muerto! {EMOJIS['dead']}")
            # Actualizar y mostrar salud final
            player_health = 0  # El jugador muere
            print("\nEstado de salud final:")
            display_health(player_name, player_health)
            display_health(outlaw_name, outlaw_health)
            return False, 0, False  # El jugador muere, no suma puntos.
        else:
            print(f"\nEl forajido {outlaw_name} muere {EMOJIS['dead']}. {player_name} avanza a la siguiente ronda {EMOJIS['win']}.")
            # Actualizar y mostrar salud final
            outlaw_health = 0  # El forajido muere
            print("\nEstado de salud final:")
            display_health(player_name, player_health)
            display_health(outlaw_name, outlaw_health)
            # Calcular puntos: base + bonus si intacto
            config = ROUND_CONFIG.get(round_number, {"base": 0, "bonus": 0})
            puntos = config["base"] + (config["bonus"] if player_intacto else 0)
            return True, puntos, True

def play_game(player_name):
    """Función principal que gestiona el juego completo."""
    total_puntos = 0
    ronda_actual = 1

    while ronda_actual <= 5:
        clear_screen()
        print(f"--- Juego 'Go Bullet!' {EMOJIS['gun']} - Ronda {ronda_actual} ---")
        print(f"Vaquero: {player_name} {EMOJIS['cowboy']}")
        
        # Seleccionar un nombre de forajido aleatorio
        outlaw_name = random.choice(OUTLAW_NAMES)
        print(f"Te enfrentas a: {outlaw_name} {EMOJIS['angry']}")
        time.sleep(1)
        
        # Jugar la ronda (se repite en caso de empate)
        ganado, puntos_ronda, intacto = play_round(ronda_actual, outlaw_name, player_name)
        if not ganado:
            print(f"\nFin del juego. {EMOJIS['dead']} Puntuación total de {player_name}: {total_puntos} {EMOJIS['score']}")
            return total_puntos
        
        total_puntos += puntos_ronda
        print(f"\n¡Has ganado la ronda {ronda_actual}, {player_name}! {EMOJIS['win']}")
        print(f"Puntos obtenidos en esta ronda: {puntos_ronda} {EMOJIS['star']}")
        print(f"Puntuación acumulada: {total_puntos} {EMOJIS['score']}")
        input(f"\nPresiona Enter para continuar a la siguiente ronda... {EMOJIS['bullet']}")
        ronda_actual += 1

    clear_screen()
    print(f"¡Felicidades, {player_name}! {EMOJIS['trophy']} Has derrotado a todos los forajidos.")
    print(f"Puntuación final: {total_puntos} {EMOJIS['medal']}")
    return total_puntos

def main():
    """Bucle principal del juego, permite reiniciar o salir."""
    while True:
        clear_screen()
        print(f"Bienvenido a 'Go Bullet!' {EMOJIS['gun']} {EMOJIS['cowboy']}\n")
        print(f"El juego de duelos del salvaje oeste {EMOJIS['fire']}\n")
        
        # Solicitar el nombre del jugador
        player_name = input(f"Ingresa tu nombre, vaquero {EMOJIS['hat']}: ").strip()
        if player_name == "":
            player_name = "Vaquero Anónimo" 
            
        play_game(player_name)
        opcion = input(f"\n¿Deseas jugar de nuevo? (s/n): ").strip().lower()
        if opcion != 's':
            print(f"\nGracias por jugar, {player_name}. ¡Hasta la próxima! {EMOJIS['cowboy']}")
            break

if __name__ == "__main__":
    main()
