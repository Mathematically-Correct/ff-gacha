"""
The Main File for FF-Gacha.
Should start the application
"""
import pygame
from views.titlescreen import TitleScene
import views.screensettings as settings


class Game:
    def __init__(self):
        self.active_scene = TitleScene()

    def is_quit_event(self, event, pressed_keys):
        x_out = event.type == pygame.QUIT
        ctrl = pressed_keys[pygame.K_LCTRL] or pressed_keys[pygame.K_RCTRL]
        q = pressed_keys[pygame.K_q]

        return x_out or (ctrl and q)

    def run(self):
        while self.active_scene is not None:
            # Get user input
            pressed_keys = pygame.key.get_pressed()
            filtered_events = []

            for event in pygame.event.get():
                if self.is_quit_event(event, pressed_keys):
                    self.active_scene.terminate()
                else:
                    filtered_events.append(event)

            # Manage scene
            self.active_scene.process_input(filtered_events, pressed_keys)
            self.active_scene.update()
            self.active_scene.render()
            self.active_scene = self.active_scene.next_scene

            # Update and tick
            pygame.display.flip()
            settings.clock.tick(settings.FPS)


if __name__ == '__main__':
    g = Game()
    g.run()
    pygame.quit()