from world_configuration import DIE_OF_HUNGER, POINTS_PER_FOOD, SQUARE_SIZE, INTERSQUARE_SPACE


class Snake:
    def __init__(self, location, lenght):
        self.body = []
        self.block_input = False
        self.lenght = lenght
        self.score = 0
        self.time_alive = 0
        self.direction = 'r'
        self.die = None
        self.predeath_event = None

        cur_x = location[0]
        cur_y = location[1]
        for _ in range(self.lenght):
            self.body.append([cur_x, cur_y])
            cur_x -= SQUARE_SIZE + INTERSQUARE_SPACE

    def update_score(self):
        self.score += POINTS_PER_FOOD

    def update_direction(self, direction):
        if self.block_input:
            return
        if(self.direction == 'r' and direction == 'l' or direction == 'r' and self.direction == 'l'):
            return
        if(self.direction == 'u' and direction == 'd' or direction == 'u' and self.direction == 'd'):
            return
        self.direction = direction
        self.block_input = True

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

    def bind_predeath_event(self, handler):
        self.predeath_event = handler

    def bind_eat_event(self, handler):
        self.eaten = handler

    def update(self, positions, walls, food_locations):
        if self.body_hit(positions) or self.wall_hit(positions, walls) or self.time_alive == DIE_OF_HUNGER:
            self.execute_predeath_event()
            self.die()
        if positions in food_locations:
            self.eat(positions)

        self.body.insert(0, positions)
        self.body.pop()
        self.time_alive += 1

    def get_location(self):
        return list(self.body[0])

    def execute_predeath_event(self):
        if self.predeath_event is not None:
            self.predeath_event()

    def eat(self, food_location):
        tail_location = self.body[-1]
        tail_direction = [self.body[-2][0] - tail_location[0],
                          self.body[-2][1] - tail_location[1]]
        self.body.append([tail_location[0] - tail_direction[0],
                          tail_location[1] - tail_direction[1]])
        self.update_score()
        self.time_alive = 0
        self.eaten(food_location)

    def move(self, walls, food_locations):
        snake_location = self.calculate_move(self.direction)
        self.block_input = False

        self.update(snake_location, walls, food_locations)

    def calculate_move(self, direction):
        snake_location = self.get_location()
        if(direction == 'r'):
            snake_location[0] += SQUARE_SIZE + INTERSQUARE_SPACE
        if(direction == 'u'):
            snake_location[1] -= SQUARE_SIZE + INTERSQUARE_SPACE
        if(direction == 'l'):
            snake_location[0] -= SQUARE_SIZE + INTERSQUARE_SPACE
        if(direction == 'd'):
            snake_location[1] += SQUARE_SIZE + INTERSQUARE_SPACE
        return snake_location

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
