from typing import List
from submarine import Submarine


# day 1
def get_day_one_input(filename: str):
    depths_list = []
    with open(filename, 'r') as reader:
        for line in reader:
            depths_list.append(int(line.strip()))
    return depths_list


# day 1
def count_deeper(depths: List) -> int:
    counter = 0
    current_depth = depths[0]
    for depth in depths[1:]:
        if depth > current_depth:
            counter += 1
        current_depth = depth
    return counter


# day 1
def count_deeper_triplets(depths: List) -> int:
    counter = 0
    current_depth = sum(depths[0:3])
    for i in range(1, len(depths) - 2):
        depth = sum(depths[i:i + 3])
        if depth > current_depth:
            counter += 1
        current_depth = depth
    return counter


# day 2
def get_day_two_input(filename: str, my_submarine: Submarine):
    with open(filename, 'r') as reader:
        for line in reader:
            data = line.strip().split()
            if data[0] == 'down':
                my_submarine.down(int(data[1]))
            if data[0] == 'up':
                my_submarine.up(int(data[1]))
            if data[0] == 'forward':
                my_submarine.forward(int(data[1]))


my_sub = Submarine()
get_day_two_input('input2.txt', my_sub)
print(my_sub.current_coordinates_multiplied())
