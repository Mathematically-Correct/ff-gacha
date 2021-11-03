"""
Holds the Main Menu Screen.
"""
import pygame

import views.character_select
import views.screensettings as settings
from views.scene import Scene
from views.display_characters import DisplayCharacters


class MainMenu(Scene):
    """
    Main Menu Screen.
    Implemented Events: None but has one for if Space is pressed.
    To-Do: Implement Events for Play, Settings, and Exit Buttons.
    """
    def __init__(self):
        super().__init__()
        self.display_characters_text = settings.font_sm.render("Display Characters", 1, settings.WHITE)
        self.display_characters_button = self.display_characters_text.get_rect()
        self.play_text = settings.font_sm.render("Play", 1, settings.WHITE)
        self.play_button = self.play_text.get_rect()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                if self.display_characters_button.collidepoint(mouse_pos):
                    # If Enter button is clicked, goes to Main Menu
                    self.next_scene = DisplayCharacters()

                if self.play_button.collidepoint(mouse_pos):
                    self.next_scene = views.character_select.SelectCharacters()

    def update(self):
        pass

    def render(self):
        settings.screen.fill(settings.BLACK)
        text = settings.font_xl.render("Main Menu", 1, settings.WHITE)
        rect = text.get_rect()
        rect.centerx = settings.SCREEN_WIDTH // 2
        rect.centery = settings.SCREEN_HEIGHT // 4
        settings.screen.blit(text, rect)
        self.display_characters_button.centerx = settings.SCREEN_WIDTH // 2
        self.display_characters_button.centery = settings.SCREEN_HEIGHT // 1.5
        settings.screen.blit(self.display_characters_text, self.display_characters_button)
        self.play_button.centerx = settings.SCREEN_WIDTH // 2
        self.play_button.centery = settings.SCREEN_HEIGHT // 1.7
        settings.screen.blit(self.play_text,self.play_button)

