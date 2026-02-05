import pygame
from sys import exit
from settings import TILE_SIZE,WIDTH,HEIGHT,FPS
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()


#Sprite class for Canvas
class Grid(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image.fill('White')

grid_surf = pygame.sprite.Group()



#Display Screen
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))

for i in range(WIDTH//TILE_SIZE):
    for j in range(HEIGHT//TILE_SIZE):
        x_pos_new = i*TILE_SIZE #Multiplied By the respective number of pixel
        y_pos_new = j*TILE_SIZE #i and j increases 
        new_tile = Grid(x_pos_new,y_pos_new)
        grid_surf.add(new_tile)



# -----   Game Loop  -------
while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            exit()
    screen.fill("Black")
    grid_surf.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
