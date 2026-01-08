import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    OVerall class to manage game assets and behaviour
    """
    
    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        ) #it is called surface where a game elements can be displayed

        pygame.display.set_caption("Alien Invasion")
    
        self.ship = Ship(self)


        # self.bg_color = (230,230,230)

    def run_game(self):
        """start the main loop for game"""

        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            
            
# A helper method does work inside a class but isn’t meant to be called through an instance. In Python, a single leading underscore indicates a helper method.
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                    if event.type == pygame.K_RIGHT:
                        self.ship.moving_right=False
                    elif event.type == pygame.K_LEFT:
                        self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
#Pygame directly screen par draw nahi karta
# Pygame pehle memory me draw karta hai, phir ek command se screen update karta hai.
# pygame.display.flip() = “Ab jo kuch draw hua hai, wo player ko dikhao”
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()

 