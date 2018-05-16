class Sight:
    """
    Sight is vector of 16 values:
        1) First eight coordinates are distance to walls or body
        1) Second eight coordinates are distance to food
    The vector octets follow next pattern:
        \(x7) |(x0) /(x1)
        --(x6)     --(x2)
        /(x5) |(x4) \(x3)
        [x0, x1, x2, x3, x4, x5, x6, x7]
    """

    def __call__(self, location, walls, food, grid_size, body):
        # horizontal
        sight = self.get_wall_distance(location, walls, grid_size)
        sight = self.get_body_distance(location, walls, body, grid_size, sight)
        sight.extend(self.get_food_distance(location, food, grid_size))
        return sight

    def get_wall_distance(self, location, walls, grid_size):
        dist_x_left = (location[0] - walls[0][0]) / grid_size
        dist_x_right = (walls[0][1] - location[0]) / grid_size
        dist_y_up = (location[1] - walls[1][0]) / grid_size
        dist_y_down = (walls[1][1] - location[1]) / grid_size

        dist_diagonal_up_left = min(dist_y_up, dist_x_left) * 2
        dist_diagonal_up_right = min(dist_y_up, dist_x_right) * 2
        dist_diagonal_down_left = min(dist_y_down, dist_x_left) * 2
        dist_diagonal_down_right = min(dist_y_down, dist_x_right) * 2

        return [dist_y_up,
                dist_diagonal_up_right,
                dist_x_right,
                dist_diagonal_down_right,
                dist_y_down,
                dist_diagonal_down_left,
                dist_x_left,
                dist_diagonal_up_left]

    def get_body_distance(self, location, walls, body, grid_size, sight):
        dist_left = sight[6]
        dist_right = sight[2]
        dist_up = sight[0]
        dist_down = sight[4]
        dist_diagonal_up_left = sight[7]
        dist_diagonal_up_right = sight[1]
        dist_diagonal_down_left = sight[5]
        dist_diagonal_down_right = sight[3]
        for x in range(location[0]-grid_size, walls[0][0], -grid_size):
            if [x, location[1]] in body:
                dist_left = (location[0] - x) / grid_size
                break
        for x in range(location[0]+grid_size, walls[0][1], grid_size):
            if [x, location[1]] in body:
                dist_right = (x - location[0]) / grid_size
                break
        for y in range(location[1]-grid_size, walls[1][0], -grid_size):
            if [location[0], y] in body:
                dist_up = (location[1] - y) / grid_size
                break
        for y in range(location[1]+grid_size, walls[1][1], grid_size):
            if [location[0], y] in body:
                dist_down = (y - location[1]) / grid_size
                break
        for x, y in zip(range(location[0]+grid_size, walls[0][1], grid_size),
                        range(location[1]-grid_size, walls[1][0], -grid_size)):
            if [x, y] in body:
                dist_diagonal_up_right = (x + y) / grid_size
                break

        for x, y in zip(range(location[0]+grid_size, walls[0][1], grid_size),
                        range(location[1]+grid_size, walls[1][1], grid_size)):
            if [x, y] in body:
                dist_diagonal_down_right = (x + y) / grid_size
                break

        for x, y in zip(range(location[0]-grid_size, walls[0][0], -grid_size),
                        range(location[1]+grid_size, walls[1][1], grid_size)):
            if [x, y] in body:
                dist_diagonal_down_left = (x + y) / grid_size
                break

        for x, y in zip(range(location[0]-grid_size, walls[0][0], -grid_size),
                        range(location[1]-grid_size, walls[1][0], -grid_size)):
            if [x, y] in body:
                dist_diagonal_up_left = (x + y) / grid_size
                break

        return [dist_up,
                dist_diagonal_up_right,
                dist_right,
                dist_diagonal_down_right,
                dist_down,
                dist_diagonal_down_left,
                dist_left,
                dist_diagonal_up_left]

    def get_food_distance(self, location, food_location, grid_size):
        food_sight = [0] * 8
        food_vector = [(food_location[0] - location[0]) / grid_size,
                       (food_location[1] - location[1]) / grid_size]
        if food_vector[0] == 0 and food_vector[1] > 0:
            food_sight[0] = food_vector[1]
        if food_vector[0] == 0 and food_vector[1] < 0:
            food_sight[4] = food_vector[1]
        if food_vector[1] == 0 and food_vector[0] > 0:
            food_sight[2] = food_vector[0]
        if food_vector[1] == 0 and food_vector[0] < 0:
            food_sight[6] = food_vector[0]
        if abs(food_vector[0]) == abs(food_vector[1]):
            dist = abs(food_vector[0]) + abs(food_vector[1])
            if food_vector[0] > 0 and food_vector[1] > 0:
                food_sight[1] = dist
            if food_vector[0] > 0 and food_vector[1] < 0:
                food_sight[3] = dist
            if food_vector[0] < 0 and food_vector[1] < 0:
                food_sight[5] = dist
            if food_vector[0] < 0 and food_vector[1] > 0:
                food_sight[7] = dist

        return food_sight
