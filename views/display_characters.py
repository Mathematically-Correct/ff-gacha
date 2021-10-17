"""
Holds the Display Character Screen which shows all the different sprites
"""
import pygame
from views.scene import Scene
import views.screensettings as settings


class DisplayCharacters(Scene):
    """
    Title Screen.
    Implemented Events: Button for Menu
    """
    def __init__(self):
        super().__init__()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                if self.enter_button.collidepoint(mouse_pos):
                    #If Enter button is clicked, goes to Main Menu
                    pass

    def update(self):
        pass

    def render(self):
        settings.screen.fill(settings.BACKGROUND)
        text = settings.font_xl.render(settings.TITLE, 1, settings.WHITE)
        rect = text.get_rect()
        rect.centerx = settings.SCREEN_WIDTH // 2
        rect.centery = settings.SCREEN_HEIGHT // 2
        settings.screen.blit(text, rect)
