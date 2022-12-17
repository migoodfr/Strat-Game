from random import choice,randint

from PIL import Image

dimensions = (100, 100)
map = Image.new("RGBA", dimensions)

# 0 = ground
# 1 = océan

def get_randomdata_list(ground_density):
    """génère une liste de dimensions fournies avec des valeurs semi-aléatoires 
    (ground_density représente le pourcentage de 0 (ground) dans la liste) """
    list_data_tile = []
    for x in range(0, dimensions[0]):
        list_data_tile.append([])
        for y in range(0, dimensions[1]):
            nb_random = randint(1,100)
            if nb_random < ground_density:
                list_data_tile[x].append(0)
            else:
                list_data_tile[x].append(1)
    return list_data_tile

def automata_cellular_algorithm(liste_data,list_dimensions):
    """Pour chaque pixel, regarde tous les pixels alentours (carré de 3x3 pixels dont le centre est le pixel) :
     -  si il y a qautre 0 (ground) : change le pixel en 0 (ground)
     -  sinon change le pixel en océan (1)"""
    for x in range(1, list_dimensions[0]-1):
        for y in range(1, list_dimensions[1]-1):
            nb_ground = 0
            if liste_data[x][y] == 0:
                nb_ground += 1
            if liste_data[x][y+1] == 0:
                nb_ground += 1
            if liste_data[x][y-1] == 0:
                nb_ground += 1
            if liste_data[x-1][y+1] == 0:
                nb_ground += 1
            if liste_data[x-1][y] == 0:
                nb_ground += 1
            if liste_data[x-1][y-1] == 0:
                nb_ground += 1
            if liste_data[x+1][y+1] == 0:
                nb_ground += 1
            if liste_data[x+1][y] == 0:
                nb_ground += 1
            if liste_data[x+1][y-1] == 0:
                nb_ground += 1
            if nb_ground > 4 :
                liste_data[x][y] = 0
            else:
                liste_data[x][y] = 1
    return liste_data

def convert_list_to_image(list, list_dimensions):
    """transforme la liste en image"""
    for x in range(0, list_dimensions[0]):
        for y in range(0, list_dimensions[1]):
            if list[x][y] == 1:
                map.putpixel((x, y), (0, 0, 255))
            if list[x][y] == 0:
                map.putpixel((x, y), (0, 255, 0))

def create_map():
    list_tile = get_randomdata_list(45)
    list_tile = automata_cellular_algorithm(list_tile,dimensions)
    convert_list_to_image(list_tile,dimensions)

    map.show()