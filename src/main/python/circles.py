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
play_time = 10
HEIGHT = 800
WIDTH = 600
border_width = 100 # The width of the "orbits" in which the circles will be drawn
center_x = 400
center_y = 300
A_color = (255, 0, 0)
S_color = (0, 255, 0)
D_color = (0, 0, 255)
F_color = (255, 255, 0)
Target_quantity = 15
circle_active = True

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
        global ball_coordinates
        ball_coordinates = tuple()

        for i in range(Target_quantity):

            while True:                
                x = random.randrange(0, WIDTH, 1)
                y = random.randrange(0, HEIGHT, 1)
                center_distance = math.sqrt(math.pow((x-center_x),2) + math.pow((y-center_y),2))
                if center_distance<initial_radius & i == 0:
                    break
                if center_distance<initial_radius & i >0:
                    if center_distance>ball_coordinates[i-1][2]+border_width | center_distance<ball_coordinates[i-1][2]-border_width:
                        break
            type = random.sample(set('ASDF'), 1)
            ball_coordinates += tuple([(x,y,center_distance,type)])
        
        



        # print(ball_coordinates)
        #for x,y,c,t in ball_coordinates: print(x,y,c,t)




        # self.image = load('images/inimigo_1.png')
        # self.rect = self.image.get_rect(
        #     center=(400, 300)
        # )

    def update(self):
        for x,y, c, t in ball_coordinates:
            color = A_color
            match t:
                case ['A']:
                    color = A_color
                case ['S']:
                    color = S_color
                case ['D']:
                    color = D_color
                case ['F']:
                    color = F_color
            if c<current_radius:
                pygame.draw.circle(view, color, 
                    (x,y), 10, width=2)                
            else:
                pygame.draw.circle(view, (255,255,255), 
                    (x,y), 5, width=5)



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
    ball_target.update()
    display.update()