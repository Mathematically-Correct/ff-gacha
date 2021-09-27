"""
Basic Scene Class File.
"""
import pygame
import views.screensettings as settings


class Scene():
    """
    Is the base class for the Scenes
    Normally each scene is an object/subclass of this.
    """
    def __init__(self):
        self.next_scene = self

    def process_input(self, events, pressed_keys):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def terminate(self):
        self.next_scene = None

    def update_screen(self, new_w, new_h):
        settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT = new_w, new_h
        settings.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), pygame.RESIZABLE)
