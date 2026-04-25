# Duskers - Text-Based Survival Strategy
This project was developed as a part of the JetBrains Academy (Hyperskill) curriculum to practice and implement advanced Object-Oriented Programming concepts in Python.
## About the Project
Duskers is a text-based strategic survival game built entirely in Python. The core focus of this project was to implement a clean, modular Object-Oriented Programming (OOP) architecture rather than relying on a single monolithic script. It features terminal-based exploration, resource management, and persistent game states.

## Key Features
* **Modular OOP Design**: Separation of concerns using distinct classes for game logic, menus, and entities.
* **Persistent State**: Game progress saving and loading utilizing `JSON`.
* **Command Line Interface**: Handled via Python's `argparse` module.
* **Resource Optimization**: Implementation of Python generators for efficient data handling.

## Project Structure
The repository is divided into logical components:
* `duskers.py` - The main entry point of the game.
* `Game.py` - Core game loop, state management, and primary logic.
* `Menu.py` - Handles the CLI-based user interface and input validation.
* `Robots.py` - Class definitions and behaviors for robotic entities within the game.
* `robotv1` / `title` - Assets and ASCII art resources for the terminal display.

## How to Run
To start the game, simply run the main script from your terminal:
\`\`\`bash
python duskers.py
\`\`\`

## Technologies Used
* Python 3
* JSON
* Argparse
