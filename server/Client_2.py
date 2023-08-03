import pygame
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


class Player:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


def redraw_window(win, player, player2):
    win.fill((255, 255, 255))
    pygame.draw.circle(win, (0, 0, 0), (player.x, player.y), player.radius)
    pygame.draw.circle(win, (0, 0, 0), (player2.x, player2.y), player2.radius)
    pygame.display.update()


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    p = Player(50, 50, 10)
    p2 = Player(100, 100, 10)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        try:
            data = client.recv(2048)
            if data:
                p2Pos = pickle.loads(data)
                p2.x = p2Pos["x"]
                p2.y = p2Pos["y"]
            else:
                print("No data received from the server.")
                break
        except EOFError:
            print("Failed to receive data from the server.")
            break

        # Update player position and send to server
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            p.x -= 1
        if keys[pygame.K_RIGHT]:
            p.x += 1
        if keys[pygame.K_UP]:
            p.y -= 1
        if keys[pygame.K_DOWN]:
            p.y += 1

        client.send(pickle.dumps({"x": p.x, "y": p.y}))

        # Redraw the game window
        redraw_window(win, p, p2)
        clock.tick(60)


main()