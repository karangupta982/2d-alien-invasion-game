import sys
import pygame
import settings from Settings
import ship from Ship

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            pygame.display.flip() 



if __name__ == '__main__':
    # make a game instance and running the game
    ai = AlienInvasion()
    ai.run_game()
