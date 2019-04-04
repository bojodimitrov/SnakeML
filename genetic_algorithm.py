from population import Population
from world_configuration import KILL_COUNT, CROSSBREED_COUNT


class Evolver:
    def __init__(self, population_size):
        self.epoch = 0
        self.population_size = population_size
        self.population = Population(population_size)

    def evolve(self):
        self.population.kill(KILL_COUNT)
        self.population.crossbreed(CROSSBREED_COUNT)
        self.population.mutate()
        self.population.utilities()
        self.population.reset()
        self.epoch += 1
        print("Generation: " + str(self.epoch))

    def get_next_snake(self):
        if self.population.population_is_over():
            self.evolve()

        return self.population.get_next_snake()

    def get_current_snake(self):
        return self.population.get_current_snake()
