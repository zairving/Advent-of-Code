# Day 9

## Part 1

Given a list of coordinates, find the largest possible rectangle whose opposite corners are given by a pair of said coordinates. Solution: for each coordinate, compute the areas of all the rectangles that coordinate could make, and find the largest area. Really straightforward and efficient using `numpy`. Solution reached in 67.5 ms.

## Part 2

Now rectangles must fall within the perimeter laid out by the given coordinates. This is a significantly more difficult problem to solve. Solution: similar to Part 1 but now using `shapely` to define the perimeter and each rectangle, and the `contains()` method to check if rectangles fall within the perimeter. Solution reached in 4.0 s.