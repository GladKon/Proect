import math

from settings import *
import pygame


class Player:
    def __init__(self):
        self.x, self.y = start_pos
        self.angl = start_angl

    def get_pos(self):
        return self.x, self.y

    def move(self):
        sin_a = math.sin(self.angl)
        cos_a = math.cos(self.angl)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.x += start_speed * cos_a
            self.y += start_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -start_speed * cos_a
            self.y += -start_speed * sin_a
        if keys[pygame.K_a]:
            self.x += start_speed * sin_a
            self.y += -start_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -start_speed * sin_a
            self.y += start_speed * cos_a

        if keys[pygame.K_LEFT]:
            self.angl -= 0.08
        if keys[pygame.K_RIGHT]:
            self.angl += 0.08