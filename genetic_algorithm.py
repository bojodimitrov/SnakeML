from population import Population

KILL_COUNT = 4
CROSSBREED_COUNT = 4


class Evolver:
    def __init__(self, population_size):
        self.epoch = 0
        self.population_size = population_size
        self.population = Population(population_size)

    def evolve(self):
        self.population.kill(KILL_COUNT)
        self.population.crossbreed(CROSSBREED_COUNT)
        self.population.mutate()
        self.population.reset()
        self.epoch += 1
        print("Generation: " + str(self.epoch))

    def get_next_snake(self):
        if self.population.population_is_over():
            self.evolve()

        return self.population.get_next_snake()
