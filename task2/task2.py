import math
import os

if os.path.isfile('points.txt'):
    print('Файл points.txt существует.')
else:
    print('Файл points.txt не существует.')

if os.path.isfile('center and rad.txt'):
    print('Файл center and rad.txt существует.')
else:
    print('Файл center and rad.txt не существует.')

with open('center and rad.txt', 'r', encoding='utf-8') as f:
    if os.stat('center and rad.txt').st_size == 0:
        print('Файл center and rad.txt пустой.')
    else:
        center_line = f.readline().strip()
        radius_line = f.readline().strip()

        center = list(map(float, center_line.split()))
        radius = float(radius_line)

if radius == int(radius):
    print('Радиус является целым числом.')
else:
    print('Радиус не является целым числом.')
    exit()



with open('points.txt', 'r', encoding='utf-8') as f:

    if os.stat('points.txt').st_size == 0:
        print('Файл points.txt пустой.')
    else:
        point_list = []

        for line in f:
            line = line.strip()
            if line:


                coord = list(map(float, line.split()))
                point_list.append(coord)


if 1 <= len(point_list) <= 100:
    print(f'Количество точек от 1 до 100: {len(point_list)}.')
else:
    print(f'Количество точек вне диапазона 1-100, а именно: {len(point_list)}.')
    exit()


for point in point_list:
    d = math.sqrt(math.pow(point[0] - center[0], 2) + math.pow(point[1] - center[1], 2))
    if d < radius:
        print("1 - точка лежит внутри окружности.")
    if d > radius:
        print("2 - точка лежит вне окружности.")
    if d == radius:
        print("0 - точка лежит на окружности.")