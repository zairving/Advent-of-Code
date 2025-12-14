# given a line of numbers (e.g., 12345)
# get the largest possible number (in the above case, 45)

import time
from typing import List

def get_max_value(numbers: List[str]) -> int:
    """
    Get the maximum twelve-digit number from a list of single-digit integers.
    
    Parameters
    ----------
    numbers : List[str]
        The list of single-digit integers.
    
    Returns
    -------
    int
        The maximum twelve-digit integer.
    """
    
    indices = [-1]
    number = str()
    
    for i in range(12):
        if i < 11:
            new_numbers = numbers[indices[-1] + 1:-(11 - i)]
        else:
            new_numbers = numbers[indices[-1] + 1:]
        
        digit = max(new_numbers)
        index = new_numbers.index(digit)
        
        indices.append(indices[-1] + 1 + index)
        number += digit
    
    return int(number)

t_start = time.time()

max_values = []

with open('input.txt', 'r') as file:
    for line in file:
        max_value = get_max_value(list(line.strip()))
        max_values.append(max_value)

t_stop = time.time()

print(sum(max_values))
print(sum(max_values) == 3121910778619)
print(f'Took {1000 * (t_stop - t_start):.1f} ms')  # 6.0 ms