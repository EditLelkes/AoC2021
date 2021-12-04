from typing import List


class BingoTable:
    def __init__(self, table: List):
        self.table = table
        self.is_done = False

    def get_columns(self):
        verticals = []
        vertical = []
        for i in range(len(self.table[0])):
            for row in self.table:
                vertical.append(row[i])
            verticals.append(vertical)
            vertical = []
        self.table.extend(verticals)

    def check_hit(self, draw_num: str):
        if self.is_done:
            return False
        for line in self.table:
            for i in range(len(line)):
                if draw_num == line[i]:
                    line[i] = 'X'

    def check_bingo(self) -> bool:
        if self.is_done:
            return False
        for line in self.table:
            if all(num == 'X' for num in line):
                self.is_done = True
                return True

    def get_score(self) -> int:
        sum_of_remaining_numbers = 0
        for line in self.table:
            for element in line:
                if element != 'X':
                    sum_of_remaining_numbers += int(element)
        return sum_of_remaining_numbers // 2
