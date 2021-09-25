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
        self.button = pygame.Rect(375, 450, 50, 50)

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.next_scene = MainMenu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if self.button.collidepoint(mouse_pos):
                    # prints current location of mouse
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
        pygame.draw.rect(settings.screen, [255, 0, 0], self.button)
