import pygame
import random as rn
from sys import exit
from settings import TILE_SIZE,WIDTH,HEIGHT,FPS
from perlin_noise import PerlinNoise

pygame.init()
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()

#Display Screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
from textures import water_img,forest_img,sand_img,grass_img,snow_img,savana_img


#Sprite class for Canvas
class Grid(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft = (x,y))
        #To ignore the invisible corners made by isometric view 
        self.mask = self.image.get_rect(topleft = (x,y))

grid_surf = pygame.sprite.Group()

seed = rn.randint(1,1000000)
seed_moisture = rn.randint(1,1000000)
scale = 0.05 #For smoothness of image elevation and depression
noise_gen = PerlinNoise(octaves=3, seed=seed)
moisture_gen = PerlinNoise(octaves=3, seed=seed_moisture) 
rows = (WIDTH//TILE_SIZE)*3
cols = (HEIGHT//TILE_SIZE)*3
offset_x = 0
offset_y = 0
scroll_speed = 1.5
update = False #TO update map only when user presses "WASD" key
forest_colour = (34,139,34)
savana_colour = (210,210,100)

def isometric(x,y):
    x_iso = x-y
    y_iso = (x+y)//2
    return x_iso,y_iso

def map_gen(offset_x,offset_y):
    grid_surf.empty()
    shift_x = WIDTH //2
    shift_y = -(HEIGHT // 2)
    for i in range(rows):
        for j in range(cols):
            x = ((i*scale)+offset_x)
            y = ((j*scale)+offset_y)
            noise_val = noise_gen([x, y])
            moist_val = moisture_gen([x, y])

            cart_x = (i * (TILE_SIZE //2)) + offset_x
            cart_y = (j * (TILE_SIZE // 2)) + offset_y

            iso_x, iso_y = isometric(cart_x, cart_y)
            iso_x += shift_x
            iso_y += shift_y


            if noise_val >0:
                iso_y -= int(noise_val*50)
            if noise_val < -0.1:
                tile_colour = water_img
            elif noise_val < 0.1:
                tile_colour = sand_img
            elif noise_val < 0.7:
                if moist_val >0.5:
                    tile_colour = forest_img
                elif moist_val < -0.5:
                    tile_colour = savana_img
                else:
                    tile_colour = grass_img
            else:
                tile_colour = snow_img 
            new_tile = Grid(iso_x,iso_y,tile_colour)
            grid_surf.add(new_tile)

map_gen(offset_x,offset_y)

#Game Loop  
while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
    key =  pygame.key.get_pressed()   

            
    if(key[pygame.K_w]):
        offset_y -= scroll_speed * 0.1
        update = True    
    if(key[pygame.K_s]):
        offset_y += scroll_speed * 0.1
        update = True
    if(key[pygame.K_a]):
        offset_x -= scroll_speed * 0.1
        update = True
    if(key[pygame.K_d]):
        offset_x += scroll_speed *0.1
        update = True
    if(update):
        map_gen(offset_x,offset_y)
        update = False
    screen.fill("LightBlue")
    grid_surf.draw(screen)
    mouse_x_pos, mouse_y_pos = pygame.mouse.get_pos()
    pygame.display.update()
    clock.tick(FPS)
