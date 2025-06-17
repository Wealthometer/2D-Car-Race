import pygame
import time
import random

pygame.init()

w_width = 500 
w_height = 500
window = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Car race")

# game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont("helvetica", 50, 1, 1)

# importing images
car_img = pygame.image.load("img/car1.png")
grass = pygame.image.load("img/grass.jpg")
yellow_line = pygame.image.load("img/yellow_line.jpg")
white_line = pygame.image.load("img/white_line.jpg")
enemy_car_imgs = [pygame.image.load("img/car2.png"),pygame.image.load("img/car3.png")]

# define the car class
class Car():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = 28
        self.height = 54
        self.vel = 2
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

# define the enemy car class
class EnemyCar(Car):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.width = 28
        self.height = 69
        self.vel = 2

    def move(self):
        self.y += self.vel

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

# create a list of enemy cars
enemy_cars = []

# create enemy cars and add them to the list
for i in range(3):
    x = random.randint(100, 400 - 28)
    y = random.randint(-500, -50)
    img = random.choice(enemy_car_imgs)
    enemy_car = EnemyCar(x, y, img)
    enemy_cars.append(enemy_car)

# drawing the background
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

# drawing on window surface
def DrawInGameLoop():
    clock.tick(60)
    window.fill((136, 134, 134))
    drawing_background()
    maincar.draw(window)

    # draw all enemy cars
    for enemy_car in enemy_cars:
        enemy_car.draw(window)

    pygame.display.flip()

# creating objects
maincar = Car(250, 250, car_img)

# adding crash condition
def crash():
    text = font.render("CAR CRASHED", 1, "black")
    window.blit(text, (95, 250))
    pygame.display.flip()
    time.sleep(2)

    # reset the position of the main car
    maincar.x = 250
    maincar.y = 250

    # reset the position and speed of all enemy cars
    for enemy_car in enemy_cars:
        enemy_car.x = random.randint(100, 400 - 28)
        enemy_car.y = random.randint(-500, -50)
        enemy_car.img = random.choice(enemy_car_imgs)
        enemy_car.vel = 2

    game_loop()


run = True
def game_loop():
    global run
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if maincar.x < 100 or maincar.x > 400 - maincar.width:     
            crash()

        # handling keyboard events 
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and maincar.x > 95:
            maincar.x -= maincar.vel

        elif keys[pygame.K_RIGHT] and maincar.x < 405 - maincar.width:
            maincar.x += maincar.vel

        if keys[pygame.K_UP] and maincar.y > 0:
            maincar.y -= maincar.vel

        elif keys[pygame.K_DOWN] and maincar.y < w_width - maincar.height:
            maincar.y += maincar.vel

        # move all enemy cars
        for enemy_car in enemy_cars:
            enemy_car.move()

            # check for collision with main car
            if (enemy_car.x < maincar.x + maincar.width and
                enemy_car.x + enemy_car.width > maincar.x and
                enemy_car.y < maincar.y + maincar.height and
                enemy_car.y + enemy_car.height > maincar.y):
                crash()

            # if enemy car goes off the screen, reset its position
            if enemy_car.y > w_height:
                enemy_car.x = random.randint(100, 400 - 28)
                enemy_car.y = random.randint(-500, -50)
                enemy_car.img = random.choice(enemy_car_imgs)
                enemy_car.vel = 2

        DrawInGameLoop()

game_loop()
pygame.quit()
