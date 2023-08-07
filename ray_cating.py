import pygame
import math

from settings import *
from Cartoon import *

def ray_casting(screen, player_pos, player_angle,oponent_pos):
    x1, y1 = player_pos
    start_angle = player_angle - Half_Fov
    for i in range(Num_raus):
        sin_a = math.sin(start_angle)
        cos_a = math.cos(start_angle)
        for d in range(1, Max_rause):
            x2 = x1 + d * cos_a
            y2 = y1 + d * sin_a
            # pygame.draw.line(screen, (255, 0, 0), (x1, y1), (x2, y2), 1)
            if (x2 // s_x * s_x, y2 // s_y * s_y) in coor_s:
                visota = coef / d
                pygame.draw.rect(screen,(255, 255, 255), (i * HSKALA, win_y // 2 - visota // 2, HSKALA, visota))
                break

            if (x2 // s_x * s_x, y2 // s_y * s_y) == oponent_pos:
                visota = coef / d
                pygame.draw.rect(screen, (255, 0, 0), (i * HSKALA, win_y // 2 - visota // 2, HSKALA, visota))
                break
        start_angle += Delta_Angle