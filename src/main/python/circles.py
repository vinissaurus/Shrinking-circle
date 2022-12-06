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
initial_radius = 180
circle_radius = 180
play_time = 20
HEIGHT = 900
WIDTH = 900
CENTER = (450,450)
A_color = (255, 0, 0)
S_color = (0, 255, 0)
D_color = (0, 0, 255)
F_color = (255, 255, 0)
Target_quantity = 20
circle_active = True
key_tolerance = 100
score = 0

screen_res = HEIGHT, WIDTH

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
        global scoredsaf
        remaining_time -= 1/fps
        # print(remaining_time)

        if remaining_time <= 0:
            # self.kill()
            print('Game Over: {}'.format(score))
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
        global remaining_time
        global current_radius
        global initial_radius
        global ball_coordinates
        global orbit_space

        color = (255,255,255)
        if circle_active:
            current_radius -= initial_radius/(play_time*fps)

        for center, _, type, _, _ in ball_coordinates:
            if current_radius<center+orbit_space:
                match type:
                    case ['A']:
                        color = A_color
                    case ['S']:
                        color = S_color
                    case ['D']:
                        color = D_color
                    case ['F']:
                        color = F_color
                break


        pygame.draw.circle(view, color, 
            CENTER, current_radius, width=3) 
        pygame.draw.circle(view, (255,255,255),
            CENTER, 3, width=3)
        #if self.rect.x == 0:
           # self.kill()
            #perdeu = True
    


# numeros = random.getstate()
#print(random.sample(range(10), k=5))

class Target():
    global initial_radius
    global orbits
    orbits = 0
    def __init__(self, quantity = Target_quantity, variations = 4):
        super().__init__()
        global ball_coordinates
        global orbit_space
        ball_coordinates = tuple()

        for i in range(Target_quantity):
            # Set orbits coordinates
            orbit_space = initial_radius/(Target_quantity+1)
            x = CENTER[0] + (i+1)*orbit_space
            y = CENTER[1]
            angle = random.uniform(0, 2*math.pi)
            center_distance = math.sqrt(math.pow((x-CENTER[0]),2) + math.pow((y-CENTER[1]),2))
            speed = randint(-1, 3)
            if speed == 0:
                speed = 1

            # while True:                
            #     x = random.randrange(0, WIDTH, 1)
            #     y = random.randrange(0, HEIGHT, 1)
            #     if center_distance<initial_radius:
            #         break

            type = random.sample(set('ASDF'), 1)
            ball_coordinates += tuple([(center_distance,angle,type,speed,i)])
        # print(ball_coordinates)

    def update(self):
        global orbits
        global remaining_time
        time_factor =(play_time-remaining_time)/play_time
        orbits = orbits+0.5/fps
        if orbits>360:
            orbits = 0
        for center, angle, type, speed, index in ball_coordinates:
            index_factor = (Target_quantity-index)/Target_quantity
            time_index = index_factor*time_factor
            color = A_color
            match type:
                case ['A']:
                    color = A_color
                case ['S']:
                    color = S_color
                case ['D']:
                    color = D_color
                case ['F']:
                    color = F_color
            if center<current_radius:
                # x = CENTER[0] - ((index+1)*orbit_space)*pow(math.cos(orbits+angle),2)
                #y = CENTER[1] - ((index+1)*orbit_space)*pow(math.sin(orbits+angle),2)
                x = CENTER[0] - ((index+1)*orbit_space)*math.cos((orbits+angle)*speed)
                y = CENTER[1] - ((index+1)*orbit_space)*math.sin((orbits+angle)*speed)
                pygame.draw.circle(view, color, 
                    (x,y), 6, width=2)                
            # else:
            #     # x = CENTER[0] - ((index+1)*orbit_space)*math.cos((orbits+angle)*(speed*time_index))
            #     # y = CENTER[1] - ((index+1)*orbit_space)*math.sin((orbits+angle)*(speed*time_index))
            #     pygame.draw.circle(view, (255*time_factor,255*time_index,255*index_factor), 
            #         (x,y), 5, width=5)



main_circle = Shrinking_circle(circle_radius)
game_time = Remaining_time(play_time)
ball_target = Target()
clock = Clock()
frame = 0

def key_action(key):
    global ball_coordinates
    global current_radius
    global score
    for center, angle, type, speed, index in ball_coordinates:
        if center>current_radius-key_tolerance:
            if ['{}'.format(key)] == type:
                print('Ganhô: {}'.format(key))
                score += 1
            else:
                print('Errou {} -> {}!'.format(key, type))
            break

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
                key_action('A')
                #print('A')
            if evento.key == K_s:
                key_action('S')
                #print('S')
            if evento.key == K_d:
                key_action('D')
                #print('D')
            if evento.key == K_f:
                key_action('F')
                #print('F')
    
    frame +=1
    main_circle.update()
    game_time.update()
    ball_target.update()
    display.update()