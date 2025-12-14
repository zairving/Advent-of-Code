# Day 1

## Part 1

Given a range of numbers, check for numbers with repeated digits (e.g., 11, 123123, etc.). Solution: iterate through ranges, split numbers in half, and check that both halves are equal. Only need to check numbers with an even number of digits. Not the fastest, but fast enough. Solution reached in 835.9 ms.

## Part 2

Now check if any digits repeat (e.g., 111, 121212, etc.). Now includes numbers with an odd number of digits. Solution: check for repeated digits, starting with 1 digit up to half the number of digits in the given number. Quite slow, but workable. Solution reached in 4.6 s.