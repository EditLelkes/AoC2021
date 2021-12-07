import time
from typing import List

with open('7input.txt') as reader:
    initial_state = reader.readline().strip().split(',')

ints = sorted([int(i) for i in initial_state])
ints_middle = ints[len(ints) // 2]
ints_mean = sum(ints) // len(ints)


def check_fuel_needed(positions_list: List, current_position: int) -> int:
    fuel_first, fuel_second = 0, 0
    for number in positions_list:
        diff = abs(current_position - number)
        fuel_first += diff
        for x in range(1, diff + 1):
            fuel_second += x
    return fuel_second


def minimal_fuel(positions_list: List, middle_position: int) -> int:
    fuel_needed = check_fuel_needed(positions_list, middle_position)
    for i in range(1, len(ints) // 2):
        right_side = check_fuel_needed(positions_list, middle_position + i)
        left_side = check_fuel_needed(positions_list, middle_position - i)
        if min(right_side, left_side) >= fuel_needed:
            return fuel_needed
        else:
            fuel_needed = min(right_side, left_side)


# First task
start = time.time()
print(minimal_fuel(ints, ints_middle))
end = time.time()
print(end - start)
# 0.03690004348754883s

start = time.time()
print(minimal_fuel(ints, ints_mean))
end = time.time()
print(end - start)
# 2.857393741607666

# Second task
start = time.time()
print(minimal_fuel(ints, ints_middle))
end = time.time()
print(end - start)
# 2.8571105003356934

start = time.time()
print(minimal_fuel(ints, ints_mean))
end = time.time()
print(end - start)
# 0.03789854049682617
