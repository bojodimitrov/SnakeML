from snake import Snake
import NeuralNetwork
from sight import Sight


class SmartSnake(Snake):
    def __init__(self, location, lenght, brain):
        super(SmartSnake, self).__init__(location, lenght)
        self.brain = NeuralNetwork(brain)
        self.sight = Sight()

    def move(self, walls, food_location):
        result = self.brain(self.sight())
        super(SmartSnake, self).move(walls, food_location)
