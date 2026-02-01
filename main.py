#To activate a virtual environment in Python, you typically use the following command in your terminal or command prompt:
# On Windows: .\venv\Scripts\Activate.ps1
import pygame
from sys import exit
#Starts and initiates pygame
pygame.init()
x = pygame.display .set_mode((1200, 600)) 
pygame.display.set_caption("Map Generator")
clock = pygame.time.Clock()
tp_sur = pygame.Surface((50, 50))
player = pygame.image.load('ima.png').convert_alpha()
player_rect = player.get_rect(bottomright = (600,300))



player_resize = pygame.transform.scale(player,(300,200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if(player_rect.right<1300):
        player_rect.x+= 4
    else:
        player_rect.left=0
    x.blit(player_resize, player_rect)
    pygame.display.update()
    clock.tick(60)