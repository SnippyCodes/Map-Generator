import pygame
from sys import exit
from settings import TILE_SIZE,WIDTH,HEIGHT,FPS
from noise import pnoise2 #For 2D image 
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
sand_colour  = (194, 178, 128) #RGB for Skin Colour

#Sprite class for Canvas
class Grid(pygame.sprite.Sprite):
    def __init__(self,x,y,colour):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image.fill(colour)

grid_surf = pygame.sprite.Group()



#Display Screen
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))


seed = 42 
seed_moisture = 30
scale = 0.1 #For smoothness of image elevation and depression 
rows = WIDTH//TILE_SIZE
cols = HEIGHT//TILE_SIZE
offset_x = 0
offset_y = 0
scroll_speed = 1.5
update = False #TO update map only when user presses "WASD" key
forest_colour = (34,139,34)
savana_colour = (210,210,100)

def map_gen(offset_x,offset_y):
    grid_surf.empty()
    for i in range(rows):
        for j in range(cols):
            noise_val = pnoise2((i*scale)+offset_x,(j*scale)+offset_y,base = seed,octaves = 5,persistence = 0.4,lacunarity = 1.5)
            x_pos_new = i*TILE_SIZE #Multiplied By the respective number of pixel
            y_pos_new = j*TILE_SIZE #i and j increases        
            moist_val = pnoise2((i*scale)+ offset_x, (j*scale)+offset_y,base = seed_moisture,octaves = 5)
            if noise_val<-0.1:
                tile_colour = "Blue"
            elif noise_val<0.1:
                if(moist_val>0.5):
                    tile_colour = forest_colour
                elif moist_val<-0.5:
                    tile_colour = savana_colour
                else:
                    tile_colour = "Green"
            else:
                tile_colour = 'White'
            new_tile = Grid(x_pos_new,y_pos_new,tile_colour)
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
    screen.fill("Black")
    grid_surf.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
