from typing import List
from bingo_table import BingoTable

with open('input.txt', 'r') as reader:
    lines = reader.readlines()

bingo_draw = lines[0].strip().split(',')
lines.pop(0)
lines.pop(0)

bingo_tables = []
table = []
for line in lines:
    if line == '\n':
        bingo_tables.append(BingoTable(table))
        table = []
    else:
        table.append(line.split())

for bingo_table in bingo_tables:
    bingo_table.get_columns()


def play_bingo(bingo_tables_list: List, list_of_drawn_numbers: List):
    table_scores = []
    for number in list_of_drawn_numbers:
        for current_bingo_table in bingo_tables_list:
            current_bingo_table.check_hit(number)
            if current_bingo_table.check_bingo():
                table_scores.append(current_bingo_table.get_score() * int(number))
    print(table_scores[0])
    print(table_scores[-1])


play_bingo(bingo_tables, bingo_draw)
