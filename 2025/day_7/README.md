# Day 7

## Part 1

Propagate a beam downwards through a manifold. The manifold contains beam splitters ('^'), that split a single beam into two beams: one to the left of the splitter and one to the right. Both beams then propagate vertically downwards. We need to find the number of times the beam is split. Solution: propagate the beam downwards, track the coordinates of splitters to prevent the same splitter from splitting more than one beam, and propagate the split beams (making sure not to propagate more than one beam from a given position). Solution reached in 47.5 ms.

## Part 2

Now we need to track how many unique paths a beam could take through the manifold. I knew memoization would be important in this case, and so I re-wrote my solution from Part 1 to propagate beams recursively instead of iteratively. For fun, I decided to write my own memoization decorator since I've never written a custom decorator before. Solution reached in 2.8 ms.