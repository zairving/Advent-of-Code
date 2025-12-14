# Day 1

## Part 1

Given a long integer (e.g., 34584375873), find the largest possible two-digit integer. The numbers cannot be rearranged. Solution: split long integer into a list of integers, find the first maximum in the list *excluding the final number*, then find the maxmimum value in the remaining list starting from the first maximum through to the end of the list. Solution reached in 3.4 ms.

## Part 2

Now the maximum number must be twelve digits instead of two. Solution: very similar to part 1 but now using a for loop to exclude the last `12 - i` elements of the list, where `i` is the loop counter. Solution reached in 6 ms.