# FlapPyBird

A Python clone of the popular game **Flappy Bird** built with **Pygame**.

---

## 🕹️ Gameplay

Press **Left Mouse Button**  to flap the bird and avoid hitting the pipes. The game ends when the bird collides with a pipe or the ground.

---

## 📁 Project Structure
FlapPyBird-master/
├── assets/
│ └── sprites/ # All game images (bird, pipes, backgrounds, etc.)
├── src/
│ ├── utils/
│ │ ├── images.py # Handles loading all image assets
│ │ └── constants.py # Lists filenames for bird, pipe, and background sprites
│ └── flappy.py # Main game class
├── main.py # Entry point for the game
├── README.md # This file



---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.8+
- Pygame

### 📦 Install Dependencies

```bash
pip install pygame


##▶️ Running the Game

Just run the Flappy Bird.exe file

##🖼️ Assets
All game sprites (backgrounds, birds, pipes, UI) are located in:
assets/sprites/

Ensure that your constants.py lists only the file names, like:
BACKGROUNDS = ["background-day.png", "background-night.png"]

Your image loading logic will automatically append the full path in images.py.

