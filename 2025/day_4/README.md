# Day 1

## Part 1

Given a grid of '@' and '.' symbols, find how many '@' symbols have fewer than four adjacent '@' symbols. Solution: iterate through grid rows and columns and check how many adjacent '@' symbols each '@' symbol has. Be careful not to go over the edges of the grid or count the grid point itself. Solution reached in 32.3 ms.

## Part 2

Now accessible rolls can be removed. I therefore repeated my solution to part 1, but now restarted the search from the beginning each time an accessible roll was found. I chose to restart the search from the beginning each time since a roll removed on, say, line 3 may make a roll on line 2 (or a previous roll on line 3) accessible. It would be quicker to check if removing a roll makes any adjacent rolls accessible instead of starting a grid search again, but in this case it was quicker to write this solution and tolerate the longer run time than to write a more elegant solution that will run quicker. Solution reached in 14.8 s.