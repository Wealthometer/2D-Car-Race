import pygame
pygame.init()

w_width = 500 
w_height = 500
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Car race")

# game varibles
clock = pygame.time.Clock()

#drawing on the window surface
def DrawInGameLoop():
    clock.tick(60)
    window.fill("gray")
    pygame.display.flip()

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    DrawInGameLoop()

pygame.quit()
