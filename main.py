import pygame
import sys
from scripts.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Color Beatchange Platformer')
        self.clock = pygame.time.Clock()
        self.player = Player()

    def run(self):
        while True:
            dt = self.clock.tick(60) / 1000.0  # Convert to seconds
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            self.player.update(dt)
            self.screen.fill((0, 0, 0))
            self.player.draw(self.screen)
            pygame.display.update()

if __name__ == '__main__':
    Game().run()


    