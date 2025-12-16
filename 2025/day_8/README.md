# Day 8

## Part 1

Given a list of coordinates, connect the closest 1000 pairs of nodes. Connected nodes form circuits. Answer is the product of the lengths of the three longest circuits. Computing a distance matrix was straightforward using the `scipy.spatial.distance.cdist()` function. It was then a matter of finding the smallest non-zero distance, getting the corresponding nodes, and then connecting them. One oversight I made initially was that when a pair of nodes are connected, both nodes may be part of separate circuits, and so both circuits need to be combined. Once circuits have been formed/combined, sort circuits by length and then multiple the lengths of the three longest circuits. Solution reached in 479.8 ms.

## Part 2

Now connect nodes until all nodes form a single large circuit. Answer is the product of the x coordinates of the final two nodes that connect. Solution was pretty similar to Part 1, just allowing to iterate until all nodes are in a single circuit. Solution reached in 8.5 s.