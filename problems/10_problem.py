"""
Problem 10: Syntax Correction

Premise: Series of {} [] () <> but the series have errors or are incomplete.
"""

data = open('10_input.txt', 'r').readlines()

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

bracket_pairs = {'{': '}',
                 '[': ']',
                 '(': ')',
                 '<': '>'}


def check_syntax(line):
    line_chars = list(line.strip())
    still_open = [line_chars[0]]
    for i, c in enumerate(line_chars[1:]):
        if c in bracket_pairs:
            still_open.append(c)
        else:
            last_open = still_open[-1]
            if c == bracket_pairs[last_open]:
                still_open.pop()
            else:
                return c

    return ''.join(still_open)


checked_lines = [check_syntax(line) for line in data]
bad_chars = [c for c in checked_lines if len(c) == 1]

print(f"Part 1: Points for illegal characters = {sum([points[c] for c in bad_chars])}")

# Part 2: Complete the incomplete lines.
# This gives what's left to match with closing brackets in the incomplete lines.
# Takes more time to calculate the score than complete the lines...
incomplete_lines = [line for line in checked_lines if len(line) > 1]

inc_pts = {')': 1, ']': 2, '}': 3, '>': 4}


def completetion_points(line, point_map):
    characters_to_complete = [bracket_pairs[c] for c in list(line)[::-1]]
    points = 0
    for c in characters_to_complete:
        points = points * 5 + point_map[c]
    return points


# Calculate scores per line to complete
scores = [completetion_points(l, inc_pts) for l in incomplete_lines]

# Find middle score
scores.sort()
middle_index = int(len(scores) / 2 - 0.5)

print(f"Part 2: Middle score for completed row points = {scores[middle_index]}")


