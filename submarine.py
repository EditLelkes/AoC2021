class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

    def up(self, distance: int):
        # self.depth -= distance
        self.aim -= distance

    def down(self, distance: int):
        # self.depth += distance
        self.aim += distance

    def forward(self, distance: int):
        self.horizontal += distance
        self.depth += (self.aim * distance)

    def current_coordinates_multiplied(self):
        return self.depth * self.horizontal
