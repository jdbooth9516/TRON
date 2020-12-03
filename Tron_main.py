import pygame
import os  
from Variables import FPS, WIN, TEXT_BOX, TEXT_INDEX
pygame.font.init()

def main():
    run = True 
    #level = 0 
    #system_font = pygame.font.SysFont("need", 50)
    text_font = pygame.font.SysFont("Terminal", 30)

    clock = pygame.time.Clock()


    while run: 
        clock.tick(FPS)
        # this group will need to be moved to a draw window function 
        WIN  #full game window 
        TEXT_BOX #makes the text box 
        text_font.render("test", 1,(255,255,255)) # these two line are fromatted for the text
        WIN.blit(text_font.render("test", 1,(255,255,255)),(TEXT_INDEX, TEXT_INDEX))

        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
    
main()
