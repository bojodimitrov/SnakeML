from snake import Snake
from sight import Sight
from neural_networks import NeuralNetwork
from mutation_operations import replace_weight, scale, shift, swap_sign
from world_configuration import DIE_OF_HUNGER, POINTS_PER_FOOD

MUTATION_PROBABILITY = 0.04


class SmartSnake(Snake):
    def __init__(self, location, lenght, brain):
        super(SmartSnake, self).__init__(location, lenght)
        self.brain = NeuralNetwork(brain)
        self.sight = Sight()
        self.bind_predeath_event(self.punish_for_suicide)

    def move(self, walls, food_location):
        sight = self.sight(self.get_location(),
                           food_location,
                           self.get_body(),
                           self.direction)
        # print(sight)

        result = self.brain(sight)

        desicion = self.change_direction(result)
        self.reward_for_food_approach(food_location, desicion)
        self.update_direction(desicion)
        super(SmartSnake, self).move(walls, food_location)

    def choose_direction(self, result):
        if result == 0:
            return 'u'
        if result == 1:
            return 'r'
        if result == 2:
            return 'd'
        if result == 3:
            return 'l'

    def change_direction(self, direction):
        if(self.direction == 'r'):
            if(direction == 0):
                return 'r'
            if(direction == 1):
                return 'u'
            if(direction == 2):
                return 'd'
        if(self.direction == 'u'):
            if(direction == 0):
                return 'u'
            if(direction == 1):
                return 'l'
            if(direction == 2):
                return 'r'
        if(self.direction == 'l'):
            if(direction == 0):
                return 'l'
            if(direction == 1):
                return 'd'
            if(direction == 2):
                return 'u'
        if(self.direction == 'd'):
            if(direction == 0):
                return 'd'
            if(direction == 1):
                return 'r'
            if(direction == 2):
                return 'l'

    def fit(self):
        # if self.score < 5:
        #     return (DIE_OF_HUNGER - self.time_alive) ** 2 * pow(2, self.score)
        # fitness = (DIE_OF_HUNGER - self.time_alive) ** 2
        # fitness *= pow(2, 10)
        return (self.score)

    def mutate(self):
        self.brain.mutate(MUTATION_PROBABILITY, [
                          replace_weight, scale, shift, swap_sign])

    def reward_for_food_approach(self, food_location, decision):
        location = self.get_location()
        dist_to_food = abs(food_location[0][0] - location[0]) / self.get_grid() + abs(
            food_location[0][1] - location[1]) / self.get_grid()
        future_location = self.calculate_move(decision)
        future_dist_to_food = abs(food_location[0][0] - future_location[0]) / self.get_grid() + abs(
            food_location[0][1] - future_location[1]) / self.get_grid()
        if (dist_to_food < future_dist_to_food):
            self.score -= 1.5
        else:
            self.score += 1

    def punish_for_suicide(self):
        if self.time_alive < 10:
            self.score -= 20

    def plug(self, brain):
        self.brain = NeuralNetwork(brain, False)

    def get_brain(self):
        return self.brain
