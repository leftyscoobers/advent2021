"""
Problem 14: Polymerization - string insertion

Note: The question asks for total number of pairs in a long string (how many "CH"s and so on) - order does not matter.
"""

raw_data = open('14_input.txt', 'r').readlines()
start = raw_data[0].strip()
rules = {}
for line in raw_data[2:]:
    pair, arrow, insert_element = line.strip().split()
    rules[pair] = insert_element


def split_pair(pair):
    insert_letter = rules[pair]
    new_pair1 = pair[0] + insert_letter
    new_pair2 = insert_letter + pair[1]
    return new_pair1, new_pair2


def do_steps(steps):
    initial_pairs = [start[i:(i + 2)] for i in range(len(start) - 1)]
    pairs_counts = dict([(pair, start.count(pair)) for pair in initial_pairs])

    for step in range(steps):
        new_pairs = {}
        for p, ct in pairs_counts.items():
            split_pairs = split_pair(p)
            for np in split_pairs:
                if np in new_pairs:
                    new_pairs[np] += 1 * ct
                else:
                    new_pairs[np] = ct

        pairs_counts = new_pairs.copy()

    # Every letter is double-counted in dict except first and last:
    letter_set = set(''.join(pairs_counts.keys()))
    start_letter = start[0]
    end_letter = start[1]
    pairs_tuples = []
    for l in letter_set:
        l_count = 0
        for pair, ct in pairs_counts.items():
            if l in pair:
                l_count += ct
                if pair[0] == pair[1]:
                    l_count += ct # Accounts for double letters like BB
        if l in (start_letter, end_letter):
            if start_letter == end_letter:
                l_real = (l_count - 2) / 2 + 2
            else:
                l_real = (l_count - 1) / 2 + 1
        else:
            l_real = l_count / 2
        pairs_tuples.append((l, l_real))

    pairs_tuples.sort(key=lambda x: x[1])
    max_count = pairs_tuples[-1][1]
    min_count = pairs_tuples[0][1]
    return max_count - min_count

print(f"Part 1: 10 steps = {do_steps(10)}") # 2027
print(f"Part 2: 40 steps = {do_steps(40)}") # 2265039461737


