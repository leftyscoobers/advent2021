"""
PROBLEM 2
"""

data = [l.strip().split(' ') for l in open("02_input.txt", 'r').readlines()]

# Part 1: What do you get if you multiply your final horizontal position by your final depth?
def go_sub(directions, start=[0, 0]):
    position = start
    for d in directions:
        action = d[0]
        distance = int(d[1])
        if action == 'forward':
            new_position = [position[0] + distance, position[1]]
        elif action == 'up':
            new_position = [position[0], position[1] - distance]
        else:
            new_position = [position[0], position[1] + distance]
        position = new_position
    return position

part_1 = go_sub(data)w

print(f"Part 1: Product of final position coords is {part_1[0] * part_1[1]}")

# Part 2: Same question but this time up and down change "aim" and forward increases x but also depth by aim * unit given.
# Previous function doesn't help at all so copy and adjust...
def go_sub2(directions):
    x = 0
    y = 0
    aim = 0
    for d in directions:
        action = d[0]
        distance = int(d[1])
        if action == 'forward':
            x += distance
            y += distance * aim
        elif action == 'up':
            aim -= distance
        else:
            aim += distance

    return [x, y]


part_2 = go_sub2(data)

print(f"Part 2: Product of final position coords is {part_2[0] * part_2[1]}")
