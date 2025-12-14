import time
from typing import List

def check_accessibility(grid: List[str], row: int, col: int) -> bool:
    """
    Check if a grid point is accessible.
    
    Parameters
    ----------
    grid : List[str]
        The grid.
    row : int
        The row of the grid point.
    col : int
        The column of the grid point.
    
    Returns
    -------
    bool
        Whether the grid point is accessible.
    """
    
    adjacent_rolls = 0
    
    for rows in range(-1, 2):
        # do not go beyond the grid
        if row + rows < 0 or row + rows >= len(grid):
            continue
        for cols in range(-1, 2):
            # do not go beyond the grid and do not include the grid point itself
            if col + cols < 0 or col + cols >= len(grid[row]) or (row + rows == row and col + cols == col):
                continue
            
            if grid[row + rows][col + cols] == '@':
                adjacent_rolls += 1
    
    # grid point is accessible if there are fewer than 4 adjacent rolls
    return adjacent_rolls < 4

grid = []

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(line.strip())

t_start = time.time()

counter = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '@':
            accessible = check_accessibility(grid, row, col)
            if accessible:
                counter += 1

t_stop = time.time()

print(counter)
print(f'Took {1000 * (t_stop - t_start):.1f} ms')  # 32.3 ms