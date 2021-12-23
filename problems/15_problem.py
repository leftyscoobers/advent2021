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
    risk_total[end] = 0  # start point risk is 0, but we work backwards from the intended end

    continue_from = {end}
    while len(continue_from) > 0:
        new_continue = set()
        for coord in continue_from:
            r, c = coord
            visited.add(coord)
            for n_r, n_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (n_r, n_c) in visited:
                    continue
                if not (0 <= n_r < dx and 0 <= n_c < dy):
                    continue

                risk_at_neighbor = risk_total[(n_r, n_c)]
                new_risk = risk_total[coord] + risk_map[(n_r, n_c)]
                if new_risk < risk_at_neighbor:
                    risk_total[(n_r, n_c)] = new_risk

                new_continue.add((n_r, n_c))
        continue_from = new_continue

    return risk_total[start]


print(f"Part 1: Lowest risk = {find_least_risky_path(risk_map)}")  # Calculate this backwards from the end to the start


# Part 2: Now make 5 x 5 tile of the above but every translation right or down increases risk by 1
# (anything over 9 starts over at 1)


