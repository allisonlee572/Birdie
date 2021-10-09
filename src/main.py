import pygame
from pygame.sprite import Group
import random as r
from player import Player
from enemy1 import Enemy1
from enemy2 import Enemy2
from battle_player import BattlePlayer
from battle_enemy1 import BattleEnemy1
from battle_enemy2 import BattleEnemy2
from bullet import Bullet
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
        self.player = Player(20, 305, RIGHT, SPRITE_SIZE, self.screen)
        self.player_group.add(self.player)

        self.enemy1_group = Group()
        self.enemy1 = Enemy1(200, 330, RIGHT, SPRITE_SIZE, self.screen)
        self.enemy1_group.add(self.enemy1)

        self.enemy2_group = Group()
        self.enemy2 = Enemy2(400,330, RIGHT, SPRITE_SIZE, self.screen)
        self.enemy2_group.add(self.enemy2)

        self.battle_player_group = Group()
        self.battle_player = BattlePlayer(WIDTH/2, 330, RIGHT, SPRITE_SIZE, self.screen)

        self.battle_enemy1_group = Group()
        self.battle_enemy1 = BattleEnemy1(WIDTH/2, 0, RIGHT, SPRITE_SIZE, self.screen)

        self.battle_enemy2_group = Group()
        self.battle_enemy2 = BattleEnemy2(WIDTH / 2, 0, RIGHT, SPRITE_SIZE, self.screen)

        self.bullet_group = Group()

        self.mode = GAME_STARTED

        self.bullet_cooldown_timer = BULLET_COOLDOWN_DELAY

    def create_bullet(self):
        random_y = r.randint(0, HEIGHT)
        new_bullet = Bullet(0, random_y, RIGHT, SPRITE_SIZE, self.screen)
        self.bullet_group.add(new_bullet)

    def launch_bullet(self):
        keys_pressed = pygame.key.get_pressed()

        self.bullet_cooldown_timer -= 1

        if self.bullet_cooldown_timer <= 0:
            if keys_pressed[pygame.K_SPACE]:
                bullet = Bullet(self.battle_player.x, self.battle_player.y, SPRITE_SIZE, self.player.direction, self.screen)
                self.bullet_group.add(bullet)
                self.bullet_cooldown_timer = BULLET_COOLDOWN_DELAY
                if self.player.direction == UP:
                    self.battle_player.y = self.player.y + 50
                if self.player.direction == DOWN:
                    self.battle_player.y = self.player.y - 300

                # bullet = Bullet(self.x, bullet_y, SPRITE_SIZE, self.player.direction,self.screen)
                # self.bullet_group.add(bullet)
                # self.bullet_cooldown_timer = BULLET_COOLDOWN_DELAY



    def create_player(self):
        random_y = r.randint(0, WIDTH)
        random_direction = r.choice([LEFT, RIGHT])

        x = 0
        y = 0

        if random_direction == LEFT:
            x = WIDTH

        new_player = Player(x, y, random_direction, SPRITE_SIZE, self.screen)
        self.player_group.add(new_player)

    def handle_player_enemy1_collision(self, player, enemy1):
        if player.rect.colliderect(enemy1.rect):
            self.background = pygame.image.load('assets/bg02.png')
            self.battle_player_group.add(self.battle_player)
            self.battle_enemy1_group.add(self.battle_enemy1)
            self.enemy2_group.empty()
            self.create_bullet()
            return True
        else:
            return False

    def handle_player_enemy2_collision(self, player, enemy2):
        if player.rect.colliderect(enemy2.rect):
            self.background = pygame.image.load('assets/bg03.png')
            self.battle_player_group.add(self.battle_player)
            self.battle_enemy2_group.add(self.battle_enemy2)
            self.enemy1_group.empty()
            self.create_bullet()
            print("collision correct")
            return True
        else:
            return False

    def game_loop(self):
        # -------- Main Program Loop -----------
        while self.running:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            self.screen.blit(self.background, (0, 0))

            # if self.mode == GAME_NOT_STARTED:
                # pass
            # else:
            if self.mode == GAME_STARTED:
                self.handle_game_in_session()

            # --- Limit to 60 frames per second
            self.clock.tick(FPS)
            current_fps = str(self.clock.get_fps())
            pygame.display.set_caption(f'{self.project_name}, fps: {current_fps}')

        # Close the window and quit.
        pygame.quit()

    def handle_game_in_session(self):
        pygame.sprite.groupcollide(self.player_group, self.enemy1_group, True, True, self.handle_player_enemy1_collision)
        pygame.sprite.groupcollide(self.player_group, self.enemy2_group, True, True, self.handle_player_enemy2_collision)

        self.player_group.update()
        self.enemy1_group.update()
        self.enemy2_group.update()

        self.battle_player_group.update()
        self.battle_enemy1_group.update()
        self.battle_enemy2_group.update()

        self.launch_bullet()
        self.bullet_group.update()

if __name__ == '__main__':
    puddles = Puddles()
    puddles.game_loop()
