POINTS_PER_FOOD = 1
SQUARE_SIZE = 12
INTERSQUARE_SPACE = 3


class Snake:
    def __init__(self, location, lenght):
        self.body = []
        self.lenght = lenght
        self.score = 0
        self.time_alive = 0
        self.direction = 'r'
        self.die = None

        cur_x = location[0]
        cur_y = location[1]
        for _ in range(self.lenght):
            self.body.append([cur_x, cur_y])
            cur_x -= SQUARE_SIZE + INTERSQUARE_SPACE

    def update_score(self):
        self.score += POINTS_PER_FOOD

    def update_direction(self, direction):
        if(self.direction == 'r' and direction == 'l' or direction == 'r' and self.direction == 'l'):
            return
        if(self.direction == 'u' and direction == 'd' or direction == 'u' and self.direction == 'd'):
            return
        self.direction = direction

    def get_size(self):
        return SQUARE_SIZE

    def get_grid(self):
        return SQUARE_SIZE + INTERSQUARE_SPACE

    def get_body(self):
        return self.body

    def get_score(self):
        return self.score

    def bind_death_event(self, handler):
        self.die = handler

    def bind_eat_event(self, handler):
        self.eaten = handler

    def update(self, positions, walls, food_location):
        if self.body_hit(positions) or self.wall_hit(positions, walls) or self.time_alive == 500:
            self.die()
        if positions[0] == food_location[0] and positions[1] == food_location[1]:
            self.eat()

        self.body.insert(0, positions)
        self.body.pop()
        self.time_alive += 1

    def get_location(self):
        return list(self.body[0])

    def eat(self):
        tail_location = self.body[-1]
        tail_direction = [self.body[-2][0] - tail_location[0],
                          self.body[-2][1] - tail_location[1]]
        self.body.append([tail_location[0] - tail_direction[0],
                          tail_location[1] - tail_direction[1]])
        self.update_score()
        self.eaten()

    def move(self, walls, food_location):
        snake_location = list(self.body[0])

        if(self.direction == 'r'):
            snake_location[0] += SQUARE_SIZE + INTERSQUARE_SPACE
        if(self.direction == 'u'):
            snake_location[1] -= SQUARE_SIZE + INTERSQUARE_SPACE
        if(self.direction == 'l'):
            snake_location[0] -= SQUARE_SIZE + INTERSQUARE_SPACE
        if(self.direction == 'd'):
            snake_location[1] += SQUARE_SIZE + INTERSQUARE_SPACE

        self.update(snake_location, walls, food_location)

    def wall_hit(self, location, walls):

        if location[0] < walls[0][0] or location[0] > walls[0][1] or location[1] < walls[1][0] or location[1] > walls[1][1]:
            self.die()

    def body_hit(self, new_position):
        for body_part in self.body:
            if new_position[0] == body_part[0] and new_position[1] == body_part[1]:
                return True

    def reset_location(self, location, lenght):
        self.body = []
        self.lenght = lenght
        self.score = 0
        self.time_alive = 0
        self.direction = 'r'

        cur_x = location[0]
        cur_y = location[1]
        for _ in range(self.lenght):
            self.body.append([cur_x, cur_y])
            cur_x -= SQUARE_SIZE + INTERSQUARE_SPACE
