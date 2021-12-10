"""
Problem 8 : Seven Segment Search (digital numbers)

Premise - you have a 4-digit display but the segments in the numbers to be displayed are scrambled.
You have noted the patters (left side of | in input) and you have the read-out of displayed sgments (right side of |).

Descramble!
"""

from copy import deepcopy
from itertools import permutations


# Parse input
raw_strings = [l.split('|') for l in open('08_input.txt', 'r').readlines()]

observed_patterns = [p[0].strip().split() for p in raw_strings]
observed_display = [p[1].strip().split() for p in raw_strings]

# Part 1: Find total number of 1, 4, 7, 8, all of which have a unique number of segments.


def is_1478(display_value):
    unique_seg_counts = (2, 3, 4, 7)
    return len(display_value) in unique_seg_counts


def display_count_of_1478(four_dig_display):
    is_easy_digit = [is_1478(d) for d in four_dig_display]
    return sum(is_easy_digit)


easy_values = [display_count_of_1478(four_dig) for four_dig in observed_display]

print(f"Part 1: There are *** {sum(easy_values)} *** 1s, 4s, 7s, or 8s in the input.")

# Part 2: Decode everything, obviously.
# This is a mess and not all that efficient but it works.


def string1_substringof_string2(string_1, string_2):
    # Need this because the order of the digit doesn't matter.
    s1 = set(list(string_1))
    s2 = set(list(string_2))
    return s1.issubset(s2)


decoded = []
for line, display in zip(observed_patterns, observed_display):
    pattern = deepcopy(line)
    decode_line = {}
    for obs in line:
        if is_1478(obs):
            if len(obs) == 2:
                one = obs
                decode_line[obs] = '1'
            elif len(obs) == 3:
                seven = obs
                decode_line[obs] = '7'
            elif len(obs) == 4:
                four = obs
                decode_line[obs] = '4'
            elif len(obs) == 7:
                eight = obs
                decode_line[obs] = '8'
            pattern.remove(obs)

    zero_six_nine = [d for d in pattern if len(d) == 6]
    nine = [d for d in zero_six_nine if string1_substringof_string2(four, d)][0]
    decode_line[nine] = '9'
    zero_six_nine.remove(nine)
    zero = [d for d in zero_six_nine if string1_substringof_string2(seven, d)][0]
    decode_line[zero] = '0'
    zero_six_nine.remove(zero)
    six = zero_six_nine[0]
    decode_line[six] = '6'

    for i in [zero, six, nine]:
        pattern.remove(i)

    for r in pattern:
        if string1_substringof_string2(r, six):
            decode_line[r] = '5'
        elif string1_substringof_string2(r, nine):
            decode_line[r] = '3'
        else:
            decode_line[r] = '2'

    display_nums = []
    for value in display:
        possible_perms = set([''.join(p) for p in permutations(value)])
        digit = [v for k, v in decode_line.items() if k in possible_perms][0]
        display_nums.append(digit)

    decoded.append(int(''.join(display_nums)))

print(f"Part 2: Sum of decoded digits is {sum(decoded)}")
