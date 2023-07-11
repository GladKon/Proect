import math

from settings import *
import pygame


class Player:
    def __init__(self):
        self.x, self.y = start_pos
        self.angl = start_angl
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        self.player_move = {'Up': True, 'Dawn': True, 'Right': True, 'Left': True}

    def get_pos(self):
        return self.x, self.y

    def move(self):

        sin_a = math.sin(self.angl)
        cos_a = math.cos(self.angl)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and player_move["Up"]:
            self.x += start_speed * cos_a
            self.y += start_speed * sin_a
        if keys[pygame.K_s] and player_move["Dawn"]:
            self.x += -start_speed * cos_a
            self.y += -start_speed * sin_a
        if keys[pygame.K_a] and player_move["Left"]:
            self.x += start_speed * sin_a
            self.y += -start_speed * cos_a
        if keys[pygame.K_d] and player_move["Right"]:
            self.x += -start_speed * sin_a
            self.y += start_speed * cos_a

        if keys[pygame.K_LEFT]:
            self.angl -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angl += 0.05
        if self.x <= 0:
            self.x = 5
        if self.x >= win_x // 5 - 5:
            self.x = win_x // 5 - 5
        if self.y <= 0:
            self.y = 5
        if self.y >= win_y // 5 - 5:
            self.y = win_y // 5 - 5
        self.rect = pygame.Rect(self.x - 5, self.y - 5, 10, 10)

    def proverka(self, coor_s, win):
        player_move['Right'] = True
        player_move['Up'] = True
        player_move['Dawn'] = True
        player_move['Left'] = True
        sin_a = math.sin(self.angl)
        cos_a = math.cos(self.angl)
        for y, x in coor_s:
            pygame.draw.rect(win, (150, 5, 0), (y, x, s_x, s_y), 2)
            rect = pygame.Rect(y, x, s_x, s_y)
            X, Y = self.get_pos()
            X -= 4
            Y -= 4
            X1 = X + (-start_speed * cos_a)
            Y1 = Y + (start_speed * sin_a)
            Rect = pygame.Rect(X1, Y1, 8, 8)
            pygame.draw.rect(win, (255, 1, 1), Rect)
            if Rect.colliderect(rect):
                player_move['Right'] = False
            X1 = X + start_speed * cos_a
            Y1 = Y + start_speed * sin_a
            Rect = pygame.Rect(X1, Y1, 8, 8)
            pygame.draw.rect(win, (255, 0, 0), Rect)
            if Rect.colliderect(rect):
                player_move['Up'] = False
            X1 = X + (-start_speed * cos_a)
            Y1 = Y + (-start_speed * sin_a)
            Rect = pygame.Rect(X1, Y1, 8, 8)
            pygame.draw.rect(win, (255, 1, 1), Rect)
            if Rect.colliderect(rect):
                player_move['Dawn'] = False
            X1 = X + (start_speed * cos_a)
            Y1 = Y + (-start_speed * sin_a)
            Rect = pygame.Rect(X1, Y1, 8, 8)
            pygame.draw.rect(win, (255, 1, 1), Rect)
            if Rect.colliderect(rect):
                player_move['Left'] = False

