# from curses import init_pair
from email.errors import InvalidMultipartContentTransferEncodingDefect
from inspect import currentframe
from random import randint
import pygame
from pygame import font
from pygame import display
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_a, K_s, K_d, K_f
import time
from pygame.time import Clock
import random  # necessário para utilizar o módulo random
import math


random.seed(8)

pygame.init()

fps = 60
circle_radius = 200
play_time = 2
HEIGHT = 800
WIDTH = 600
Target_quantity = 10
circle_active = False

screen_res = HEIGHT, WIDTH
# fonte = font.SysFont('comicsans', 50)
# fonte_perdeu = font.SysFont('comicsans', 300)

view = display.set_mode(
    size=screen_res,
    display=0
)
display.set_caption(
    'Shrinking Circle'
)

  
class Remaining_time():
    def __init__(self, time_s):
        global remaining_time 
        super().__init__()
        remaining_time = time_s

    def update(self):
        global remaining_time 
        remaining_time -= 1/fps
        # print(remaining_time)

        if remaining_time <= 0:
            # self.kill()
            pygame.quit()
            exit()

class Shrinking_circle(Sprite):
    def __init__(self, radius):
        super().__init__()
        global current_radius
        global initial_radius
        if WIDTH>HEIGHT:
            current_radius = HEIGHT/2
        else:
            current_radius = WIDTH/2
        
        initial_radius = current_radius

        # self.image = load('images/inimigo_1.png')
        # self.rect = self.image.get_rect(
        #     center=(400, 300)
        # )

    def update(self):
        global current_radius
        global initial_radius

        if circle_active:
            current_radius -= initial_radius/(play_time*fps)
        #self.rect.x -= 0.1

        pygame.draw.circle(view, (255,255,255), 
            (400,300), current_radius, width=3) 
        #if self.rect.x == 0:
           # self.kill()
            #perdeu = True
    


# numeros = random.getstate()
#print(random.sample(range(10), k=5))

class Target():
    global initial_radius
    def __init__(self, quantity = Target_quantity, variations = 4):
        super().__init__()
        ball_coordinates = tuple()

        for i in range(Target_quantity):
            center_x = WIDTH/2
            center_y = HEIGHT/2
            while True:                
                x = random.randrange(0, WIDTH, 1)
                y = random.randrange(0, HEIGHT, 1)
                center_distance = math.sqrt(math.pow((x-center_x),2) + math.pow((y-center_y),2))
                if center_distance<initial_radius:
                    break
                
            ball_coordinates += list([x,y])

        print(ball_coordinates)




        # self.image = load('images/inimigo_1.png')
        # self.rect = self.image.get_rect(
        #     center=(400, 300)
        # )

#     def update(self):



main_circle = Shrinking_circle(circle_radius)
game_time = Remaining_time(play_time)
ball_target = Target()
clock = Clock()
frame = 0

while True:
    clock.tick(fps)

    #if frame == 0:


    #view.blit
    pygame.draw.rect(view, (0,0,0), (0,0,HEIGHT,WIDTH))
        # Espaço dos eventos
    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_a:
                print('A')
            if evento.key == K_s:
                print('S')
            if evento.key == K_d:
                print('D')
            if evento.key == K_f:
                print('F')
    
    frame +=1
    main_circle.update()
    game_time.update()
    display.update()