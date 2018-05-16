from graphics import Graphics
from snake import Snake
from smart_snake import SmartSnake
from food import Food
from genetic_algorithm import Evolver
import tkinter as tk
import events

DIMENSIONS = [[0, 600], [0, 600]]
WINDOW_SIZE = [620, 620]
MIL_SEC_PER_FRAME = 60
DEFAULT_SNAKE_LENGHT = 40
POPULATION_COUNT = 10


class Master:
    def __init__(self, snake_picker=None):
        self.master = tk.Tk()
        canvas = tk.Canvas(
            self.master, width=WINDOW_SIZE[0], height=WINDOW_SIZE[1])
        self.pick_snake = snake_picker
        self.init_snake()
        self.free_space = []
        self.calculate_free_space()
        self.food = Food(self.free_space)
        self.graphics = Graphics(canvas)
        self.bind_events()

    def bind_events(self):
        self.graphics.bind_event(
            "<Up>", lambda event: events.move_up(self.snake))
        self.graphics.bind_event(
            "<Right>", lambda event: events.move_right(self.snake))
        self.graphics.bind_event(
            "<Left>", lambda event: events.move_left(self.snake))
        self.graphics.bind_event(
            "<Down>", lambda event: events.move_down(self.snake))
        self.graphics.bind_event(
            "<Return>", lambda event: events.eat(self.snake))

    def calculate_free_space(self):
        snake_body = self.snake.get_body()
        self.free_space = []
        for i in range(DIMENSIONS[0][0], DIMENSIONS[0][1]+1, self.snake.get_grid()):
            for j in range(DIMENSIONS[1][0], DIMENSIONS[1][1]+1, self.snake.get_grid()):
                if [i, j] not in snake_body:
                    self.free_space.append([i, j])

    def init_snake(self):
        if self.pick_snake is None:
            self.snake = Snake([105, 105], 10)
        else:
            self.snake = self.pick_snake()
            self.handle_feed()
        self.snake.bind_death_event(self.init_snake)
        self.snake.bind_eat_event(self.handle_feed)

    def handle_feed(self):
        self.calculate_free_space()
        self.food = Food(self.free_space)

    def start(self):
        self.loop()
        self.master.mainloop()

    def loop(self):
        self.graphics.clear()
        self.snake.move(DIMENSIONS, self.food.get_location())
        self.draw()
        self.master.after(MIL_SEC_PER_FRAME, self.loop)

    def draw(self):
        snake_body = self.snake.get_body()
        snake_size = self.snake.get_size()
        self.graphics.draw(snake_body, snake_size, "white")
        self.graphics.draw([self.food.get_location()], snake_size, "red")
        self.graphics.write(str(self.snake.get_score()), [20, 20])


class Environment:
    def __init__(self):
        self.evolver = Evolver(POPULATION_COUNT)
        self.simulator = Master()

    def start(self):
        self.simulator.start()

    def get_next_snake(self):
        return self.evolver.get_next_snake()


world = Environment()
world.start()
