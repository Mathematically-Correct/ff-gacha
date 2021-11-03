"""
Holds all the characters
"""
import pygame
import views.screensettings as settings


class Rand(pygame.sprite.Sprite):
    name = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("portrait_art/randportrait.png")
        self.rect = self.image.get_rect()
        self.rect.center = (settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2)
        self.name = "Rand Al' Thor"
