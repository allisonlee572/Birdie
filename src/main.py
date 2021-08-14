import pygame

class ChangeMe():
    # Define some colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Set the width and height of the screen [width, height]
    WIDTH = 700
    HEIGHT = 500

    # FPS is Frame Per Second
    FPS = 40

    TARGET_WIDTH = 10

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.project_name = 'Puddles'

        pygame.display.set_caption(self.project_name)

        # Loop until the user clicks the close button.
        self.running = True

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()


    def game_loop(self):
        # -------- Main Program Loop -----------
        while self.running:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False



            pygame.display.flip()

            # --- Limit to 60 frames per second
            self.clock.tick(self.FPS)
            current_fps = str(self.clock.get_fps())
            pygame.display.set_caption(f'{self.project_name}, fps: {current_fps}')

        # Close the window and quit.
        pygame.quit()


if __name__ == '__main__':
    sb = ChangeMe()
    sb.game_loop()


