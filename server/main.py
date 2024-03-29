import socket
import pickle
from _thread import start_new_thread

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)
print("Server Started. Waiting for a connection.")

players = [{"x": 25, "y": 40}, {"x": 25, "y": 25}]


def threaded_client(conn, player):
    global players,currentPlayer
    conn.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Connection lost")
    conn.close()
    currentPlayer -= 1

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1