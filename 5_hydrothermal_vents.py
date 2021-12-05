from typing import List


def create_hydrothermal_vents_coordinates(input_file_name: str) -> List:
    with open(input_file_name, 'r') as reader:
        vents_coordinates = []
        for line in reader:
            stripped_line = line.strip().split(' -> ')
            a_x = int(stripped_line[0].split(',')[0])
            b_x = int(stripped_line[1].split(',')[0])
            a_y = int(stripped_line[0].split(',')[1])
            b_y = int(stripped_line[1].split(',')[1])
            if a_x == b_x:
                for y in range(min(a_y, b_y), max(a_y, b_y) + 1):
                    vents_coordinates.append((a_x, y))
            elif a_y == b_y:
                for x in range(min(a_x, b_x), max(a_x, b_x) + 1):
                    vents_coordinates.append((x, a_y))
            # addition for the second part
            else:
                x_dir, y_dir = 1, 1
                if a_x - b_x > 0:
                    x_dir = -1
                if a_y - b_y > 0:
                    y_dir = -1
                for i in range(abs(b_x - a_x) + 1):
                    vents_coordinates.append((a_x + i * x_dir, a_y + i * y_dir))
        return vents_coordinates


def count_high_risk_coordinates(hydrothermal_vent_coordinates):
    counts = {}
    for coordinates in hydrothermal_vent_coordinates:
        counts[coordinates] = counts.get(coordinates, 0) + 1

    high_risk_coordinates = 0
    for value in counts.values():
        if value > 1:
            high_risk_coordinates += 1
    return high_risk_coordinates

print(count_high_risk_coordinates(create_hydrothermal_vents_coordinates('input.txt')))
