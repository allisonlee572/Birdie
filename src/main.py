import pygame
from pygame.sprite import Group
import random as r
from player import Player
from config import *


class Puddles:

    def __init__(self):
        pygame.init()

        # self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.project_name = 'Puddles'

        pygame.display.set_caption(self.project_name)

        # Loop until the user clicks the close button.
        self.running = True

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('assets/bg01.png')

        self.player_group = Group()
        self.player = Player(400, 400, RIGHT, SPRITE_SIZE, self.screen)
        self.player_group.add(self.player)

        self.mode = GAME_STARTED

    def create_player(self):
        random_y = r.randint(0, WIDTH)
        random_direction = r.choice([LEFT, RIGHT])

        x = 0
        y = 0

        # if random_direction == LEFT:
            # x = WIDTH

        new_player = Player(x, y, random_direction, SPRITE_SIZE, self.screen)
        self.player_group.add(new_player)

    def game_loop(self):
        # -------- Main Program Loop -----------
        while self.running:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            self.screen.blit(self.background, (0, 0))
            # --- Limit to 60 frames per second
            self.clock.tick(FPS)
            current_fps = str(self.clock.get_fps())
            pygame.display.set_caption(f'{self.project_name}, fps: {current_fps}')

        # Close the window and quit.
        pygame.quit()

        if self.mode == GAME_NOT_STARTED:
            pass
        else:
            self.handle_game_in_session()

    def handle_game_in_session(self):
        self.player_group.update()

if __name__ == '__main__':
    puddles = Puddles()
    puddles.game_loop()
