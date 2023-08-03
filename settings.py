import math


win_x = 1200
win_y = 700
BG_color = 150,230.5,200
FPS = 40
start_pos = win_x//10 - 15, win_y//10
start_angl = 0
start_speed = 1
Person_color = 10,10,110
Bullet_speed = 0.01

player_move = {'Up': True, 'Dawn': True, 'Right': True, 'Left': True}

map_list = [
    'SSSSSSSSSSSSSSSS',
    'S..S...S...SS...',
    'S..SSS...S....SS',
    'S....S..SS.S.SSS',
    'S..S....S..S...S',
    'S..S...SSS.SSS.S',
    '.....S.........S',
    'SSSSSSSSSSSSSSSS'
]
s_y = (win_y // len(map_list)) // 5
s_x = (win_x // len(map_list[0])) // 5


FOV = math.pi / 3
Half_Fov = FOV / 2
Num_raus = 240
Delta_Angle = FOV / Num_raus
Max_rause = 1000

H = 15
D = Num_raus / (2 * math.tan(Half_Fov))
coef = H * D * s_x // 6
HSKALA = win_x // Num_raus
