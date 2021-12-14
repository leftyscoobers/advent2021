"""
Problem 13: Transparent Oragami (folding a grid)
"""

import numpy as np

# Parse file
x = [] # cols
y = [] # rows
folds = []
with open('13_input.txt', 'r') as f:
# with open('13_test.txt', 'r') as f:
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
paper = np.zeros(((max(y) + 1), (max(x) + 1), ))
for i, j in zip(x, y):
    paper[j, i] = 1


# Plan folds (x - vertical "fold left", y - horizontal "fold up")
def flip_vertical(grid):
    return np.flip(grid, axis=1)


def flip_horizontal(grid):
    return np.flip(grid, axis=0)


def fold(paper, fold):
    direction, location = fold
    if direction == 'x':
        new_paper = paper[:, :location] + flip_vertical(paper[:, (location + 1):])
    else:
        new_paper = paper[:location, :] + flip_horizontal(paper[(location + 1):, :])

    return new_paper


new_paper = fold(paper, folds[0])
print(f"After first flip, there are {(new_paper > 0).sum()} dots.")

# Finish folding and then get the 8 capital letter code from the out put (?)
paper_to_fold = paper.copy()
for i, f in enumerate(folds):
    print(f"Fold {i} : {f}")
    new_paper = fold(paper_to_fold, f)
    paper_to_fold = new_paper.copy()


# Overwrite all > 0 values with 1s
paper_to_fold[paper_to_fold > 0] = 1

# Print to file to view - opened in GSheets and colored cells > 1 to read
np.savetxt('13_output.txt', paper_to_fold, delimiter=' ', fmt='%1.0f') # RZKZLPGH
