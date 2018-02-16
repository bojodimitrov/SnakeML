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

    def bind_event(self, name, handler):
        self.canvas.bind(name, handler)

    def clear(self):
        self.canvas.delete('all')

    def write(self, text, location):
        self.canvas.create_text(
            location[0], location[1], text=text, fill="white")
