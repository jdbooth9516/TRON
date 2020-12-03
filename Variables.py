import pygame 
WIDTH, HEIGHT = 600, 700 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Aftermath")

TEXT_BOX = pygame.draw.rect(WIN, (0,0,200), [0,450,600,250], 10, border_radius= 5)
TEXT_INDEX = (15, 465)
FPS = 60 


