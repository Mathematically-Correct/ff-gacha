"""
Holds the Title Screen.
"""
import pygame
from views.scene import Scene
import views.screensettings as settings
from views.mainmenu import MainMenu


class TitleScene(Scene):
    def __init__(self):
        super().__init__()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = MainMenu()

    def update(self):
        pass

    def render(self):
        settings.screen.fill(settings.BACKGROUND)
        text = settings.font_xl.render(settings.TITLE, 1, settings.WHITE)
        rect = text.get_rect()
        rect.centerx = settings.SCREEN_WIDTH // 2
        rect.centery = settings.SCREEN_HEIGHT // 2
        settings.screen.blit(text, rect)
