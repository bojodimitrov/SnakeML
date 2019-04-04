from smart_snake import SmartSnake
import pickle
from random import shuffle, randint
from world_configuration import (DEFAULT_LOCATION,
                                 DEFAULT_LENGHT,
                                 LAYERS_PATTERN,
                                 MUTABLE_COUNT,
                                 POPULATION_COUNT,
                                 UNCHANGABLE_COUNT,
                                 CROSSBREED_REPS)


class Population:
    def __init__(self, number_of_individuals):
        self.individuals = []
        self.mean_results = []
        self.current_best_result = 0
        self.current_simulated_snake = 0
        for _ in range(number_of_individuals):
            self.individuals.append(SmartSnake(
                DEFAULT_LOCATION, DEFAULT_LENGHT, LAYERS_PATTERN))

    def kill(self, number_to_kill):
        self.individuals.sort(key=lambda x: x.fit())
        for _ in range(number_to_kill):
            del self.individuals[0]

    def crossbreed(self, number_to_crossbreed, best_fit=True):
        if not best_fit:
            shuffle(self.individuals)
        self.individuals.sort(key=lambda x: x.fit(), reverse=True)
        for _ in range(CROSSBREED_REPS):
            self.crossbreed_selection(number_to_crossbreed)

    def crossbreed_selection(self, number_to_crossbreed):
        for i in range(0, int(number_to_crossbreed / CROSSBREED_REPS), 2):
            parent_a = self.individuals[i]
            parent_b = self.individuals[i+1]
            self.individuals.extend(self.mate(parent_a, parent_b))

    def mate_two_offspirngs(self, parent_a, parent_b):
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

    def mate(self, parent_a, parent_b):
        offspring_snake = SmartSnake(
            DEFAULT_LOCATION, DEFAULT_LENGHT, LAYERS_PATTERN)
        layer_chosen = randint(1, len(LAYERS_PATTERN)-1)
        offspring_snake.plug(parent_a.get_brain())
        offspring_snake.get_brain().set_layer(
            layer_chosen, parent_b.get_brain().get_layer(layer_chosen))

        return [offspring_snake]

    def mutate(self):
        self.individuals.sort(key=lambda x: x.fit(), reverse=True)
        print([x.fit() for x in self.individuals][:20])

        for _ in range(MUTABLE_COUNT):
            snake = randint(UNCHANGABLE_COUNT, len(self.individuals)-1)
            self.individuals[snake].mutate()

    def get_next_snake(self):
        self.current_simulated_snake += 1
        return self.individuals[self.current_simulated_snake - 1]

    def population_is_over(self):
        return self.current_simulated_snake == len(self.individuals)

    def get_current_snake(self):
        return self.current_simulated_snake

    def reset(self):
        for snake in self.individuals:
            snake.reset_location(DEFAULT_LOCATION, DEFAULT_LENGHT)
        self.current_simulated_snake = 0

    def save_best_snake(self):
        self.individuals.sort(key=lambda x: x.fit(), reverse=True)
        best_snake = self.individuals[0]
        if best_snake.fit() > self.current_best_result:
            self.current_best_result = best_snake.fit()
            with open('best_snake', 'wb') as best_snake_file:
                pickle.dump(best_snake.get_brain(), best_snake_file)
                print('Best snake saved with score:', best_snake.fit())

    def save_mean_result(self):
        mean = sum([x.fit() for x in self.individuals]) / len(self.individuals)
        self.mean_results.append(mean)
        with open('mean_results.txt', 'w') as f:
            for item in self.mean_results:
                f.write("%s\n" % item)

    def print_most_feedings(self):
        self.individuals.sort(key=lambda x: x.get_score(), reverse=True)
        print("Most feedings: ", self.individuals[0].get_score())

    def utilities(self):
        self.save_best_snake()
        self.save_mean_result()
