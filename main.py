import math

import pygame

from settings import *
from Player import Player
from ray_cating import ray_casting
from Cartoon import *


def check_intersection(square, circle):
    x1, y1, x2, y2 = square
    xc, yc, r = circle

    # Вычисляем координаты центра квадрата
    xs, ys = (x1 + x2) / 2, (y1 + y2) / 2

    # Вычисляем длину диагонали и стороны квадрата
    diagonal = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    side = diagonal / math.sqrt(2)

    # Вычисляем максимальное и минимальное расстояние от центра квадрата до его границы
    max_dist = diagonal / 2
    min_dist = side / 2

    # Вычисляем расстояние от центра квадрата до центра круга
    dist = math.sqrt((xs - xc) ** 2 + (ys - yc) ** 2)

    # Проверяем условия пересечения
    if dist < r - min_dist:
        return player.get_pos()
    else:
        return player.get_pos()


pygame.init()
win = pygame.display.set_mode((win_x, win_y))
Clock = pygame.time.Clock()
player = Player()

Cartoon(s_x, s_y, map_list,coor_s)

Life = True

while Life == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Life = False

    win.fill(BG_color)

    ray_casting(win, player.get_pos(), player.angl)

    flag = True

    X, Y = player.get_pos()

    player.proverka(coor_s, win)







    pygame.draw.circle(win, Person_color, player.get_pos(), 5)
    if flag == True:
        player.move()


    sin_a = math.sin(player.angl)
    cos_a = math.cos(player.angl)
    x1 , y1 = player.get_pos()
    for d in range(1, Max_rause):
        x2 = x1 + d * cos_a
        y2 = y1 + d * sin_a

        if (x2 // s_x * s_x, y2 // s_y * s_y) in coor_s:
            pygame.draw.line(win, Person_color,(x1, y1), (x2, y2), 1)
            break
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        for i in coor_s:
            x, y = i
            if x < x2 < x + s_x and y < y2 < y + s_y:
                coor_s.remove(i)
                break

    pygame.display.flip()
    Clock.tick(FPS)

# TEST
