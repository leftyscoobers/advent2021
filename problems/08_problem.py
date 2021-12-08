"""
Problem 8 : Seven Segment Search (digital numbers)

Premise - you have a 4-digit display but the segments in the numbers to be displayed are scrambled.
You have noted the patters (left side of | in input) and you have the read-out of displayed sgments (right side of |).

Descramble!
"""

# Parse input
raw_strings = [l.split('|') for l in open('08_test.txt', 'r').readlines()]
# raw_strings = [l.split('|') for l in open('08_input.txt', 'r').readlines()]

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
# Let's start over.

def in_string_a_but_not_b(string_a, string_b):
    set_a = set(list(string_a))
    set_b = set(list(string_b))
    return list(set_a - set_b)


# Segment map is: top (0), middle (1), bottom (2), top left (3), bottom left (4), top right (5), bottom right (6)
# Now map digits to segments:
digits_to_segments = {0: (0, 2, 3, 4, 5, 6),
                      1: (5, 6),
                      2: (0, 5, 1, 4, 2),
                      3: (0, 5, 1, 6, 2),
                      4: (3, 1, 5, 6),
                      5: (0, 3, 1, 6, 2),
                      6: (0, 3, 4, 2, 6, 1),
                      7: (0, 5, 6),
                      8: (0, 1, 2, 3, 4, 5, 6),
                      9: (2, 6, 5, 0, 3, 1)}

test_line = observed_patterns[0]
decode_line = {}
for obs in test_line:
    if len(obs) == 2:
        decode_line[1] = obs
    elif len(obs) == 3:
        decode_line[7] = obs
    elif len(obs) == 4:
        decode_line[4] = obs
    elif len(obs) == 7:
        decode_line[8] = obs

segment_map = [''] * 7
segment_map[0] = in_string_a_but_not_b(decode_line[7], decode_line[1])[0]
