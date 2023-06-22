import math

import pygame

from settings import *
from Player import Player

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
    if dist > r + max_dist:
        return True
    elif dist < r - min_dist:
        return False
    else:
        return False


pygame.init()
win = pygame.display.set_mode((win_x,win_y))
Clock = pygame.time.Clock()
player = Player()

Life = True

while Life == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Life = False

    win.fill(BG_color)

    pygame.draw.circle(win,Person_color,player.get_pos(),12)
    pygame.draw.line(win, Person_color,player.get_pos() ,(player.x + win_x * math.cos(player.angl), player.y + win_y * math.sin(player.angl)))

    flag = True

    X, Y = player.get_pos()

    for x, y in coor_s:
        pygame.draw.rect(win,(150,5,0),(y,x,s_x,s_y),2)
        if flag == True:
            flag = check_intersection((x,y,x + s_x,y + s_y),(X,Y,4))

    if flag == True:
        player.move()




    pygame.display.flip()
    Clock.tick(FPS)

# TEST