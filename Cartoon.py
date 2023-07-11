from settings import s_x, s_y, map_list

coor_s = set()

def Cartoon(s_x, s_y, map_list,coor_s):
    for i , stroka in enumerate(map_list):
        for j, simvol in enumerate(stroka):
            if simvol == 'S':
                coor_s.add((j * s_x, i * s_y))

