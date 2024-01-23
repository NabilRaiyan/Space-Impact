import turtle

class Level:
    def __init__(self):
        self.level_position = (0, -160)
    def create_level(self, level_img):
        bg_1 = turtle.Turtle()
        turtle.register_shape(level_img)
        bg_1.shape(level_img)
        bg_1.penup()
        bg_1.goto(self.level_position)