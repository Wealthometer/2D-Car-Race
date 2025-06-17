import pygame
pygame.init()

w_width = 500 
w_height = 500
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Car race")

# game varibles
clock = pygame.time.Clock()

#importing images
car_img = pygame.image.load("img/car1.png")

class car():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 28
        self.height = 54
        self.vel = 4

    def draw(self, window):
        window.blit(car_img, (self.x, self.y))

#drawing on the window surface
def DrawInGameLoop():
    clock.tick(60)
    window.fill((136, 134, 134))
    maincar.draw(window)
    pygame.display.flip()

#creating objects
maincar = car(250, 250)

#game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #handling keyboard events 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and maincar.x > 0:
        maincar.x -= maincar.vel

    elif keys[pygame.K_RIGHT] and maincar.x < w_width - maincar.width:
        maincar.x += maincar.vel

    if keys[pygame.K_UP] and maincar.y > 0:
        maincar.y -= maincar.vel

    elif keys[pygame.K_DOWN] and maincar.y < w_width - maincar.height:
        maincar.y += maincar.vel

    DrawInGameLoop()

pygame.quit()
