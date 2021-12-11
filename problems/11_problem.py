"""
Problem 11: Flashing Dumbo Octopuses

Premise: Octopuses are in a grid, each with an energy level. When level > 9, flash. Flash adds 1 pt to adjacent
octopuses, in the same step, which may, in turn, also flash.
"""

import numpy as np
from copy import deepcopy

string_data = [list(l.strip()) for l in open('11_input.txt').readlines()]

initial_oct_energy = np.array(string_data).astype(int)

# Copy matrix pad function from P9 (would be better to make util)
def pad(grid, pad_value=0):
    gs = grid.shape
    g0 = [d + 2 for d in gs]
    grid_pad = np.zeros(g0)
    slices = [slice(1, d+1) for d in gs]
    grid_pad[tuple(slices)] += grid
    if pad_value != 0:
        grid_pad[0, :] = pad_value
        grid_pad[(gs[0] + 1), :] = pad_value
        grid_pad[:, 0] = pad_value
        grid_pad[:, (gs[1] + 1)]= pad_value
    return grid_pad


def flash_neighbors(octo_grid, flash_octo_index, flash_marker=1000):
    x, y = flash_octo_index
    octo_grid[(x-1):(x+2), (y-1):(y+2)] += 1
    octo_grid[x, y] = flash_marker
    return octo_grid


# Pad array with values that won't turn into flashes after nearbly octopuses flash in a step
flash_array = pad(deepcopy(initial_oct_energy), pad_value=-1000)
flashes = 0
synced = False
step = 0
while not synced:
    step += 1
    flash_array += 1
    flash_points = np.where(np.logical_and(flash_array > 9, flash_array < 1000))
    rows, cols = flash_points
    while len(rows) > 0:
        i = rows[0]
        j = cols[0]
        flashes += 1
        flash_neighbors(flash_array, [i, j])
        flash_points = np.where(np.logical_and(flash_array > 9, flash_array < 1000))
        rows, cols = flash_points

    if step == 100:
        print(f"Part 1: Total flashes = {flashes}")

    if (flash_array[1:(flash_array.shape[0] - 1), 1:(flash_array.shape[1] - 1)] >= 1000).all():
        print(f"Part 2: all synced up at step {step}")
        synced = True

    flash_array[flash_array >= 1000] = 0 # Reset flashed octos after step is complete









