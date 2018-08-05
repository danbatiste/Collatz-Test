# Collatz-Test
Functions used to experiment with the Collatz conjecture.

This program has a couple functions. The two main ones are hs() and invhs().

hs() takes a starting number* and finds out how many numbers are in its sequence as it gets iterated through the Collatz function. For example, hs(5) would return 6. (5, 16, 8, 4, 2, 1)

invhs() does exactly the opposite. It takes a number, say 6, and returns the first starting number* which has that many steps in its sequence. invhs(6) returns 5. (This isn't a true inverse, because it isn't bijective, aka one-to-one.)
