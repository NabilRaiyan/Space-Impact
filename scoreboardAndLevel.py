import turtle
from turtle import Turtle
FONT = ("Comic sans", 30, 'bold')

class Level:
    def __init__(self):
        self.level_position = (0, -160)
    def create_level(self, level_img):
        bg_1 = turtle.Turtle()
        turtle.register_shape(level_img)
        bg_1.shape(level_img)
        bg_1.penup()
        bg_1.goto(self.level_position)



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(250, 200)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'000{self.score}', align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

