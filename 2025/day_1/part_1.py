# circular number dial from 0-99
# L8 means rotate left (decreasing) 8 numbers
# R4 means rotate right (increasing) 4 numbers
# etc.

import time

num = 50  # wheel starts on 50
zero_counter = 0

def rotate_dial(num: int, move: str) -> int:
    """
    Given a move (e.g., "R8"), rotate the number dial to get the new number.
    
    Parameters
    ----------
    num : int
        The current number.
    move : str
        The move (e.g., "R8").
    
    Returns
    -------
    int
        The new number.
    """
    
    # get direction of rotation
    if move[0] == 'L':
        direction = -1
    else:
        direction = 1
    
    # get number of rotations
    turns = int(move[1:])
    
    # get new number
    new_num = (num + direction * turns) % 100
    
    return new_num

t_start = time.time()

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        num = rotate_dial(num, line)
        if num == 0:
            zero_counter += 1

t_stop = time.time()

print()
print(zero_counter)  # Answer: 1092
print()
print(f'Took {(t_stop - t_start) * 1000:.1f} ms')  # 5.4 ms
