from snake import Snake
from sight import Sight
from neural_networks import NeuralNetwork


class SmartSnake(Snake):
    def __init__(self, location, lenght, brain):
        super(SmartSnake, self).__init__(location, lenght)
        self.brain = NeuralNetwork(brain)
        self.sight = Sight()

    def move(self, walls, food_location):
        result = self.brain(self.sight(self.get_location(),
                                       walls, food_location,
                                       self.get_grid(),
                                       self.get_body()))
        if result == 0:
            self.update_direction('r')
        if result == 1:
            self.update_direction('u')
        if result == 2:
            self.update_direction('d')
        if result == 3:
            self.update_direction('l')
        super(SmartSnake, self).move(walls, food_location)
