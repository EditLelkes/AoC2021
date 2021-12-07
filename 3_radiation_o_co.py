from typing import List


def to_decimal(binary: int) -> int:
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal += dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def get_key(current_binary_list: List, radiation_type: str, analysed_position_index: int) -> str:
    ones_count, zeros_count = 0, 0
    a, b = '1', '0'
    if radiation_type == 'epsilon':
        a, b = '0', '1'

    for binary_num in current_binary_list:
        if binary_num[analysed_position_index] == '1':
            ones_count += 1
        else:
            zeros_count += 1

    if ones_count >= zeros_count:
        key = a
    else:
        key = b
    return key


def get_attribute(input_data_list: List, radiation_name: str) -> int:
    my_index = 0
    my_data_list = input_data_list
    while len(my_data_list) != 1:
        key_number = get_key(my_data_list, radiation_name, my_index)
        for i in range(len(my_data_list)):
            if key_number != my_data_list[i][my_index]:
                my_data_list[i] = 0
        my_data_list = list(filter(lambda num: num != 0, my_data_list))
        my_index += 1
    return to_decimal(int(my_data_list[0]))


with open('input.txt', 'r') as reader:
    data_list = []
    for line in reader:
        stripped_line = line.strip()
        data_list.append(stripped_line)

data_list_copy = data_list.copy()

oxygen_generator = get_attribute(data_list, 'gamma')
co2_scrubber = get_attribute(data_list_copy, 'epsilon')
print(oxygen_generator * co2_scrubber)

# 4375225
