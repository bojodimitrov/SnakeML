class Sight:
    """
    Sight is vector of 24 values:
        1) First eight coordinates are distance to walls
        2) Second eight coordinates are distance to self
        3) Third eight coordinates are distance to food
    The vector octets follow next pattern:
        \(x7) |(x0) /(x1)
        --(x6)     --(x2)
        /(x5) |(x4) \(x3) 
        [x0, x1, x2, x3, x4, x5, x6, x7]
    """

    def __call__(self, location, walls, food, grid_size):
        # horizontal
        sight = []
        sight.append(self.get_wall_distance(location, walls, food, grid_size))

        return sight

    def get_wall_distance(self, location, walls, food, grid_size):
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
