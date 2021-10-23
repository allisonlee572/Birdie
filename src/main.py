import pygame
from pygame.sprite import Group
import random as r
from player import Player
from health_border import HealthBorder
from enemy1 import Enemy1
from enemy2 import Enemy2
from enemy3 import Enemy3
from battle_player import BattlePlayer
from battle_enemy1 import BattleEnemy1
from battle_enemy2 import BattleEnemy2
from battle_enemy3 import BattleEnemy3
from bullet import Bullet
from bullet1 import Bullet1
from bullet2 import Bullet2
from bullet3 import Bullet3
from config import *


class Puddles:

    def __init__(self):
        pygame.init()

        self.mode = GAME_STARTED
        # self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # self.direction_x = BattleEnemy3.right_direction_x
        self.project_name = 'Puddles'

        pygame.display.set_caption(self.project_name)

        # Loop until the user clicks the close button.
        self.running = True

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        self.background = pygame.image.load('assets/bg01.png')

        # self.health_border = Group()
        # self.health_border = HealthBorder(0, 0, SPRITE_SIZE, self.screen)

        self.health_border_group = Group()
        self.health_border = HealthBorder(15, 20, SPRITE_SIZE, self.screen)

        self.player_group = Group()
        self.player = Player(30, 305, RIGHT, SPRITE_SIZE, self.screen)

        self.enemy1_group = Group()
        self.enemy1 = Enemy1(270, 330, RIGHT, SPRITE_SIZE, self.screen)

        self.enemy2_group = Group()
        self.enemy2 = Enemy2(570, 330, RIGHT, SPRITE_SIZE, self.screen)

        self.enemy3_group = Group()
        self.enemy3 = Enemy3(870, 330, RIGHT, SPRITE_SIZE, self.screen)

        self.battle_player_group = Group()
        self.battle_player = BattlePlayer((WIDTH/2) - (SPRITE_SIZE/2), 330, RIGHT, SPRITE_SIZE, self.screen)

        self.battle_enemy1_group = Group()
        self.battle_enemy1 = BattleEnemy1((WIDTH/2) - (SPRITE_SIZE/2), 0, RIGHT, SPRITE_SIZE, self.screen)

        self.battle_enemy2_group = Group()
        self.battle_enemy2 = BattleEnemy2((WIDTH/2) - (SPRITE_SIZE/2), 0, RIGHT, SPRITE_SIZE, self.screen)

        self.battle_enemy3_group = Group()
        self.battle_enemy3 = BattleEnemy3(100, 0, SPRITE_SIZE, self.screen)
        #self.battle_enemy3 = BattleEnemy3(100, 0, RIGHT, self.right_direction_x, SPRITE_SIZE, self.screen)

        self.bullet_group = Group()
        self.bullet_cooldown_timer = BULLET_COOLDOWN_DELAY

        self.bullet1_group = Group()
        self.bullet1_cooldown_timer = BULLET_1_COOLDOWN_DELAY

        self.bullet2_group = Group()
        self.bullet2_cooldown_timer = BULLET_2_COOLDOWN_DELAY

        self.bullet3_group = Group()
        self.bullet3_cooldown_timer = BULLET_3_COOLDOWN_DELAY

        self.font = pygame.font.SysFont("default", 30)

    '''
    def create_bullet(self):
        random_y = r.randint(0, HEIGHT)
        new_bullet = Bullet(0, random_y, RIGHT, SPRITE_SIZE, self.screen)
        self.bullet_group.add(new_bullet)
    '''
    def auto_launch_bullet1(self):
        self.bullet1_cooldown_timer -= 1
        if self.bullet1_cooldown_timer == 0:
            self.bullet1_cooldown_timer = BULLET_1_COOLDOWN_DELAY
            # random_y = r.randint(0, WIDTH)
            # random_direction = r.choice([LEFT, RIGHT])
            # if random_direction == LEFT:
                # x = WIDTH

            self.battle_enemy1_bullet_x = self.battle_enemy1.x + (SPRITE_SIZE / 2)
            # move the above code (in squiggly lines) to the innit method?

            new_bullet1 = Bullet1(self.battle_enemy1_bullet_x, self.battle_enemy1.y,
                                        SPRITE_SIZE, self.enemy1.direction, self.screen)
            self.bullet1_group.add(new_bullet1)

    def auto_launch_bullet2(self):
        self.bullet2_cooldown_timer -= 1
        if self.bullet2_cooldown_timer == 0:
            self.bullet2_cooldown_timer = BULLET_2_COOLDOWN_DELAY
            self.battle_enemy2_bullet_x = self.battle_enemy2.x + (SPRITE_SIZE / 2)
            # move the above code (in squiggly lines) to the innit method?

            new_bullet2 = Bullet2(self.battle_enemy2_bullet_x, self.battle_enemy2.y,
                                    SPRITE_SIZE, self.enemy1.direction, self.screen)
            self.bullet2_group.add(new_bullet2)

    def auto_launch_bullet3(self):
        self.bullet3_cooldown_timer -= 1
        if self.bullet3_cooldown_timer == 0:
            self.bullet3_cooldown_timer = BULLET_3_COOLDOWN_DELAY
            self.battle_enemy2_bullet_x = self.battle_enemy2.x + (SPRITE_SIZE / 2)
            # move the above code (in squiggly lines) to the innit method?

            new_bullet3 = Bullet3(self.battle_enemy2_bullet_x, self.battle_enemy2.y,
                                    SPRITE_SIZE, self.enemy2.direction, self.screen)
            self.bullet3_group.add(new_bullet3)

            # note: this one says battle_enemy2 because it is used for battle_enemy2

    def auto_launch_bullet1_v2(self):
        self.bullet1_cooldown_timer -= 1
        if self.bullet1_cooldown_timer == 0:
            self.bullet1_cooldown_timer = BULLET_1_COOLDOWN_DELAY
            # random_y = r.randint(0, WIDTH)
            # random_direction = r.choice([LEFT, RIGHT])
            # if random_direction == LEFT:
            # x = WIDTH

            self.battle_enemy3_bullet_x = self.battle_enemy3.x + (SPRITE_SIZE / 2)
            # move the above code (in squiggly lines) to the innit method?

            new_bullet1 = Bullet1(self.battle_enemy3_bullet_x, self.battle_enemy3.y,
                                  SPRITE_SIZE, self.enemy3.direction, self.screen)
            self.bullet1_group.add(new_bullet1)

    def auto_launch_bullet2_v2(self):
        self.bullet2_cooldown_timer -= 1
        if self.bullet2_cooldown_timer == 0:
            self.bullet2_cooldown_timer = BULLET_2_COOLDOWN_DELAY
            self.battle_enemy3_bullet_x = self.battle_enemy3.x + (SPRITE_SIZE / 2)
            # move the above code (in squiggly lines) to the innit method?

            new_bullet2 = Bullet2(self.battle_enemy3_bullet_x, self.battle_enemy3.y,
                                  SPRITE_SIZE, self.enemy3.direction, self.screen)
            self.bullet2_group.add(new_bullet2)

    def auto_launch_bullet3_v2(self):
        self.bullet3_cooldown_timer -= 1
        if self.bullet3_cooldown_timer == 0:
            self.bullet3_cooldown_timer = BULLET_3_COOLDOWN_DELAY
            self.battle_enemy3_bullet_x = self.battle_enemy3.x + (SPRITE_SIZE / 2)
            # move the above code (in squiggly lines) to the innit method?

            new_bullet3 = Bullet3(self.battle_enemy3_bullet_x, self.battle_enemy3.y,
                                  SPRITE_SIZE, self.enemy3.direction, self.screen)
            self.bullet3_group.add(new_bullet3)

    def launch_bullet(self):
        keys_pressed = pygame.key.get_pressed()

        self.bullet_cooldown_timer -= 1
        self.battle_player_bullet_x = self.battle_player.x + (SPRITE_SIZE / 2)
        # move the above code (in squiggly lines) to the innit method?

        if self.bullet_cooldown_timer <= 0:
            if keys_pressed[pygame.K_SPACE]:
                bullet = Bullet(self.battle_player_bullet_x, self.battle_player.y, SPRITE_SIZE, self.player.direction, self.screen)
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
            # self.player_group.empty() # this code wasn't added earlier
            self.enemy2_group.empty()
            self.mode = BATTLE_1
            return True
        else:
            return False

    def handle_player_enemy2_collision(self, player, enemy2):
        if player.rect.colliderect(enemy2.rect):
            self.background = pygame.image.load('assets/bg03.png')
            self.battle_player_group.add(self.battle_player)
            self.battle_enemy2_group.add(self.battle_enemy2)
            # self.player_group.empty() # this code wasn't added earlier
            self.enemy1_group.empty()
            self.mode = BATTLE_2
            return True
        else:
            return False

    def handle_player_enemy3_collision(self, player, enemy3):
        if player.rect.colliderect(enemy3.rect):
            self.background = pygame.image.load('assets/bg04.png')
            self.battle_player_group.add(self.battle_player)
            self.battle_enemy3_group.add(self.battle_enemy3)
            # self.player_group.empty() # this code wasn't added earlier
            self.enemy1_group.empty()
            self.enemy2_group.empty()
            self.mode = BATTLE_3
            print("collision correct")
            return True
        else:
            return False

    def handle_bullet_enemy1_collision(self, bullet, enemy1):
        if bullet.rect.colliderect(enemy1.rect):
            # nothing happens lol, maybe can add a noise or something
            self.battle_enemy1.health -= 1
            if self.battle_enemy1.health == 0:
                self.player.set_position(420, 305)
                self.battle_player_group.empty()
                self.battle_enemy1_group.empty()
                self.mode = GAME_STARTED
            return True
        else:
            return False

    def handle_bullet_enemy2_collision(self, bullet, enemy2):
        if bullet.rect.colliderect(enemy2.rect):
            # nothing happens lol, maybe can add a noise or something
            self.battle_enemy2.health -= 1
            if self.battle_enemy2.health == 0:
                self.player.set_position(720, 305)
                self.battle_player_group.empty()
                self.battle_enemy2_group.empty()
                self.mode = GAME_STARTED
            return True
        else:
            return False

    def handle_bullet_enemy3_collision(self, bullet, enemy3):
        if bullet.rect.colliderect(enemy3.rect):
            # nothing happens lol, maybe can add a noise or something
            self.battle_enemy3.health -= 1
            if self.battle_enemy3.health == 0:
                self.player.set_position(20, 305)
                self.battle_player_group.empty()
                self.battle_enemy3_group.empty()
                self.mode = GAME_STARTED
                # change the player.set_position because it's the end of the game
            return True
        else:
            return False

    def handle_bullet1_battle_player_collision(self, player, bullet1):
        if player.rect.colliderect(bullet1.rect):
            # reference point #1
            self.player.set_position(30, 305)

            self.battle_player_group.empty()
            self.battle_enemy1_group.empty()
            self.battle_enemy2_group.empty()
            self.battle_enemy3_group.empty()

            self.mode = GAME_STARTED
            return True
        else:
            return False

    def handle_bullet2_battle_player_collision(self, player, bullet2):
        if player.rect.colliderect(bullet2.rect):
            # reference point #2
            self.player.set_position(420, 305)

            self.battle_player_group.empty()
            self.battle_enemy1_group.empty()
            self.battle_enemy2_group.empty()
            self.battle_enemy3_group.empty()

            self.mode = GAME_STARTED
            print("collision works")
            return True
        else:
            return False

    def handle_bullet3_battle_player_collision(self, player, bullet3):
        if player.rect.colliderect(bullet3.rect):
            # reference point 3
            self.player.set_position(720, 305)

            self.battle_player_group.empty()
            self.battle_enemy1_group.empty()
            self.battle_enemy2_group.empty()
            self.battle_enemy3_group.empty()

            self.mode = GAME_STARTED
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
                self.handle_game_started()
            if self.mode == BATTLE_1:
                self.handle_battle_1_in_session()
            if self.mode == BATTLE_2:
                self.handle_battle_2_in_session()
            if self.mode == BATTLE_3:
                self.handle_battle_3_in_session()

            # --- Limit to 60 frames per second
            self.clock.tick(FPS)
            current_fps = str(self.clock.get_fps())
            pygame.display.set_caption(f'{self.project_name}, fps: {current_fps}')

        # Close the window and quit.
        pygame.quit()

    def handle_game_started(self):
        self.background = pygame.image.load('assets/bg01.png')

        self.player_group.add(self.player)
        self.enemy1_group.add(self.enemy1)
        self.enemy2_group.add(self.enemy2)
        self.enemy3_group.add(self.enemy3)
        self.health_border_group.add(self.health_border)

        pygame.sprite.groupcollide(self.player_group, self.enemy1_group, True, True, self.handle_player_enemy1_collision)
        pygame.sprite.groupcollide(self.player_group, self.enemy2_group, True, True, self.handle_player_enemy2_collision)
        pygame.sprite.groupcollide(self.player_group, self.enemy3_group, True, True, self.handle_player_enemy3_collision)

        self.player_group.update()
        self.enemy1_group.update()
        self.enemy2_group.update()
        self.enemy3_group.update()

        self.battle_player_group.update()
        self.battle_enemy1_group.update()
        self.battle_enemy2_group.update()
        self.battle_enemy3_group.update()

        self.battle_player.reset_battle_player((WIDTH/2) - (SPRITE_SIZE/2), 330)
        self.battle_enemy1.reset_battle_enemy_1((WIDTH/2) - (SPRITE_SIZE/2), 0)
        self.battle_enemy2.reset_battle_enemy_2((WIDTH/2) - (SPRITE_SIZE/2), 0)
        self.battle_enemy3.reset_battle_enemy_3((WIDTH/2) - (SPRITE_SIZE/2), 0)

    """
    def handle_between_battles(self):
        self.player_group.add(self.player)
        #self.enemy1_group.add(self.enemy1)
        #self.enemy2_group.add(self.enemy2)
        #self.enemy3_group.add(self.enemy3)

        pygame.sprite.groupcollide(self.player_group, self.enemy1_group, True, True, self.handle_player_enemy1_collision)
        pygame.sprite.groupcollide(self.player_group, self.enemy2_group, True, True, self.handle_player_enemy2_collision)
        pygame.sprite.groupcollide(self.player_group, self.enemy3_group, True, True, self.handle_player_enemy3_collision)

        self.player_group.update()
        self.enemy1_group.update()
        self.enemy2_group.update()
        self.enemy3_group.update()

        self.battle_player_group.update()
        self.battle_enemy1_group.update()
        self.battle_enemy2_group.update()
        self.battle_enemy3_group.update()
        """


    def handle_battle_1_in_session(self):
        self.battle_enemy2_group.empty()
        self.battle_enemy3_group.empty()

        self.health_border_group.update()

        self.battle_player_group.update()
        self.battle_enemy1_group.update()

        self.launch_bullet()
        self.bullet_group.update()

        self.auto_launch_bullet1()
        self.bullet1_group.update()

        self.draw_enemy1_health_indicator()

        pygame.sprite.groupcollide(self.battle_enemy1_group, self.bullet_group, False, True,
                                   self.handle_bullet_enemy1_collision)
        pygame.sprite.groupcollide(self.bullet1_group, self.battle_player_group, True, False,
                                   self.handle_bullet1_battle_player_collision)

    def handle_battle_2_in_session(self):
        self.battle_enemy1_group.empty()
        self.battle_enemy3_group.empty()

        self.health_border_group.update()

        self.battle_player_group.update()
        self.battle_enemy2_group.update()

        self.launch_bullet()
        self.bullet_group.update()

        self.auto_launch_bullet1()
        self.bullet1_group.update()

        self.auto_launch_bullet2()
        self.bullet2_group.update()

        self.auto_launch_bullet3()
        self.bullet3_group.update()

        self.draw_enemy2_health_indicator()

        pygame.sprite.groupcollide(self.battle_enemy2_group, self.bullet_group, False, True,
                                   self.handle_bullet_enemy2_collision)
        pygame.sprite.groupcollide(self.bullet1_group, self.battle_player_group, True, False,
                                   self.handle_bullet1_battle_player_collision)
        pygame.sprite.groupcollide(self.bullet2_group, self.battle_player_group, True, False,
                                   self.handle_bullet2_battle_player_collision)
        pygame.sprite.groupcollide(self.bullet3_group, self.battle_player_group, True, False,
                                   self.handle_bullet3_battle_player_collision)

    def handle_battle_3_in_session(self):
        self.battle_enemy1_group.empty()
        self.battle_enemy2_group.empty()

        self.health_border_group.update()

        self.battle_player_group.update()
        self.battle_enemy3_group.update()

        self.launch_bullet()
        self.bullet_group.update()

        self.auto_launch_bullet1_v2()
        self.bullet1_group.update()

        self.auto_launch_bullet2_v2()
        self.bullet2_group.update()

        self.auto_launch_bullet3_v2()
        self.bullet3_group.update()

        self.draw_enemy3_health_indicator()

        pygame.sprite.groupcollide(self.battle_enemy3_group, self.bullet_group, False, True,
                                   self.handle_bullet_enemy3_collision)
        pygame.sprite.groupcollide(self.bullet1_group, self.battle_player_group, True, False,
                                   self.handle_bullet1_battle_player_collision)
        pygame.sprite.groupcollide(self.bullet2_group, self.battle_player_group, True, False,
                                   self.handle_bullet2_battle_player_collision)
        pygame.sprite.groupcollide(self.bullet3_group, self.battle_player_group, True, False,
                                   self.handle_bullet3_battle_player_collision)

    def draw_enemy1_health_indicator(self):
        health_text = f"Enemy Lives Remaining: {self.battle_enemy1.health}"
        health_msg = self.font.render(health_text, 1, BLACK)
        self.screen.blit(health_msg, (45, 50))

    def draw_enemy2_health_indicator(self):
        health_text = f"Enemy Lives Remaining: {self.battle_enemy2.health}"
        health_msg = self.font.render(health_text, 1, BLACK)
        self.screen.blit(health_msg, (45, 50))

    def draw_enemy3_health_indicator(self):
        health_text = f"Enemy Lives Remaining: {self.battle_enemy3.health}"
        health_msg = self.font.render(health_text, 1, BLACK)
        self.screen.blit(health_msg, (45, 50))


if __name__ == '__main__':
    puddles = Puddles()
    puddles.game_loop()

# rename project?
# if want to add three hearts for the enemies lives = create one sprite for heart
# use a for loop (for i in range(1,3)?
# and want to space out the hearts by multipying a constant or something?

# reset battle enemies when battle is lost?
# when enemy health is equal to 0, move the player to a different spot

# reset bullets after each battle is won/lost
# change the player's position after the third battle is won because the game is closed to finished
# fix player position depending on which bullets touch the player
# change health indicators to something more readable for battle enemy 2 and 3
# add box for where the health indicators will be?
# set battle_player to the middle spot (same spot) whenever battles are entered

# After most codes are finished:
# change enemy health back to higher numbers
# make the player be able to move only left and right after most of the codes are done

