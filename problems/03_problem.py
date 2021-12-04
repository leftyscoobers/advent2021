"""
Part 3: Binary Diagnostic

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers
 in the diagnostic report.The epsilon rate is calculated in a similar way; rather than use the most common bit, the
 least common bit from each position is used.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them
together.
"""

import numpy as np


def bin_to_int(bin_string):
    return int(bin_string, 2)


def array_to_string(array):
    return ''.join([str(x) for x in list(array)])


def array_to_int(array):
    as_string = array_to_string(array)
    return bin_to_int(as_string)


# Part 1: What is the power consumption of the submarine?
# Need to read by COLUMN and find max and min occurring number
data = open('03_input.txt', 'r').readlines()

data_to_list = [list(l.strip()) for l in data]

data_array = np.array(data_to_list).astype(int)
summed_cols = data_array.sum(axis=0)
mx_array = (summed_cols > len(data)/2).astype(int)
mn_array = (summed_cols < len(data)/2).astype(int)

print(f"Part 1: Max in binary * min in binary = {array_to_int(mx_array) * array_to_int(mn_array)} .")


def filter_values(array, filter_to_max=True):
    half = len(array) / 2
    filtered_array = array.copy()
    col_index = 0
    while filtered_array.shape[0] > 1:
        col_values = filtered_array[:, col_index]
        summed = col_values.sum()
        greater_than_half = summed > half # say this is TRUE b/c sum is 560 then min = 0 and max = 1
        if filter_to_max:
            if greater_than_half or summed == half:
                keepers = 1
            else:
                keepers = 0
        else:
            if greater_than_half or summed == half:
                keepers = 0
            else:
                keepers = 1
        filtered_array = filtered_array[col_values == keepers]
        half = len(filtered_array) / 2
        col_index += 1

    return filtered_array[0]


mx = filter_values(data_array, filter_to_max=True)
mn = filter_values(data_array, filter_to_max=False)

print(f"Part 2: {array_to_int(mx) * array_to_int(mn)}") # 4194295 too low
