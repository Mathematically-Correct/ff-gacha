"""
Holds all the characters
"""
import pygame
import views.screensettings as settings
#  player_img = pygame.image.load(os.path.join(resources, '')).convert()


class Rand(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #  self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
