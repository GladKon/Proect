from settings import win_y, win_x
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
coor_s = set()
for i , stroka in enumerate(map_list):
    for j, simvol in enumerate(stroka):
        if simvol == 'S':
            coor_s.add((i * s_y, j * s_x))
