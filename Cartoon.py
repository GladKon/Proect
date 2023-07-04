from settings import *
coor_s = set()
for i , stroka in enumerate(map_list):
    for j, simvol in enumerate(stroka):
        if simvol == 'S':
            coor_s.add((j * s_x, i * s_y))
