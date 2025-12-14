# given a line of numbers (e.g., 12345)
# get the largest possible number (in the above case, 45)

import time
from typing import List

def get_max_value(numbers: List[str]) -> int:
    """
    Get the maximum two-digit number from a list of single-digit integers.
    
    Parameters
    ----------
    numbers : List[str]
        The list of single-digit integers.
    
    Returns
    -------
    int
        The maximum two-digit integer.
    """
    
    i_first = numbers.index(max(numbers[:-1]))  # index() returns first index, so no need to worry about repeated numbers
    i_last = numbers.index(max(numbers[i_first + 1:]))
    
    return int(numbers[i_first] + numbers[i_last])

t_start = time.time()

max_values = []

with open('input.txt', 'r') as file:
    for line in file:
        max_value = get_max_value(list(line.strip()))
        max_values.append(max_value)

t_stop = time.time()

print(sum(max_values))
print(f'Took {1000 * (t_stop - t_start):.1f} ms')  # 3.4 ms