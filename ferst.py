import math


def check_intersection(square, circle):
    x1, y1, x2, y2 = square
    xc, yc, r = circle

    # Вычисляем координаты центра квадрата
    xs, ys = (x1 + x2) / 2, (y1 + y2) / 2

    # Вычисляем длину диагонали и стороны квадрата
    diagonal = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    side = diagonal / math.sqrt(2)

    # Вычисляем максимальное и минимальное расстояние от центра квадрата до его границы
    max_dist = diagonal / 2
    min_dist = side / 2

    # Вычисляем расстояние от центра квадрата до центра круга
    dist = math.sqrt((xs - xc) ** 2 + (ys - yc) ** 2)

    # Проверяем условия пересечения
    if dist > r + max_dist:
        return "Круг и квадрат не пересекаются."
    elif dist < r - min_dist:
        return "Круг находится внутри квадрата."
    else:
        return "Круг и квадрат пересекаются."


# Тестовый случай
square = (10, 10, 12, 12)  # Квадрат с координатами диагонали (0, 0) и (2, 2)
circle = (8., 11, 1)  # Круг с центром в точке (1, 1) и радиусом 1

print(check_intersection(square, circle))  # Круг находится внутри квадрата.