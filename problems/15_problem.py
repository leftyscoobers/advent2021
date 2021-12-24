"""
Problem 15: Navigating Through a Cave

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally.
Find path with lowest total risk (input is risk value for each coordinate).

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

import numpy as np

# Modify grid as we go out one coord at a time, updating 'least risky path".
# Note that we don't actually need to record the shortest path - just the risk value

raw_risk = [list(l.strip()) for l in open('15_input.txt', 'r').readlines()]
risk_map = np.array(raw_risk).astype(int)


def find_least_risky_path(risk_map):
    dx, dy = risk_map.shape
    start = (0, 0)
    end = ((dx - 1), (dy - 1))

    visited = set()
    risk_total = np.zeros((dx, dy)) + 1e10  # set to some initially huge number
    risk_total[start] = 0

    node_options = {start: 0}
    cheapest = (0, start)
    while node_options:
        risk_so_far, coord = cheapest
        if coord == end:
            break
        r, c = coord
        visited.add(coord)
        del node_options[coord]
        for n_r, n_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (n_r, n_c) in visited:
                continue
            if not (0 <= n_r < dx and 0 <= n_c < dy):
                continue

            new_risk = risk_so_far + risk_map[(n_r, n_c)]
            if new_risk < risk_total[(n_r, n_c)]:
                risk_total[(n_r, n_c)] = new_risk

            node_options[(n_r, n_c)] = risk_total[(n_r, n_c)]

        # Sort so we try lowest risk first
        min_risk = min(node_options.values())
        cheapest = [(r, coord) for coord, r in node_options.items() if r == min_risk][0]

    return risk_total[end]


print(f"Part 1: Lowest risk = {find_least_risky_path(risk_map)}")


# Part 2: Now make 5 x 5 tile of the above but every translation right or down increases risk by 1
# (anything over 9 starts over at 1)

def make_square_grid(original_tile, dimensions):
    new_horiz = original_tile.copy()
    for d in range(1, dimensions):
        new_horiz = np.concatenate((new_horiz, original_tile + d), axis=1)

    new_tile = new_horiz.copy()
    for d in range(1, dimensions):
        new_tile = np.concatenate((new_tile, new_horiz + d), axis=0)

    new_tile = new_tile % 9
    new_tile[new_tile == 0] = 9
    return new_tile


print(f"Part 2: Lowest risk from new tile-grid = {find_least_risky_path(make_square_grid(risk_map, 5))}")
