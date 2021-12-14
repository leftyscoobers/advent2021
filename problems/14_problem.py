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


def insert_in_polymer(polymer, rule_tuple):
    replacement = insert_element_in_pair(rule_tuple)
    return polymer.replace(rule_tuple[0], replacement)


# Next step - update so in each step, no inserted elements are considered for any other rules
def perform_insertions(polymer, rule_set, n_steps):
    p = polymer
    for s in range(n_steps):
        for r in rule_set:
            p = insert_in_polymer(p, r)
    return p


p1_polymer = perform_insertions(start, rules, 1)
print(p1_polymer)

counts = [p1_polymer.count(l) for l in set(p1_polymer)]
counts.sort()

print(f"Part 1: max occur - min occur = {counts[-1] - counts[0]}")

