# given a list of M (x, y, z) coords, connect the closest M pairs of coords
# the answer is then the product of the distances between the connected pairs

import time

from scipy.spatial.distance import cdist
import numpy as np

t_start = time.time()

isolated_nodes = []

with open('input.txt', 'r') as file:
    for line in file:
        coords = line.strip().split(',')
        coords = [int(ordinate) for ordinate in coords]
        isolated_nodes.append(coords)

# get Euclidean distances between all pairs of nodes
distances = cdist(isolated_nodes, isolated_nodes, metric='euclidean')

# mask for ignored elements
mask = np.eye(len(isolated_nodes), dtype=bool)  # diagonal distances are zero so need to be ignored
circuits = []

for _ in range(1000):
    distances[mask] += np.inf  # mask distances by making them infinitely large
    indices = np.argmin(distances)  # get index of minimum distance
    i, j = np.unravel_index(indices, distances.shape)
    
    # make sure nodes aren't paired up again
    mask[i, j] = True
    mask[j, i] = True
    
    added = False
    added_index = -1
    for k in range(len(circuits)):
        if added:
            continue
        
        node_1 = isolated_nodes[i] in circuits[k]
        node_2 = isolated_nodes[j] in circuits[k]
        
        if node_1 ^ node_2:
            # add new node to circuit
            if node_1:
                circuits[k].append(isolated_nodes[j])
            else:
                circuits[k].append(isolated_nodes[i])
            added = True
            added_index = k
        
        if node_1 and node_2:
            # do nothing since both nodes are already in the same circuit
            added = True
            added_index = k
    
    # check if circuits needs to be combined
    if added:
        for k in range(len(circuits)):
            # avoid adding a circuit to itself
            if k == added_index:
                continue
            
            # if one of the newly connected nodes appears in another circuit
            if isolated_nodes[i] in circuits[k] or isolated_nodes[j] in circuits[k]:
                # combine circuits
                for node in circuits[k]:
                    if node not in circuits[added_index]:
                        circuits[added_index].append(node)
                
                # delete old circuit
                circuits.pop(k)
                break
    
    if not added:
        # create new circuit
        circuits.append([isolated_nodes[i], isolated_nodes[j]])

# sort list by length
circuits = sorted(circuits, key=len, reverse=True)
answer = len(circuits[0]) * len(circuits[1]) * len(circuits[2])

t_stop = time.time()

print(answer)
print(answer == 40)
print(f'Took {1000*(t_stop - t_start):.1f} ms')  # 479.8 ms