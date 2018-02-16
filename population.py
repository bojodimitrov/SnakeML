from smart_snake import SmartSnake

DEFAULT_LOCATION = [100, 100]
DEFAULT_LENGHT = 5


class Population:
    def __init__(self, number_of_individuals):
        self.population = []
        for _ in range(number_of_individuals):
            self.population.append(SmartSnake(
                DEFAULT_LOCATION, DEFAULT_LENGHT, [8, 6, 4]))
