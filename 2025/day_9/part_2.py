import time

import numpy as np
import shapely

coords = []
with open('input.txt', 'r') as file:
    for line in file:
        x, y = line.strip().split(',')
        coords.append((int(x), int(y)))

t_start = time.time()

# create polygon from input coordinates
polygon = shapely.Polygon(coords)
shapely.prepare(polygon)  # prepare polygon for faster evaluation of contains()

max_area = 0. 
for i, point in enumerate(coords):
    # add 1 to prevent zero width in either dimension
    deltas = 1 + np.abs(np.subtract(coords, point))
    areas = np.multiply(deltas[:, 1], deltas[:, 0])  # get areas of all rectangles
    
    valid = False
    while not valid:
        j = np.argmax(areas)  # index of largest area
        area = areas[j]
        areas[j] = 0
        
        # define rectangle
        c1 = coords[i]
        c2 = (coords[i][0], coords[j][1])
        c3 = coords[j]
        c4 = (coords[j][0], coords[i][1])
        rect = shapely.Polygon([c1, c2, c3, c4])
        
        # if the rectangle is within the original polygon
        if polygon.contains(rect):
            valid = True
    
    if area > max_area:
        max_area = area

t_stop = time.time()

print(max_area)
print(f'Took {t_stop - t_start:.1f} s')  # 4.0 s 