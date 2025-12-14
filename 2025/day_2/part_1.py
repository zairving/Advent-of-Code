# given a range, e.g., 10-20
# find numbers that are made up of repeated digits (e.g., 11, 22, 1212, etc.)

import time

def check_id(id: str) -> bool:
    """
    Check if an ID contains repeated digits.
    
    Parameters
    ----------
    id : str
        The ID (e.g., "1234").
    
    Returns
    -------
    bool
        `True` if the ID contains no repeated digits, `False` otherwise.
    """
    
    # ID can only have repeated digits if it has an even number of digits
    if len(id) % 2 == 0:
        # split number in half
        first_half = id[:len(id) // 2]
        second_half = id[len(id) // 2:]
        if first_half == second_half:
            return False
    
    return True

t_start = time.time()

with open('input.txt', 'r') as file:
    ranges = file.read().split(',')

invalid_ids = []

for id_range in ranges:
    lo, hi = id_range.split('-')  # get range
    # iterate through range
    for id in range(int(lo), int(hi)):
        valid = check_id(str(id))
        if not valid:
            invalid_ids.append(id)

t_stop = time.time()

print(sum(invalid_ids))
print(f'Took {(t_stop - t_start) * 1000:.1f} ms')  # 835.9 ms