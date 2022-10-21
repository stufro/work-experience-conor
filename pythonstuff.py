import pygame
from game import*
class start_game:
    def __init__(self, run):
        self.run = run
        self.screen = pygame.display.set_mode((500, 500))
        self.main_game = Game(self.screen)
    
    def run_game_from_server(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.main_game.run()

            pygame.display.update()
        pygame.quit()

