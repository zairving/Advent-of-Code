from copy import copy
import time
from typing import List, Tuple

def propagate_beam(row: int, col: int) -> Tuple[int, int]:
    """
    Given some starting coordinates, propagate a beam downwards until it splits or reaches the end of the manifold.
    
    Parameters
    ----------
    row : int
        The starting row.
    col : int
        The starting column.
    
    Returns
    -------
    Tuple[int, int]
        The position at which the beam splits or reaches the end of the manifold.
    """
    
    while row < len(manifold):
        if manifold[row][col] == '^':
            return (row, col)
        row += 1
    
    # reached end of manifold
    return (-1, col)

def get_new_coords(split_pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    """
    If a beam is split, get the new coordinates for the resulting beam(s).
    
    Parameters
    ----------
    split_pos : Tuple[int, int]
        The position at which the beam is split.
    
    Returns
    -------
    List[Tuple[int, int]]
        The new starting position(s) of the split beam(s).
    """
    
    row, col = split_pos
    
    new_coords = []
    if col - 1 >= 0:
        new_coords.append((row, col - 1))
    if col + 1 < len(manifold[row]):
        new_coords.append((row, col + 1))
    
    return new_coords

manifold = []
with open('input.txt', 'r') as file:
    for line in file:
        manifold.append(line.strip())

t_start = time.time()

starting_column = manifold[0].index('S')  # get starting column for beam

coords = [(0, starting_column)]  # list of starting coordinates from which to propagate the beam
prev_coords = copy(coords)
split_coords = []  # list of coordinates at which a beam was split

while len(coords) > 0:
    row, col = coords.pop()
    split_pos = propagate_beam(row, col)
    if split_pos[0] == -1:
        # beam has reached end of manifold (may be important for part)
        pass
    else:
        if split_pos not in split_coords:
            split_coords.append(split_pos)
        new_coords = get_new_coords(split_pos)
        for new_coord in new_coords:
            # avoid propagating beams from the same position more than once
            if new_coord not in prev_coords:
                prev_coords.append(new_coord)
                coords.append(new_coord)

t_stop = time.time()

print(len(split_coords))
print(f'Took {1000*(t_stop - t_start):.1f} ms')  # 47.5 ms
