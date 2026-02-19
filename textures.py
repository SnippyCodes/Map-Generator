import pygame
from settings import TILE_SIZE
sand_colour = (194, 178, 128)
forest_colour = (34, 139, 34)
savana_colour = (210, 210, 100)


grass_img = pygame.transform.scale(pygame.image.load("grass.png"),(TILE_SIZE,TILE_SIZE))
water_img = pygame.transform.scale(pygame.image.load("water.png"),(TILE_SIZE,TILE_SIZE))
sand_img  = pygame.transform.scale(pygame.image.load("sand.png"),(TILE_SIZE,TILE_SIZE))
snow_img  = pygame.transform.scale(pygame.image.load("snow.png"),(TILE_SIZE,TILE_SIZE))
forest_img = pygame.transform.scale(pygame.image.load("forest.png"),(TILE_SIZE,TILE_SIZE))
savana_img = pygame.transform.scale(pygame.image.load("savana.png"),(TILE_SIZE,TILE_SIZE))