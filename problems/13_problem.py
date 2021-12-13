"""
Problem 13: Transparent Oragami (folding a grid)
"""

import numpy as np

# Parse file
x = []
y = []
folds = []
with open('13_input.txt', 'r') as f:
    for item in f.readlines():
        line = item.strip().split(',')
        first_element = line[0]
        if first_element.isnumeric():
            x.append(int(line[0]))
            y.append(int(line[1]))
        elif 'fold' in first_element:
            if 'x' in first_element:
                direction = 'x'
            else:
                direction = 'y'

            value = int(first_element.split('=')[1])
            folds.append((direction, value))

f.close()

# Build initial grid (do I care about mins?)
paper = np.zeros(((max(x) + 1), (max(y) + 1)))
for i, j in zip(x, y):
    paper[i, j] = 1


# Plan folds (x - vertical "fold left", y - horizontal "fold up")
def flip_vertical(grid):
    return np.flip(grid, axis=1)


def flip_horizontal(grid):
    return np.flip(grid, axis=0)


def fold(paper, fold):
    direction, location = fold
    if direction == 'x':
        new_paper = paper[:, location] + flip_vertical(paper[:, (location + 1):])
    else:
        new_paper = paper[:location, :] + flip_horizontal(paper[(location + 1):, :])

    return new_paper

new_paper = fold(paper, folds[0])

print(f"After first flip, there are {new_paper.sum()} dots.")
