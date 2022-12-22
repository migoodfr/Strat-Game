import pygame
import random

from cameragroup import CameraGroup

# Constantes
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
COLOR_BACKGROUND = (127, 127, 127)

# Map constantes
TILE_SIZE = 10
ROWS = 10
COLS = 10


def update(screen, camera_group):
    """
	Actualise chaque élèments du jeu 
	"""

    screen.fill(COLOR_BACKGROUND)
    camera_group.update()
    camera_group.custom_draw()

    pygame.display.update()


def start_game():
    """
	Fonction principal du jeu
	"""

    # Setup pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("yorg.io")
    clock = pygame.time.Clock()
    # pygame.event.set_grab(True)

    camera_group = CameraGroup()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        update(screen, camera_group)

        clock.tick(60)


if __name__ == '__main__':
    start_game()
    pygame.quit()
