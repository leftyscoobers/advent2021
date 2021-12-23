"""
Problem 15: Navigating Through a Cave

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally.
Find path with lowest total risk (input is risk value for each coordinate).

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""

import numpy as np

raw_risk = [list(l.strip()) for l in open('15_input.txt', 'r').readlines()]
risk_map = np.array(raw_risk).astype(int)
dx, dy = risk_map.shape
end = ((dx - 1), (dy - 1))


# Modify grid as we go out one coord at a time, updating 'least risky path".
# Note that we don't actually need to record the shortest path
visited = set()
risk_total = np.zeros((dx, dy)) + 1e10  # set to some initially huge number
risk_total[(0, 0)] = 0  # start point risk is 0

continue_from = {(0, 0)}
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
    print(f"Length of continue from: {len(continue_from)}")
    print(f"visited so far: {len(visited)}")

print(f"Risk at end point: {risk_total[end]}")  # 508 (currently outputs 510)
