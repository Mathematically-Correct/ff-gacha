"""
The Main File for FF-Gacha.
Should start the application
"""
import pygame

if __name__ == '__main__':
    background_colour = (136, 13, 30)
    (width, height) = (800, 600)

    screen = pygame.display.set_mode((width, height))
    screen.fill(background_colour)
    pygame.display.set_caption("FF-Gacha")
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False