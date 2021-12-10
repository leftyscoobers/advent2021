"""
Problem 9: Smoke Basin

Premise - find local mins in a grid to avoid during navigation
"""

import numpy as np
from copy import deepcopy

raw_data = open('09_input.txt', 'r').readlines()

split_to_list = [list(l.strip()) for l in raw_data]
ocean_floor = np.array(split_to_list).astype(int)

# Part 1: Find local mins (value is lower than all surrounding cells)
def pad(grid, dimensions=2, pad_value=0):
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


floor_padded = pad(deepcopy(ocean_floor), pad_value=9)

# Start less elegantly
min_locations = []
smoke_values = []
n_row, n_col = floor_padded.shape
for i in range(1, n_row):
    for j in range(1, n_col):
        coord = [i, j]
        center_value = floor_padded[i, j]
        adjacent_cells = floor_padded[(i-1):(i+2), (j-1):(j+2)]
        min_val = adjacent_cells.min()
        if min_val == center_value:
            min_locations.append(coord)
            smoke_values.append(1 + center_value)

print(f"Part 1: Total smoke risk is {sum(smoke_values)}")

# Part 2: Find "basins", which are basically following the low point outwards until you hit 9s up, down, left, or right.
# Find the three largest basins and multiply their values for the solution
# Sooooo messy.

def find_basin_neighbors(matrix, ind):
    x, y = ind
    if matrix[x, y] == 9:
        return []
    else:
        top = [[x, y + 1], matrix[x, y + 1]]
        bottom = [[x, y - 1], matrix[x, y - 1]]
        left = [[x - 1, y], matrix[x - 1, y]]
        right = [[x + 1, y], matrix[x + 1, y]]

        return [tuple(i) for i, v in [top, bottom, left, right] if v < 9]


basin = {}

for m in min_locations:
    x, y = m
    this_basin = set([tuple(m)])
    current_basin_size = len(this_basin)
    neighbors = find_basin_neighbors(floor_padded, m)
    [this_basin.update([n]) for n in neighbors]
    new_basin_size = len(this_basin)
    while current_basin_size < new_basin_size:
        current_basin_size = new_basin_size
        # Inefficient - will recheck previous neighbors but this problem is small enough to handle it
        for n in deepcopy(this_basin):
            new_neighbors = find_basin_neighbors(floor_padded, n)
            [this_basin.add(new) for new in new_neighbors]
        new_basin_size = len(this_basin)
    basin[tuple(m)] = this_basin


basin_sizes = [len(v) for k, v in basin.items()]
basin_sizes.sort(reverse=True)

print(f"Part 2: Top 3 basins multiplied - {basin_sizes[0] * basin_sizes[1] * basin_sizes[2]}")

