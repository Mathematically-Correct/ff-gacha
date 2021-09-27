"""
Holds the Main Menu Screen.
"""
import pygame
import views.screensettings as settings
from views.scene import Scene


class MainMenu(Scene):
    """
    Main Menu Screen.
    Implemented Events: None but has one for if Space is pressed.
    To-Do: Implement Events for Play, Settings, and Exit Buttons.
    """
    def __init__(self):
        super().__init__()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

    def update(self):
        pass

    def render(self):
        settings.screen.fill(settings.BLACK)
        text = settings.font_xl.render("Main Menu", 1, settings.WHITE)
        rect = text.get_rect()
        rect.centerx = settings.SCREEN_WIDTH // 2
        rect.centery = settings.SCREEN_HEIGHT // 4
        settings.screen.blit(text, rect)
