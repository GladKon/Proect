import math

import pygame

from settings import *
from Player import Player
from ray_cating import ray_casting
from Cartoon import *
from ferst import *
import socket
import pickle
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "127.0.0.1"
port = 5555
address = (server, port)

try:
    client.connect(address)
except socket.error as e:
    print("Failed to connect to the server:", e)
    sys.exit(1)

pygame.init()
win = pygame.display.set_mode((win_x, win_y))
Clock = pygame.time.Clock()
player = Player()

Cartoon(s_x, s_y, map_list, coor_s)

Life = True

while Life == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Life = False
    try:
        data = client.recv(2048)
        if data:
            p2Pos = pickle.loads(data)
            player.x = p2Pos["x"]
            player.y = p2Pos["y"]
        else:
            print("No data received from the server.")
            break
    except EOFError:
        print("Failed to receive data from the server.")
        break
    win.fill(BG_color)
    print(player.get_pos())
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
    print(player.get_pos())
    # Bullet(win, player.angle())
    client.send(pickle.dumps({"x": player.x, "y": player.y}))
    pygame.display.flip()
    Clock.tick(FPS)


