# Snake — Django

A browser-based Snake game built with Django, rendered on an HTML5 canvas and served through a Django view.

## Features
- Smooth grid-based snake movement
- Keyboard controls (arrow keys or WASD)
- Score tracking and persistent best score (via localStorage)
- Game over detection on wall or self-collision
- Play Again button to restart

## Tech Stack
- Python / Django (backend, serves the template)
- HTML5 Canvas, CSS, JavaScript (game logic runs client-side)

## Project Structure
```
snake_game/
├── game/
│   ├── templates/
│   │   └── game/
│   │       └── index.html
│   ├── views.py
│   └── urls.py
├── snake_game/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## Setup & Run

1. Clone the repository
   ```bash
   git clone https://github.com/fatma-shehata/snake-game.git
   cd snake-game
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install Django
   ```bash
   pip install django
   ```

4. Run the development server
   ```bash
   python manage.py runserver
   ```

5. Open your browser at
   ```
   http://127.0.0.1:8000/
   ```

## How to Play
- Use the Arrow keys or W/A/S/D to move the snake.
- Eat the orange food to grow and increase your score.
- Avoid hitting the walls or the snake's own body.
- Your best score is saved in the browser between sessions.
- Click **Play Again** after game over to restart.

## Author
Fatma shehata ewas  — Artificial Intelligence student, Kafr El-Sheikh University
