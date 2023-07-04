import math


win_x = 1200
win_y = 700
BG_color = 150,230.5,200
FPS = 40
start_pos = win_x//2 -100, win_y//2
start_angl = 0
start_speed = 5
Person_color = 10,10,110

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
s_y = win_y // len(map_list)
s_x = win_x // len(map_list[0])

FOV = math.pi / 3
Half_Fov = FOV / 2
Num_raus = 60
Delta_Angle = FOV / Num_raus
Max_rause = 1000

H = 5
D = Num_raus / (2 * math.tan(Half_Fov))
coef = H * D * s_x
HSKALA = win_x / Num_raus
