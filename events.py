def move_up(snake):
    snake.update_direction('u')


def move_right(snake):
    snake.update_direction('r')


def move_left(snake):
    snake.update_direction('l')


def move_down(snake):
    snake.update_direction('d')


def eat(snake):
    snake.eat()
