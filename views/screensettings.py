"""
Carries the settings for the screen
"""

import pygame

"""
Window
"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "FF-GACHA"
FPS = 60

"""
The Different Main Colors of Game
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND = (136, 13, 30)

"""
The Fonts that are utilized for game.
"""
TITLE_FONT = 'garamond'
DEFAULT_FONT = None

# Make window
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Load assets
font_sm = pygame.font.SysFont(DEFAULT_FONT, 24)
font_md = pygame.font.SysFont(DEFAULT_FONT, 32)
font_xl = pygame.font.SysFont(TITLE_FONT, 96)
