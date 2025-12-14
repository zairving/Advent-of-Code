# Day 1

## Part 1

Turn a circular dial in a particular direction a given number of times. Pretty straightforward using Python's modulo operator. Solution reached in 5.4 ms.

## Part 2

Now need to track how many times 0 has been passed as the dial turns. My solution uses integer division by 100, but this doesn't account for the case of starting on a positive number and ending on a negative number above -100. There is likely a more elegant solution that accounts for this special case, but this was the first solution that came to mind and it worked. Solution reached in 4.2 ms.