"""
Problem 7: Treachery of Whales or Crab Helpers
"""

import numpy as np


# input_pos = np.array([int(x) for x in '16,1,2,0,4,2,7,1,2,14'.split(',')])
input_pos = np.array([int(x) for x in open('07_input.txt', 'r').readline().strip().split(',')])


# Part 1: Find the min total "fuel" used to move each crab from initial position to a common position (median but could be mean?)

med_int = round(np.median(input_pos))
fuel_from_med = np.absolute(input_pos - med_int)
sum_fuel_med = np.sum(fuel_from_med)

print(f"Part 1: Fuel needed = {sum_fuel_med}")


# Part 2: Now fuel per move = steps moved. (Moving 3 total steps = 1 + 2 + 3) Find total fuel to move to optimal position.
# Honestly... I don't understand the math, so imma brute force it.

def fuel_for_one_crab(distance_to_move):
    return sum(range(distance_to_move + 1))


def fuel_for_all_crabs(initial_position_array, final_position):
    distance_list = list(np.absolute(initial_position_array - final_position))
    fuel_by_crab = [fuel_for_one_crab(c) for c in distance_list]
    return sum(fuel_by_crab)

min_position = min(input_pos)
max_position = max(input_pos)

all_possible_final_positions = list(range(min_position, max_position + 1))

print(f"Will be testing {len(all_possible_final_positions)} positions. FYI")

fuel_used = [fuel_for_all_crabs(input_pos, p) for p in all_possible_final_positions]

print(f"Part 2: Fuel needed is {min(fuel_used)}")
