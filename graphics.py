from world_configuration import DIMENSIONS, SQUARE_SIZE, INTERSQUARE_SPACE


class Graphics:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.focus_set()
        self.canvas.pack()
        self.canvas.configure(background="black")

    def draw(self, coordinates, square_size, color):
        for piece in coordinates:
            self.canvas.create_rectangle(
                piece[0], piece[1],
                piece[0] + square_size,
                piece[1] + square_size,
                fill=color,
                outline=color)

    def see(self, head, grid_size, walls):
        pixel = 1
        pixel_color = "blue"
        for x in range(head[0]-grid_size, walls[0][0]+1, -grid_size):
            self.canvas.create_rectangle(
                x, head[1],
                x + pixel,
                head[1] + pixel,
                fill=pixel_color,
                outline=pixel_color)
        for x in range(head[0]+grid_size, walls[0][1]+1, grid_size):
            self.canvas.create_rectangle(
                x, head[1],
                x + pixel,
                head[1] + pixel,
                fill=pixel_color,
                outline=pixel_color)
        for y in range(head[1]-grid_size, walls[1][0]+1, -grid_size):
            self.canvas.create_rectangle(
                head[0], y,
                head[0] + pixel,
                y + pixel,
                fill=pixel_color,
                outline=pixel_color)
        for y in range(head[1]+grid_size, walls[1][1]+1, grid_size):
            self.canvas.create_rectangle(
                head[0], y,
                head[0] + pixel,
                y + pixel,
                fill=pixel_color,
                outline=pixel_color)
        for x, y in zip(range(head[0]+grid_size, walls[0][1]+1, grid_size),
                        range(head[1]-grid_size, walls[1][0]+1, -grid_size)):
            self.canvas.create_rectangle(
                x, y,
                x + pixel,
                y + pixel,
                fill=pixel_color,
                outline=pixel_color)
        for x, y in zip(range(head[0]+grid_size, walls[0][1]+1, grid_size),
                        range(head[1]+grid_size, walls[1][1]+1, grid_size)):
            self.canvas.create_rectangle(
                x, y,
                x + pixel,
                y + pixel,
                fill=pixel_color,
                outline=pixel_color)
        for x, y in zip(range(head[0]-grid_size, walls[0][0]+1, -grid_size),
                        range(head[1]+grid_size, walls[1][1]+1, grid_size)):
            self.canvas.create_rectangle(
                x, y,
                x + pixel,
                y + pixel,
                fill=pixel_color,
                outline=pixel_color)
        for x, y in zip(range(head[0]-grid_size, walls[0][0]+1, -grid_size),
                        range(head[1]-grid_size, walls[1][0]+1, -grid_size)):
            self.canvas.create_rectangle(
                x, y,
                x + pixel,
                y + pixel,
                fill=pixel_color,
                outline=pixel_color)

    def bind_event(self, name, handler):
        self.canvas.bind(name, handler)

    def clear(self):
        self.canvas.delete('all')

    def write(self, text, location):
        self.canvas.create_text(
            location[0], location[1], text=text, fill="white")
