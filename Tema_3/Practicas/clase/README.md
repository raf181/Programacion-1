# Just Eleven - Juego de Temporizador

Just Eleven es un juego donde el objetivo es detener un temporizador lo más cerca posible a los 11 segundos sin pasarse. Este proyecto implementa el juego como una aplicación web utilizando Flask.

## Características

- Juego para 2-6 jugadores
- 3 rondas por jugador
- Registro de los 10 mejores tiempos
- Interfaz web moderna y responsive
- Temporizador visual con feedback en tiempo real

## Instalación

1. Clona este repositorio o descarga los archivos
2. Instala las dependencias:

```bash
pip install flask
```

## Ejecución

Para ejecutar el juego, usa el siguiente comando en la terminal:

```bash
python app.py
```

O con Flask directamente:

```bash
flask run
```

Luego abre un navegador y visita: `http://127.0.0.1:5000`

## Cómo Jugar

1. Ejecuta el servidor Flask
2. Abre un navegador y ve a `http://127.0.0.1:5000`
3. Sigue las instrucciones en pantalla:
   - Configura el número de jugadores (2-6) y sus nombres
   - Cada jugador debe iniciar el temporizador y detenerlo lo más cerca posible a 11 segundos
   - Si el jugador se pasa de 11 segundos, su puntuación para esa ronda será 0
   - Después de 3 rondas, gana el jugador cuyo tiempo esté más cerca de 11 segundos sin pasarse

## Reglas del Juego

- El objetivo es detener un temporizador lo más cerca posible a 11 segundos sin pasarse
- Cada jugador tiene 3 rondas para intentar acercarse a los 11 segundos
- En cada turno, el jugador inicia un temporizador y debe detenerlo cuando crea que han pasado 11 segundos
- Si el jugador se pasa de 11 segundos, su puntuación para esa ronda será 0
- Gana el jugador cuyo tiempo esté más cerca de 11 segundos sin pasarse
- En caso de empate, gana el jugador que haya completado sus rondas en menos tiempo total

## Estructura del Proyecto

- `app.py`: Código principal de la aplicación Flask
- `static/`: Archivos estáticos (CSS, JavaScript)
  - `css/style.css`: Estilos de la aplicación
  - `js/script.js`: JavaScript común para todas las páginas
- `templates/`: Plantillas HTML
  - `base.html`: Plantilla base con la estructura común
  - `index.html`: Página de inicio
  - `setup.html`: Configuración del juego
  - `play.html`: Pantalla de juego con el temporizador
  - `results.html`: Resultados finales
  - `ranking.html`: Tabla de clasificación
  - `help.html`: Instrucciones del juego
  - `menu.html`: Menú post-juego
- `ranking.json`: Archivo que almacena los 10 mejores resultados

## Menú del Juego

- **Ayuda**: Muestra las reglas del juego
- **Jugar**: Inicia un nuevo juego
- **Ranking**: Muestra la tabla de clasificación de los 10 mejores jugadores
- **Salir**: Cierra el juego

## Licencia

Este proyecto es libre para uso educativo.
