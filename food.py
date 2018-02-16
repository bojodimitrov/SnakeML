import random


class Food:
    def __init__(self, free_spaces):
        location = random.randint(0, len(free_spaces))
        self.location_x = free_spaces[location][0]
        self.location_y = free_spaces[location][1]

    def get_location(self):
        return [self.location_x, self.location_y]
