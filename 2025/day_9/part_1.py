import time

import numpy as np

coords = []
with open('input.txt', 'r') as file:
    for line in file:
        col, row = line.strip().split(',')
        coords.append([int(row), int(col)])

t_start = time.time()

max_area = 0. 
for i, point in enumerate(coords):
    # add 1 to prevent zero width in either dimension
    deltas = 1 + np.abs(np.subtract(coords, point))
    areas = np.multiply(deltas[:, 0], deltas[:, 1])  # get areas of all rectangles
    j = np.argmax(areas)  # index of largest area
    area = areas[j]
    
    if area > max_area:
        max_area = area

t_stop = time.time()

print(max_area)
print(f'Took {1000*(t_stop - t_start):.1f} ms')  # 67.5 ms