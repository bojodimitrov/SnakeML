from smart_snake import SmartSnake
from random import shuffle, randint

DEFAULT_LOCATION = [100, 100]
DEFAULT_LENGHT = 5
LAYERS_PATTERN = [16, 8, 4]


class Population:
    def __init__(self, number_of_individuals):
        self.individuals = []
        self.current_simulated_snake = 0
        for _ in range(number_of_individuals):
            self.individuals.append(SmartSnake(
                DEFAULT_LOCATION, DEFAULT_LENGHT, LAYERS_PATTERN))

    def kill(self, number_to_kill):
        self.individuals.sort(key=lambda x: x.fit())
        print([x.fit() for x in self.individuals])
        for _ in range(number_to_kill):
            del self.individuals[0]

    def crossbreed(self, number_to_crossbreed, best_fit=True):
        if not best_fit:
            shuffle(self.individuals)
        self.individuals.sort(key=lambda x: x.fit(), reverse=True)
        for i in range(0, number_to_crossbreed, 2):
            parent_a = self.individuals[i]
            parent_b = self.individuals[i+1]
            self.individuals.extend(self.mate(parent_a, parent_b))
        print([x.fit() for x in self.individuals])

    def mate(self, parent_a, parent_b):
        child_snake_a = SmartSnake(
            DEFAULT_LOCATION, DEFAULT_LENGHT, LAYERS_PATTERN)
        child_snake_b = SmartSnake(
            DEFAULT_LOCATION, DEFAULT_LENGHT, LAYERS_PATTERN)
        layer_chosen = randint(1, len(LAYERS_PATTERN)-1)
        child_snake_a.plug(parent_a.get_brain())
        child_snake_b.plug(parent_b.get_brain())
        child_snake_a.get_brain().set_layer(
            layer_chosen, parent_b.get_brain().get_layer(layer_chosen))
        child_snake_b.get_brain().set_layer(
            layer_chosen, parent_a.get_brain().get_layer(layer_chosen))
        return [child_snake_a, child_snake_b]

    def mutate(self):
        for snake in self.individuals:
            snake.mutate()

    def get_next_snake(self):
        self.current_simulated_snake += 1
        return self.individuals[self.current_simulated_snake - 1]

    def population_is_over(self):
        return self.current_simulated_snake == len(self.individuals)

    def reset(self):
        for snake in self.individuals:
            snake.reset_location(DEFAULT_LOCATION, DEFAULT_LENGHT)
        self.current_simulated_snake = 0
