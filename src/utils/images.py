import random
import os
import sys
from typing import List, Tuple
import pygame

# Add the project root to sys.path so Python can find the 'src' package
sys.path.append(r"C:\Users\swapb\Downloads\FlapPyBird-master\FlapPyBird-master")

# Import constants
from src.utils.constants import BACKGROUNDS, PIPES, PLAYERS


class Images:
    numbers: List[pygame.Surface]
    game_over: pygame.Surface
    welcome_message: pygame.Surface
    base: pygame.Surface
    background: pygame.Surface
    player: Tuple[pygame.Surface, pygame.Surface, pygame.Surface]
    pipe: Tuple[pygame.Surface, pygame.Surface]

    def __init__(self) -> None:
        # Absolute path to the sprites directory
        self.sprite_path = r"C:\\Users\\swapb\\Downloads\\FlapPyBird-master\\FlapPyBird-master\\assets\\sprites"

        # Load number sprites (0-9)
        self.numbers = [
            pygame.image.load(os.path.join(self.sprite_path, f"{num}.png")).convert_alpha()
            for num in range(10)
        ]

        # Game over sprite
        self.game_over = pygame.image.load(
            os.path.join(self.sprite_path, "gameover.png")
        ).convert_alpha()

        # Welcome screen sprite
        self.welcome_message = pygame.image.load(
            os.path.join(self.sprite_path, "message.png")
        ).convert_alpha()

        # Base (ground) sprite
        self.base = pygame.image.load(
            os.path.join(self.sprite_path, "base.png")
        ).convert_alpha()

        # Load randomized assets
        self.randomize()

    def randomize(self):
        # Randomly select background, player, and pipe
        rand_bg = random.randint(0, len(BACKGROUNDS) - 1)
        rand_player = random.randint(0, len(PLAYERS) - 1)
        rand_pipe = random.randint(0, len(PIPES) - 1)

        # Load background
        self.background = pygame.image.load(
            os.path.join(self.sprite_path, BACKGROUNDS[rand_bg])
        ).convert()

        # Load player animation frames
        self.player = tuple(
            pygame.image.load(os.path.join(self.sprite_path, frame)).convert_alpha()
            for frame in PLAYERS[rand_player]
        )

        # Load pipe images
        pipe_img = pygame.image.load(
            os.path.join(self.sprite_path, PIPES[rand_pipe])
        ).convert_alpha()
        self.pipe = (
            pygame.transform.flip(pipe_img, False, True),
            pipe_img
        )
