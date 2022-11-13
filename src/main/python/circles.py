from random import randint
import pygame
from pygame import font
from pygame import display
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_a, K_s, K_d, K_f
from pygame.time import Clock


pygame.init()

fps = 60
tamanho = 800, 600
fonte = font.SysFont('comicsans', 50)
fonte_perdeu = font.SysFont('comicsans', 300)

superficie = display.set_mode(
    size=tamanho,
    display=0
)
display.set_caption(
    'Shrinking Circle'
)


# import the time module
import time
  
# define the countdown func.
class Remaining_time():
    def __init__(self, time_s):
        super().__init__()
        global remaining_time 
        remaining_time = time_s

    def update(self):
        remaining_time -= 1/fps

        if remaining_time == 0:
            # self.kill()
            print("Time's up!")

class Shrinking_circle():
    def __init__(self, radius):
        super().__init__()

        # self.image = load('images/inimigo_1.png')
        self.rect = self.image.get_rect(
            center=(800, randint(20, 580))
        )

    def update(self):
        global perdeu
        self.rect.x -= 0.1

        if self.rect.x == 0:
            self.kill()
            perdeu = True

#class Target():

clock = Clock()

while True:
    clock.tick(fps)

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