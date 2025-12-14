import time
from typing import List, Tuple

def check_accessibility(grid: List[str], row: int, col: int) -> Tuple[bool, List[str]]:
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
    Tuple[bool, List[str]]
        Whether the grid point is accessible and the updated grid (with the accessible point removed).
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
    
    accessible = adjacent_rolls < 4
    
    if accessible:
        grid[row] = grid[row][:col] + '.' + grid[row][col + 1:]  # remove roll from grid
    
    # grid point is accessible if there are fewer than 4 adjacent rolls
    return accessible, grid

def iter(grid: List[str]) -> Tuple[bool, List[str]]:
    """
    Iterate through the grid until an accessible roll is found.
    
    Parameters
    ----------
    grid : List[str]
        The grid.
    
    Returns
    -------
    Tuple[bool, List[str]]
        Whether an accessible roll is found and the updated grid (with the accessible roll removed).
    """
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@':
                accessible, grid = check_accessibility(grid, row, col)
                if accessible:
                    return True, grid
    
    return False, grid

grid = []

with open('input.txt', 'r') as file:
    for line in file:
        grid.append(line.strip())

t_start = time.time()

counter = 0
converged = False

while not converged:
    accessible, grid = iter(grid)
    
    if accessible:
        counter += 1
    else:
        converged = True

t_stop = time.time()

print(counter)
print(f'Took {(t_stop - t_start):.1f} s')  # 14.8 s