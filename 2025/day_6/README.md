# Day 6

## Part 1

Given a series of columns, with each column containing several numbers followed by a '+' or '*'. We have to calculate the sum (if the column ends with a '+') or product (if the column ends with a '\*') of the numbers in the column. The final answer is then the sum of these numbers. Solution: read each column, get the operator, and then either sum (using Python's built-in `sum()` function) or multiply (using a custom `multiply()` function) the numbers in the column. Quite straightforward. Solution reached in 6.5 ms.

## Part 2

Now the columns should be read right-to-left, numbers are now given vertically, and empty spaces within columns are important. For example, the column:
```
123
12
1
*
```
is no longer `123 * 12 * 1`, but instead `3 * 22 * 111`. Columns are not a fixed width, so the widths of the columns needs to be inferred before they can be unpacked (since white spaces within columns are now meaningful). Fortunately, since each operator in the final line is at the left-most side of each column, the spaces between consecutive operators can be used to infer the column width. Aside from some extra parsing of the input, my solution was the same as Part 1. Solution reached in 33.2 ms.