# Ce fichier contient la class mère de tous les batiments plaçables sur la carte

###########
# Imports #
###########

import pygame

class Batiment(pygame.sprite.Sprite):
    def __init__(self):
        """class mère des différents (à utiliser pour créer autres batiments),
         arguments :    -
                        -
                        -
                        -  """
        super().__init__() # initilaisation de la class mère (Sprite de pygame)

        #