"""
Problem 5: Hydrothermal Venture

Puzzle input looks like
341,395 -> 467,395
on each line. These are end points of line segments that should be avoid while traveling the sea floor.
"""

raw_input = open('05_input.txt', 'r').readlines()
input_as_list = [l.split()[::2] for l in raw_input]


# Part 1: Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
class LineSegment:
    # [thing, thing]
    def __init__(self, string_pairs_as_list):
        self.string_pairs = string_pairs_as_list
        self.coord_1 = [int(x) for x in self.string_pairs[0].split(',')]
        self.coord_2 = [int(x) for x in self.string_pairs[1].split(',')]
        self.coord_pair = [self.coord_1, self.coord_2]

    def is_horiz_or_vert(self):
        x1, y1 = self.coord_1
        x2, y2 = self.coord_2
        if x1 == x2 or y1 == y2:
            return True
        else:
            return False

    def line_coords_from_endpoints(self):
        x_diff = self.coord_2[0] - self.coord_1[0]
        y_diff = self.coord_2[1] - self.coord_1[1]
        x_diff_abs = abs(x_diff)
        y_diff_abs = abs(y_diff)

        if x_diff < 0:
            all_x_vals = list(range(self.coord_1[0], self.coord_2[0] - 1, -1))
        else:
            all_x_vals = list(range(self.coord_1[0], self.coord_2[0] + 1))

        if y_diff < 0:
            all_y_vals = list(range(self.coord_1[1], self.coord_2[1] - 1, -1))
        else:
            all_y_vals = list(range(self.coord_1[1], self.coord_2[1] + 1))

        if y_diff == 0:
            y_values = [self.coord_1[1]] * len(all_x_vals)
            return [[x, y] for x, y in zip(all_x_vals, y_values)]
        elif x_diff == 0:
            x_values = [self.coord_1[0]] * len(all_y_vals)
            return [[x, y] for x, y in zip(x_values, all_y_vals)]
        else:
            x_over_y = x_diff_abs / y_diff_abs
            y_over_x = 1 / x_over_y

            check_x_ints = [((x - self.coord_1[0]) * y_over_x).is_integer() for x in all_x_vals]
            check_y_ints = [((y - self.coord_1[1]) * x_over_y).is_integer() for y in all_y_vals]
            x_inds = [i for i, is_int in enumerate(check_x_ints) if is_int]
            y_inds = [j for j, is_int in enumerate(check_y_ints) if is_int]
            x_int_vals = [all_x_vals[i] for i in x_inds]
            y_int_vals = [all_y_vals[j] for j in y_inds]
            return [[x, y] for x, y in zip(x_int_vals, y_int_vals)]


#  Now get coords for all lines that are h or v and collect in dictionary with count of occurrences.
hv_vent_coords = {}

for string_pair in input_as_list:
    segment = LineSegment(string_pair)
    if segment.is_horiz_or_vert():
        segment_coords = segment.line_coords_from_endpoints()
        for coord in segment_coords:
            coord_tup = tuple(coord)
            if coord_tup in hv_vent_coords:
                hv_vent_coords[coord_tup] += 1
            else:
                hv_vent_coords[coord_tup] = 1

coords_appear_at_least_twice = 0
for k, v in hv_vent_coords.items():
    if v > 1:
        coords_appear_at_least_twice += 1

print(f"Part 1: {coords_appear_at_least_twice} coordinates are hit by at least two vent segments.")

# Part 2: Same thing but include diagonals
vent_coords = {}

for string_pair in input_as_list:
    segment = LineSegment(string_pair)
    segment_coords = segment.line_coords_from_endpoints()
    for coord in segment_coords:
        coord_tup = tuple(coord)
        if coord_tup in vent_coords:
            vent_coords[coord_tup] += 1
        else:
            vent_coords[coord_tup] = 1

coords_appear_at_least_twice = 0
for k, v in vent_coords.items():
    if v > 1:
        coords_appear_at_least_twice += 1

print(f"Part 2: {coords_appear_at_least_twice} coordinates are hit by at least two vent segments.")
