import random
from world_configuration import FOOD_PIECES


class Food:
    def __init__(self, free_spaces):
        self.locations = []
        for _ in range(FOOD_PIECES):
            location = random.randint(0, len(free_spaces)-1)
            self.locations.append(
                [free_spaces[location][0], free_spaces[location][1]])
            del free_spaces[location]

    def get_locations(self):
        return self.locations

    def respawn_piece(self, free_spaces, piece_location):
        self.locations.remove(piece_location)
        new_location = random.randint(0, len(free_spaces)-1)
        self.locations.append(
            [free_spaces[new_location][0], free_spaces[new_location][1]])
