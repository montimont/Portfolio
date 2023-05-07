import pygame
import sys
import time
from settings import *
from level import level


class Game:
    def __init__(self):

        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (WIDTH, HEIGTH))
        pygame.display.set_caption('Ori Adventure')
        self.clock = pygame.time.Clock()

        self.level = level()

        # sound
        main_sound = pygame.mixer.Sound(
            '/Users/montebolds/Portofolio/Advanced/Zelda Clone/Zelda-main/15 - fixes audio/audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def run(self):
        last_time = time.time()
        while True:

            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            # game logic
            self.display_surface.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()