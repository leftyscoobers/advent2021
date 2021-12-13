"""
Problem 12: Cave Paths (map)

Given links in graph from cave to cave, find all possible paths from start to end.
Upper case (big caves) can be visited more than once, but lower case (small caves) are limited to one visit.
"""

data = [l.strip().split('-') for l in open('12_input.txt', 'r').readlines()]

# Build graph-dict
def add_segments(pair_list, graph_dict):
    """
    Add pairs to graph dict as seg1 -> seg2
    :param pair_list [[l1, l2], [l3, l4]
    :return: graph_dict of form graph_dict[some_point] = [point1, point2, ...]
    """
    for pair in pair_list:
        l1, l2 = pair
        if l1 in graph_dict:
            graph_dict[l1].append(l2)
        else:
            graph_dict[l1] = [l2]

    return graph_dict


segments = {}
for pair in data:
    l1, l2 = pair
    if 'start' not in pair and 'end' not in pair:
        pairs_to_add = [pair, [l2, l1]]
    elif l2 == 'start' or l1 == 'end':
        pairs_to_add = [[l2, l1]]
    else:
        pairs_to_add = [pair]

    add_segments(pairs_to_add, segments)


# Build paths: P1 no double-visits allowed for small aves, P2 double visits allowed for one sm cave per path
small_cave = set([c for pair in data for c in pair if c.islower() and c not in ['start', 'end']])


def is_valid(c, p, double_visit_ok=False):
    if not c.islower():
        return True
    else:
        proposed = p + [c]
        list_of_small_caves = [c for c in proposed if c in small_cave]
        set_of_small_caves = set(list_of_small_caves)
        n_list = len(list_of_small_caves)
        n_set = len(set_of_small_caves)
        if n_list == n_set:
            return True
        elif double_visit_ok and (n_list - n_set) == 1:
            return True
        else:
            return False


def build_paths(segments, double_visit_ok=False):
    parent = 'start'
    children = segments[parent]
    valid_paths = []
    paths = [[parent, child] for child in children]
    while len(paths) > 0:
        new_paths = []
        for p in paths:
            children = segments[p[-1]]
            for c in children:
                proposed = p + [c]
                if c == 'end':
                    valid_paths.append(proposed)
                elif is_valid(c, p, double_visit_ok):
                    new_paths.append(proposed)
                else:
                    pass

        paths = new_paths.copy()

    return valid_paths


print(f"Part 1: Total valid paths through caves = {len(build_paths(segments, double_visit_ok=False))}")
print(f"Part 2: Total valid paths through caves = {len(build_paths(segments, double_visit_ok=True))}")
