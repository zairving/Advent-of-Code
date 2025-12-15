# Day 5

## Part 1

Given a list of values and ranges, find how many of the values fall within the given ranges. Solution: interate through each ingredient value and see if it's value falls within the limits of any of the given ranges. Solution reached in 17.3 ms.

## Part 2

Now we have to calculate how many valid values there are within the given ranges. The ranges are too large to calculate explicitly. Solution: clip the ranges to prevent overlap; the number of allowed values is then the sum of the difference between the range limits (+ 1 since ranges are *inclusive*). Solution reached in 3.6 ms. 