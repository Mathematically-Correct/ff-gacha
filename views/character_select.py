"""
Holds the Character Select screen.
"""
import pygame

import data.party
import views.mainmenu
import views.characterview
import views.map
from views.scene import Scene
import views.screensettings as settings
import data.character as characters


class SelectCharacters(Scene):
    """
    Select Characters Screen.
    Implemented Events: Button for Menu, Button to view Specific Character screen
    """

    def __init__(self):
        super().__init__()
        self.Rand = characters.Rand()
        self.back_text = settings.font_sm.render("Go Back", 1, settings.WHITE)
        self.back_button = self.back_text.get_rect()

    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                if self.Rand.rect.collidepoint(mouse_pos):
                    data.party.party.append(self.Rand)
                    self.next_scene = views.map.Map()

                if self.back_button.collidepoint(mouse_pos):
                    self.next_scene = views.mainmenu.MainMenu()

    def update(self):
        pass

    def render(self):
        settings.screen.fill(settings.BACKGROUND)
        settings.screen.blit(self.back_text, self.back_button)
        settings.screen.blit(self.Rand.image, self.Rand.rect)
