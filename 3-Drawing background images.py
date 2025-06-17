import pygame
import time

pygame.init()

w_width = 500 
w_height = 500
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Car race")

# game varibles
clock = pygame.time.Clock()
font = pygame.font.SysFont("helvetica", 50, 1, 1)

#importing images
car_img = pygame.image.load("img/car1.png")
grass = pygame.image.load("img/grass.jpg")
yellow_line = pygame.image.load("img/yellow_line.jpg")
white_line = pygame.image.load("img/white_line.jpg")

class car():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 28
        self.height = 54
        self.vel = 4

    def draw(self, window):
        window.blit(car_img, (self.x, self.y))

def drawing_background():
    window.blit(grass, (0, 0))
    window.blit(grass, (420, 0))
    window.blit(white_line, (90, 0))
    window.blit(white_line, (405, 0))
    window.blit(yellow_line, (225, 0))
    window.blit(yellow_line, (225, 100))
    window.blit(yellow_line, (225, 200))
    window.blit(yellow_line, (225, 300))
    window.blit(yellow_line, (225, 400))

#drawing on window surface
def DrawInGameLoop():
    clock.tick(60)
    window.fill((136, 134, 134))
    drawing_background()
    maincar.draw(window)
    pygame.display.flip()

#creating objects
maincar = car(250, 250)

#adding crash condition
def crash():
    text = font.render("CAR CRASHED", 1, "black")
    window.blit(text, (95, 250))
    pygame.display.flip()
    time.sleep(2)
    maincar.x = 250
    maincar.y = 250
    game_loop()

run = True
def game_loop():
    global run
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if maincar.x < 100 or maincar.x > 400- maincar.width:     
            crash()

        #handling keyboard events 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and maincar.x > 95:
            maincar.x -= maincar.vel

        elif keys[pygame.K_RIGHT] and maincar.x < 405 - maincar.width:
            maincar.x += maincar.vel

        if keys[pygame.K_UP] and maincar.y > 0:
            maincar.y -= maincar.vel

        elif keys[pygame.K_DOWN] and maincar.y < w_width - maincar.height:
            maincar.y += maincar.vel

        DrawInGameLoop()

game_loop()
pygame.quit()
