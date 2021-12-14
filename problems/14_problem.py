"""
Problem 14: Polymerization - string insertion
"""

raw_data = open('14_test.txt', 'r').readlines()
start = raw_data[0].strip()
rules = [] # Insertion process is ordered = no dict
for line in raw_data[2:]:
    pair, arrow, insert_element = line.strip().split()
    rules.append((pair, insert_element))


def insert_element_in_pair(rule_tuple):
    pair, insert_element = rule_tuple
    return ''.join([pair[0], insert_element, pair[1]])


def insert_in_polymer(polymer, rule_tuple, forbidden_indices):
    replacement = insert_element_in_pair(rule_tuple)
    first_indices_of_possible_pairs = [i for i in range(0, len(polymer)) if polymer[i:(i+2)] == rule_tuple[0]]
    insert_indices = [fi + ind + 1 for ind, fi in enumerate(first_indices_of_possible_pairs)] # This is only if you insert all but you won't. fix
    updated_list = []
    for i, v in enumerated():

    updated_polymer = [polymer.replace(rule_tuple[0], replacement)] # update this line to avoid forbidden
    return (insert_indices, updated_polymer)


# Next step - update so in each step, no inserted elements are considered for any other rules
def perform_insertions(polymer, rule_set, n_steps):
    p = polymer
    for s in range(n_steps):
        indices_of_inserted_letters = []
        for r in rule_set:
            ind, p = insert_in_polymer(p, r)
            [indices_of_inserted_letters.append(i) for i in ind]
    return p


p1_polymer = perform_insertions(start, rules, 1)
print(p1_polymer)

counts = [p1_polymer.count(l) for l in set(p1_polymer)]
counts.sort()

print(f"Part 1: max occur - min occur = {counts[-1] - counts[0]}")

