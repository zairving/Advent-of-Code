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
    
    for i in range(len(id) // 2):
        digits = id[:i + 1]
        valid = check_digits_repeated(digits, id)
        if not valid:
            return False
    
    return True

def check_digits_repeated(digits: str, id: str) -> bool:
    """
    Check if `digits` are repeated in `id`.
    
    Parameters
    ----------
    digits : str
        The digits.
    id : str
        The ID.
    
    Returns
    -------
    bool
        `False` if digits repeat, `True` otherwise.
    """
    
    valid = False
    
    l = len(digits)
    L = len(id)
    
    for i in range(l, L, l):
        if id[i:i + l] != digits:
            valid = True
    
    return valid

t_start = time.time()

with open('input.txt', 'r') as file:
    ranges = file.read().split(',')

invalid_ids = []

for id_range in ranges:
    lo, hi = id_range.split('-')  # get range
    # iterate through range
    for id in range(int(lo), int(hi) + 1):
        valid = check_id(str(id))
        if not valid:
            invalid_ids.append(id)

t_stop = time.time()

print(sum(invalid_ids))
print(f'Took {t_stop - t_start:.1f} s')  # 4.6 s