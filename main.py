import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # This creates an 1000x900 window
pygame.display.set_caption("Dracula's Chess!")  # This sets the title of the window
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)  #to print different things you need different fonts
timer = pygame.time.Clock()
fps = 60


#  game variables and images

run = True
while run:
    timer.tick(fps)
    screen.fill('dark grey')
    

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()        
pygame.quit()    
