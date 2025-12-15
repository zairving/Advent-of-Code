# given columns of numbers and followed by an operator
# e.g.,:
# 8 9
# 8 9
# 1 1
# * +
# the answer is then (8 * 8 * 1) + (9 + 9 + 1)

import time
from typing import List

def multiply(column: List[int]) -> int:
    """
    Multiply a column of numbers.
    
    Parameters
    ----------
    column : List[int]
        The column of numbers.
    
    Returns
    -------
    int
        The product of all the numbers in the column.
    """
    
    product = column.pop()
    
    while len(column) > 0:
        product *= column.pop()
    
    return product

t_start = time.time()

total = 0

columns = list()
with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.strip()
        cols = line.split(' ')
        cols = [col for col in cols if len(col) > 0]  # remove empty elements
        if i == 0:
            columns = [[] for col in cols]
        for j, col in enumerate(cols):
            columns[j].append(col)

for column in columns:
    operation = column.pop()  # get operation
    
    column = [int(num) for num in column]
    
    if operation == '*':
        total += multiply(column)
    else:
        total += sum(column)

t_stop = time.time()

print(total)
print(total == 4277556)
print(f'Took {1000*(t_stop - t_start):.1f} ms')  # 1.7 ms
