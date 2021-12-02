"""
Problem 01
"""

# How many measurements are larger than the previous measurement?
data = [int(x.strip()) for x in open("01_input.txt", 'r').readlines()]


def is_bigger(data):
    return [data[i+1] > data[i] for i in range(len(data)-1)]


print(f"PART 1 - Numbers greater than the previous number: {sum(is_bigger(data))}")

#Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
three_sums = [sum(data[i:(i+3)]) for i in range(len(data)-2)]

print(f"PART 2 - Sums of 3 greater than the previous set: {sum(is_bigger(three_sums))}")
