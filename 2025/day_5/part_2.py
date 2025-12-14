import time
from typing import List

def clip_ranges(ranges: List[str]) -> List[str]:
    """
    Given a list of ranges, clip them to prevent overlap.
    
    Parameters
    ----------
    ranges : List[str]
        The list of ranges (e.g., 10-15).
    
    Returns
    -------
    List[str]
        The clipped ranges with no overlap.
    """
    
    clipped_ranges = []
    indices_to_ignore = []
    
    for i, irange in enumerate(ranges):
        ilo, ihi = irange.split('-')
        ilo = int(ilo)
        ihi = int(ihi)
        
        for j, jrange in enumerate(ranges[i+1:]):
            jlo, jhi = jrange.split('-')
            jlo = int(jlo)
            jhi = int(jhi)
            
            if jlo <= ilo <= jhi < ihi:
                ilo = int(jhi) + 1
            
            if ilo < jlo <= ihi <= jhi:
                ihi = int(jlo) - 1
            
            if ilo >= jlo and ihi <= jhi:
                indices_to_ignore.append(i)
            elif jlo >= ilo and jhi <= ihi:
                indices_to_ignore.append(j + i + 1)
        
        if i not in indices_to_ignore:
            clipped_ranges.append(f'{ilo}-{ihi}')
    
    return clipped_ranges

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

fresh_ids = 0
ranges = clip_ranges(ranges)

for irange in ranges:
    lo, hi = irange.split('-')
    fresh_ids += int(hi) - int(lo) + 1

t_stop = time.time()

print(fresh_ids)
print(f'Took {1000 * (t_stop - t_start):.1f} ms')  # 3.6 ms