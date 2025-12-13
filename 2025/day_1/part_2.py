# circular number dial from 0-99
# L8 means rotate left (decreasing) 8 numbers
# R4 means rotate right (increasing) 4 numbers
# etc.

import time
from typing import Tuple

num = 50  # wheel starts on 50
zeros_passed = 0

def rotate_dial(num: int, move: str) -> Tuple[int, int]:
    """
    Given a move (e.g., "R8"), rotate the number dial to get the new number and the number of times the dial passes 0.
    
    Parameters
    ----------
    num : int
        The current number.
    move : str
        The move (e.g., "R8").
    
    Returns
    -------
    Tuple[int, int]
        The new number and the number of times 0 has been passed.
    """
    
    zeros_passed = 0
    
    # get direction of rotation
    if move[0] == 'L':
        direction = -1
    else:
        direction = 1
    
    # get number of rotations
    turns = int(move[1:])
    
    # get new number
    raw_num = num + direction * turns
    new_num = raw_num % 100
    
    # get number of times zero has been passed
    zeros_passed += abs(raw_num) // 100
    
    # need to account for case when abs(raw_num) < 100
    if num > 0 and raw_num <= 0:
        zeros_passed += 1
    
    return new_num, zeros_passed

t_start = time.time()

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        num, iter_zeros_passed = rotate_dial(num, line)
        zeros_passed += iter_zeros_passed

t_stop = time.time()

print()
print(zeros_passed)  # Answer: 6616
print()
print(f'Took {(t_stop - t_start) * 1000:.1f} ms')  # 4.2 ms
