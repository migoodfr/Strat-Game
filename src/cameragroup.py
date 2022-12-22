import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.camera_borders = {"top": 50, "left": 50, "right": 950,
                               "bottom": 950}  # TODO faire en sorte que ces valeurs scale een fonction des dimensions
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.background = pygame.image.load("../graphics/map.png").convert()

    def mouse_control(self):
        mouse = pygame.mouse.get_pos()
        if mouse[0] < self.camera_borders["left"] and mouse[1] < self.camera_borders["top"]:
            difference = pygame.math.Vector2(self.camera_borders["left"] - mouse[0],
                                             self.camera_borders["top"] - mouse[1])
            self.offset = self.offset + difference

        elif mouse[0] < self.camera_borders["left"] and mouse[1] > self.camera_borders["bottom"]:
            difference = pygame.math.Vector2(self.camera_borders["left"] - mouse[0],
                                             self.camera_borders["bottom"] - mouse[1])
            self.offset = self.offset + difference

        elif mouse[0] > self.camera_borders["right"] and mouse[1] > self.camera_borders["bottom"]:
            difference = pygame.math.Vector2(self.camera_borders["right"] - mouse[0],
                                             self.camera_borders["bottom"] - mouse[1])
            self.offset = self.offset + difference
        elif mouse[0] > self.camera_borders["right"] and mouse[1] < self.camera_borders["top"]:
            difference = pygame.math.Vector2(self.camera_borders["right"] - mouse[0],
                                             self.camera_borders["top"] - mouse[1])
            self.offset = self.offset + difference

        elif mouse[0] < self.camera_borders["left"]:
            difference = self.camera_borders["left"] - mouse[0]
            self.offset = self.offset + pygame.math.Vector2(difference, 0)

        elif mouse[0] > self.camera_borders["right"]:
            difference = self.camera_borders["right"] - mouse[0]
            self.offset = self.offset + pygame.math.Vector2(difference, 0)

        elif mouse[1] < self.camera_borders["top"]:
            difference = self.camera_borders["top"] - mouse[1]
            self.offset = self.offset + pygame.math.Vector2(0, difference)

        elif mouse[1] > self.camera_borders["bottom"]:
            difference = self.camera_borders["bottom"] - mouse[1]
            self.offset = self.offset + pygame.math.Vector2(0, difference)

    def custom_draw(self):
        self.mouse_control()
        self.screen.blit(self.background, self.offset)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)
