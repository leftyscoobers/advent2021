"""
Problem 7: Treachery of Whales or Crab Helpers
"""

import numpy as np


input_pos = np.array([int(x) for x in '16,1,2,0,4,2,7,1,2,14'.split(',')])
# input_pos = np.array([int(x) for x in open('07_input.txt', 'r').readline().strip().split(',')])


# Part 1: Find the min total "fuel" used to move each crab from initial position to a common position (median but could be mean?)

med_int = round(np.median(input_pos))
fuel_from_med = np.absolute(input_pos - med_int)
sum_fuel_med = np.sum(fuel_from_med)

print(f"Part 1: Fuel needed = {sum_fuel_med}")


# Part 2: Now fuel per move = steps moved. (Moving 3 total steps = 1 + 2 + 3) Find total fuel to move to optimal position.


