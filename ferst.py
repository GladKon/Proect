import pygame
from settings import *
from Player import *
from Cartoon import *

player = Player()


def Bullet(win, angle):
    keys = pygame.key.get_pressed()
    sin_a, cos_a = angle
    Delit = 0
    if keys[pygame.K_SPACE]:
        X, Y = player.get_pos()
        Bullet = pygame.Rect(X, Y, 2, 2)

        while Delit != 1:
            pygame.draw.rect(win, (0, 128, 128), Bullet)
            for i in coor_s:
                x, y = i
                wool = pygame.Rect(x, y, 2, 2)
                if Bullet.colliderect(wool):
                    coor_s.discard(i)
                    Delit = 1
            X1 = X + (Bullet_speed * cos_a)
            Y1 = Y + (Bullet_speed * sin_a)
            Bullet = pygame.Rect(X1, Y1, 2, 2)


