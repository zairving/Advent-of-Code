import time
from typing import List

def check_ingredient_is_fresh(ranges: List[str], ingredient: int) -> bool:
    """
    Check if an ingredient (integer) falls within any of the given ranges.
    
    Parameters
    ----------
    ranges : List[str]
        The ranges (e.g., 10-15).
    ingredient : int
        An ingredient number.
    
    Returns
    -------
    bool
        If the ingredient falls within any of the given ranges.
    """
    
    for irange in ranges:
        lo, hi = irange.split('-')
        
        if int(lo) <= ingredient <= int(hi):
            return True
    
    return False

ranges = []
ingredients = []

white_space_passed = False

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line == '':
            white_space_passed = True
            continue
        
        if not white_space_passed:
            ranges.append(line)
        else:
            ingredients.append(int(line))

t_start = time.time()

fresh_veggies = 0

for ingredient in ingredients:
    fresh = check_ingredient_is_fresh(ranges, ingredient)
    if fresh:
        fresh_veggies += 1

t_stop = time.time()

print(fresh_veggies)
print(fresh_veggies == 3)
print(f'Took {1000 * (t_stop - t_start):.1f} ms')  # 17.3 ms