# 🐍 Snake Game in Python

A classic Snake game built with Python's `turtle` module. I made it to practice object-oriented programming, so each part of the game (the snake, the food, the scoreboard and the game itself) lives in its own class.

![Gameplay demo](assets/demo.gif)

## Features

- Smooth, grid-based snake movement with arrow key controls
- The snake grows every time it eats food, and the score goes up
- Game ends when you hit the wall or run into your own tail
- Press **SPACE** after game over to restart instantly, or **ESC** to quit
- Can't reverse straight into yourself (the snake ignores a 180° turn)

## Getting started

You only need Python 3.8 or newer. `turtle` and `tkinter` come with the standard Python installation, so there is nothing else to install.

```bash
git clone https://github.com/<your-username>/snake-game-python.git
cd snake-game-python
python main.py
```

> On some Linux distributions, `tkinter` is packaged separately. If you get an import error, install it with `sudo apt install python3-tk`.

## Controls

| Key | Action |
|-----|--------|
| ↑ ↓ ← → | Steer the snake |
| SPACE | Restart (after game over) |
| ESC | Quit |

## Project structure

```
snake-game/
├── main.py     # Game class: sets up the screen, key bindings and the game loop
├── snake.py    # Snake class: movement, growing, turning, tail collision, reset
├── food.py     # Food class (inherits from Turtle): appears at random positions
├── score.py    # ScoreCard class (inherits from Turtle): score and game over text
└── README.md
```

## OOP concepts used

- **Classes and objects:** `Game`, `Snake`, `Food` and `ScoreCard` each have one clear job.
- **Inheritance:** `Food` and `ScoreCard` extend `turtle.Turtle`, so they get drawing and movement for free and add their own behaviour on top.
- **Composition:** `Snake` is built from a list of `Turtle` segments, and `Game` is built from a `Snake`, a `Food` and a `ScoreCard`.
- **Encapsulation:** each class manages its own state. For example, `Game` just calls `snake.reset()` or `scorecard.update_score()` without caring how they work inside.
- **Constants:** values like move distance, headings and wall distance are defined once and reused.

## How it works

Every frame, `Game.run()` moves the snake one step and then checks three things: did the head reach the food (grow and score), did it hit a wall, and did it hit its own body. If it hit something, the game goes into a "game over" state and waits for you to press SPACE or ESC. Restarting resets the snake, score and food without recreating the window.

## Ideas for the future

- Save a high score to a file
- Speed up as the score increases
- Make sure food never spawns on top of the snake
- Add a start menu and difficulty levels

## License

MIT. Feel free to use it, learn from it, or build on it.
