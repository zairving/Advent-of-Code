import time
from typing import Any, Callable

def memoize(func: Callable) -> Any:
    """
    Decorator for memoizing an arbitrary function.
    
    Parameters
    ----------
    func : Callable
        A function to be memoized.
    
    Returns
    -------
    Any
        The output of the function.
    """
    
    cache = {}
    def eval(*args: Any) -> Any:
        """
        Evaluate the memoized function, or return the cached result if it exists.
        
        Returns
        -------
        Any
            The output of the function.
        """
        
        if args not in cache:
            cache[args] = func(*args)
        
        return cache[args]
    
    return eval

@memoize
def propagate_beam(row: int, col: int) -> int:
    """
    Given some coordinates, propagate a beam.
    
    Parameters
    ----------
    row : int
        The beam's current row.
    col : int
        The beam's current column.
    
    Returns
    -------
    int
        The number of timelines.
    """
    
    if row >= len(manifold):
        # beam reached end of manifold
        return 1
    
    # split beam
    if manifold[row][col] == '^':
        # left split
        if col - 1 >= 0:
            left = propagate_beam(row + 1, col - 1)
        else:
            left = 0
        
        # right split
        if col + 1 < len(manifold[row]):
            right = propagate_beam(row + 1, col + 1)
        else:
            right = 0
        
        # get number of timelines
        timelines = left + right
    else:
        # no split, just propagate downwards
        timelines = propagate_beam(row + 1, col)
    
    return timelines

manifold = []
with open('input.txt', 'r') as file:
    for line in file:
        manifold.append(line.strip())

t_start = time.time()

starting_row = 0
starting_column = manifold[starting_row].index('S')  # get starting column for beam
total_timelines = propagate_beam(starting_row + 1, starting_column)

t_stop = time.time()

print(total_timelines)
print(f'Took {1000*(t_stop - t_start):.1f} ms')  # 2.8 ms
