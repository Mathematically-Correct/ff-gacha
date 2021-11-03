"""
Holds the Display Character Screen which shows all the different sprites
"""
import pygame

import views.mainmenu
from views.scene import Scene
import views.screensettings as settings
import views.display_characters
import data.character as characters


class DisplayCharacterView(Scene):
    """
    Display Specific Character View Screen.
    Implemented Events: Button to go back to main Character screen
    """

    def __init__(self, character):
        super().__init__()
        self.sprite = character

        self.back_text = settings.font_sm.render("Go Back", 1, settings.WHITE)
        self.back_button = self.back_text.get_rect()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                if self.back_button.collidepoint(mouse_pos):
                    self.next_scene = views.display_characters.DisplayCharacters()

    def update(self):
        pass

    def render(self):
        settings.screen.fill(settings.BACKGROUND)
        settings.screen.blit(self.back_text, self.back_button)
        settings.screen.blit(self.sprite.image, self.sprite.rect)
        sprite_name = settings.font_xl.render(self.sprite.name, 1, settings.BLACK)
        sprite_name_rect = sprite_name.get_rect()
        sprite_name_rect.centerx = settings.SCREEN_WIDTH // 1.65
        sprite_name_rect.centery = settings.SCREEN_HEIGHT // 1.1
        settings.screen.blit(sprite_name, sprite_name_rect)
