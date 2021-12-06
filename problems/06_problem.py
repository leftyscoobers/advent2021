"""
Problem 6: Lantern Fish Exponential Growth

Lantern fish take 7 days to create 1 baby. Each baby takes 2 days to mature before beginning 7 day replication loop.

Assume they never die.
"""

from copy import deepcopy

# input_list = [int(i) for i in '3,4,3,1,2'.split(',')]
input_list = [int(i) for i in open('06_input.py', 'r').readlines()[0].split(',')]

# Collect into counts at each day-stage.
possible_initial_day_values = list(range(7))
initial_counts = [input_list.count(d) for d in possible_initial_day_values] + [0, 0]


def spawn_fish(intial_counts, n_days):
    current_counts = deepcopy(initial_counts)
    for d in range(n_days):
        fish_that_spawn = current_counts[0]
        current_counts = current_counts[1:] + [fish_that_spawn]
        current_counts[6] += fish_that_spawn

    return  current_counts


# Part 1: Spawn for 80 days and report total lanternfish
print(f"Total fish after eighty days: {sum(spawn_fish(initial_counts, 80))}")


# Part 2: Spawn for 256 days and report total lanternfish
print(f"Total fish after 256 days: {sum(spawn_fish(initial_counts, 256))}")
