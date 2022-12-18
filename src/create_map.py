from random import choice,randint
import pygame

from PIL import Image


class Map:
    """

    """

    def __init__(self, size_tile: int, rows: int, cols: int, color: tuple):
        self.size_tile = size_tile
        self.rows = rows
        self.cols = cols
        self.color = color

    def draw(self, screen):
        """
        Dessine le cadrillage il faudra remplacer par les photos des deux differents carreaux
        """

        for row in range(self.rows):
            for col in range(self.cols):
                if (col + row) % 2 == 1:
                    pygame.draw.rect(screen, self.color, pygame.Rect(col * self.size_tile, row * self.size_tile, self.size_tile, self.size_tile))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(col * self.size_tile, row * self.size_tile, self.size_tile, self.size_tile))


