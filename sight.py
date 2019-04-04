from collections import deque
import utils
from world_configuration import DIMENSIONS, SQUARE_SIZE, INTERSQUARE_SPACE


class Sight:
    r"""
    Sight is vector of 16 values:
        1) First eight coordinates are distance to walls or body
        1) Second eight coordinates are distance to food
    Coordinates are in Manhattan distance
    The vector octets follow next pattern:
        \(x7)   |(x0) /(x1)
        --(x6)  *    --(x2)
        /(x5)   |(x4) \(x3)
        [x0, x1, x2, x3, x4, x5, x6, x7]
    """

    def __call__(self, location, food, body, move_direction):
        # horizontal
        self.sight = [0] * 6
        grid = SQUARE_SIZE + INTERSQUARE_SPACE
        self.get_wall_distance(
            location, DIMENSIONS, grid, move_direction)
        self.get_body_distance(
            location, DIMENSIONS, body, grid, move_direction)
        self.get_food_distance(
            location, food, grid, move_direction)

        # self.rotate_sight(move_direction)
        return self.sight

    def get_wall_distance(self, location, walls, grid_size, move_direction):
        dist_left = (location[0] - walls[0][0]) / grid_size
        dist_right = (walls[0][1] - location[0]) / grid_size
        dist_up = (location[1] - walls[1][0]) / grid_size
        dist_down = (walls[1][1] - location[1]) / grid_size
        dist_up = dist_up if dist_up == 0 else -1
        dist_right = dist_right if dist_right == 0 else -1
        dist_down = dist_down if dist_down == 0 else -1
        dist_left = dist_left if dist_left == 0 else -1
        # dist_diagonal_up_left = min(dist_up, dist_left) * 2
        # dist_diagonal_up_right = min(dist_up, dist_right) * 2
        # dist_diagonal_down_left = min(dist_down, dist_left) * 2
        # dist_diagonal_down_right = min(dist_down, dist_right) * 2
        look_direction = []
        if(move_direction == 'u'):
            look_direction = [dist_up, dist_left, dist_right]
        if(move_direction == 'r'):
            look_direction = [dist_right, dist_up, dist_down]
        if(move_direction == 'd'):
            look_direction = [dist_down, dist_right, dist_left]
        if(move_direction == 'l'):
            look_direction = [dist_left, dist_down, dist_up]
        self.sight[::2] = look_direction

    def get_body_distance(self, location, walls, body, grid_size, move_direction):
        dist_left = -1
        dist_right = -1
        dist_up = -1
        dist_down = -1
        for y in range(location[1]-grid_size, walls[1][0], -grid_size):
            if [location[0], y] in body:
                dist_up = (location[1] - y) / grid_size
                break
        for x in range(location[0]+grid_size, walls[0][1], grid_size):
            if [x, location[1]] in body:
                dist_right = (x - location[0]) / grid_size
                break
        for y in range(location[1]+grid_size, walls[1][1], grid_size):
            if [location[0], y] in body:
                dist_down = (y - location[1]) / grid_size
                break
        for x in range(location[0]-grid_size, walls[0][0], -grid_size):
            if [x, location[1]] in body:
                dist_left = (location[0] - x) / grid_size
                break

        dist_up = dist_up if dist_up == 0 else -1
        dist_right = dist_right if dist_right == 0 else -1
        dist_down = dist_down if dist_down == 0 else -1
        dist_left = dist_left if dist_left == 0 else -1

        look_direction = []
        if(move_direction == 'u'):
            look_direction = [dist_up, dist_left, dist_right]
        if(move_direction == 'r'):
            look_direction = [dist_right, dist_up, dist_down]
        if(move_direction == 'd'):
            look_direction = [dist_down, dist_right, dist_left]
        if(move_direction == 'l'):
            look_direction = [dist_left, dist_down, dist_up]

        if look_direction[0] >= 0:
            self.sight[0] = look_direction[0]
        if look_direction[1] >= 0:
            self.sight[2] = look_direction[1]
        if look_direction[2] >= 0:
            self.sight[4] = look_direction[2]

        self.sight = utils.normalize_vector(self.sight)

    def get_food_distance(self, location, food_locations, grid_size, move_direction):
        dist_left = 0
        dist_right = 0
        dist_up = 0
        dist_down = 0

        for food_location in food_locations:
            food_vector = [(food_location[0] - location[0]) / grid_size,
                           (food_location[1] - location[1]) / grid_size]

            if food_vector[0] == 0 and food_vector[1] > 0 and (dist_down > abs(food_vector[1]) or dist_down == 0):
                dist_down = 1  # abs(food_vector[1])
            if food_vector[0] == 0 and food_vector[1] < 0 and (dist_up > abs(food_vector[1]) or dist_up == 0):
                dist_up = 1  # abs(food_vector[1])
            if food_vector[1] == 0 and food_vector[0] > 0 and (dist_right > abs(food_vector[0]) or dist_right == 0):
                dist_right = 1  # abs(food_vector[0])
            if food_vector[1] == 0 and food_vector[0] < 0 and (dist_left > abs(food_vector[0]) or dist_left == 0):
                dist_left = 1  # abs(food_vector[0])

        look_direction = []
        if(move_direction == 'u'):
            look_direction = [dist_up, dist_left, dist_right]
        if(move_direction == 'r'):
            look_direction = [dist_right, dist_up, dist_down]
        if(move_direction == 'd'):
            look_direction = [dist_down, dist_right, dist_left]
        if(move_direction == 'l'):
            look_direction = [dist_left, dist_down, dist_up]
        self.sight[1::2] = look_direction

    def rotate_sight(self, direction):
        if(direction == 'r'):
            self.sight[::2] = self.shift_left(self.sight[::2], 2)
            self.sight[1::2] = self.shift_left(self.sight[1::2], 2)
        if(direction == 'l'):
            self.sight[::2] = self.shift_left(self.sight[::2], 6)
            self.sight[1::2] = self.shift_left(self.sight[1::2], 6)
        if(direction == 'd'):
            self.sight[::2] = self.shift_left(self.sight[::2], 4)
            self.sight[1::2] = self.shift_left(self.sight[1::2], 4)

    def shift_left(self, _list, steps):
        items = deque(_list)
        items.rotate(-steps)
        return list(items)
