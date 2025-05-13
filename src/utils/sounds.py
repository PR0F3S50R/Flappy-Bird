import sys
import os
import pygame


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class Sounds:
    die: pygame.mixer.Sound
    hit: pygame.mixer.Sound
    point: pygame.mixer.Sound
    swoosh: pygame.mixer.Sound
    wing: pygame.mixer.Sound

    def __init__(self) -> None:
        ext = "wav" if "win" in sys.platform else "ogg"

        self.die = pygame.mixer.Sound(resource_path(f"assets/audio/die.{ext}"))
        self.hit = pygame.mixer.Sound(resource_path(f"assets/audio/hit.{ext}"))
        self.point = pygame.mixer.Sound(resource_path(f"assets/audio/point.{ext}"))
        self.swoosh = pygame.mixer.Sound(resource_path(f"assets/audio/swoosh.{ext}"))
        self.wing = pygame.mixer.Sound(resource_path(f"assets/audio/wing.{ext}"))
