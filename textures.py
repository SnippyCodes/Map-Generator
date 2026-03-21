import pygame
from settings import TILE_SIZE

# Correct syntax: Load -> Convert -> Scale
grass_img = pygame.image.load("grass.png").convert()
grass_img = pygame.transform.scale(grass_img, (TILE_SIZE, TILE_SIZE))

water_img = pygame.image.load("water.png").convert()
water_img = pygame.transform.scale(water_img, (TILE_SIZE, TILE_SIZE))

sand_img = pygame.image.load("sand.png").convert()
sand_img = pygame.transform.scale(sand_img, (TILE_SIZE, TILE_SIZE))

snow_img = pygame.image.load("snow.png").convert()
snow_img = pygame.transform.scale(snow_img, (TILE_SIZE, TILE_SIZE))

# Use convert_alpha() for images with transparent backgrounds
forest_img = pygame.image.load("forest.png").convert_alpha()
forest_img = pygame.transform.scale(forest_img, (TILE_SIZE, TILE_SIZE))

savana_img = pygame.image.load("savana.png").convert_alpha()
savana_img = pygame.transform.scale(savana_img, (TILE_SIZE, TILE_SIZE))