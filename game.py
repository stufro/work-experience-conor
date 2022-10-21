import pygame
class Game:
    def __init__(self, screen):
        self.screen = screen
        self.groups()

    def groups(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()

    def draw(self):
        self.all_sprites.draw(self.screen)

    def update(self):
        self.all_sprites.update()

    def run(self):
        self.draw()
        self.update()