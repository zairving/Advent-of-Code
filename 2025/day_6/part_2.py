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

def parse_column(column: List[str], width: int) -> List[int]:
    """
    Parse the column into the right-to-left format required.
    
    Parameters
    ----------
    column : List[str]
        The column of numbers.
    width : int
        The width of the column.
    
    Returns
    -------
    List[int]
        The parsed column of numbers.
    """
    
    numbers = []
    for i in range(1, width + 1):
        number = ''
        for num_string in column:
            number += num_string[-i]
        try:
            numbers.append(int(number))
        except ValueError:
                continue
    
    return numbers

t_start = time.time()

total = 0

column_widths = []
columns = []
with open('input.txt', 'r') as file:
    # operator always to left side of column
    # spaces between operators gives width of column
    
    # get last line
    for line in file:
        pass
    last_line = line
    last_line = last_line.split(' ')
    
    # determine the width of each column
    col_width = 1  # minimum width is 1 since operator constitutes part of the column
    for element in last_line[1:]:
        if element == '':
            col_width += 1
        else:
            column_widths.append(col_width)
            col_width = 1
    column_widths.append(col_width)  # include width of final column

with open('input.txt', 'r') as file:
    for i, line in enumerate(file):
        line = line.replace('\n', '')
        
        cols = []
        for j, width in enumerate(column_widths):
            # get index corresponding to start of column
            start = sum(column_widths[:j]) + j
            # extract column from line
            cols.append(line[start:start + width])
        
        if i == 0:
            columns = [[] for col in cols]
        for k, col in enumerate(cols):
            columns[k].append(col)

for i, column in enumerate(columns):
    operation = column.pop().strip()  # get operation
    column = parse_column(column, column_widths[i])
    if operation == '*':
        total += multiply(column)
    else:
        total += sum(column)

t_stop = time.time()

print(total)
print(f'Took {1000*(t_stop - t_start):.1f} ms')  # 33.2 ms
