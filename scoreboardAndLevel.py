import turtle
from turtle import Turtle
FONT = ("Comic sans", 20, 'bold')

class Level:
    def __init__(self):
        self.level_position = (0, -160)
        self.level = 1

    # creating the level class
    def create_level(self, level_img):
        bg_1 = turtle.Turtle()
        turtle.register_shape(level_img)
        bg_1.shape(level_img)
        bg_1.penup()
        bg_1.goto(self.level_position)


# creating the scoreboard class
class ScoreBoard(Turtle):
    def __init__(self):
        with open("data.txt") as data_file:
            high_score = int(data_file.read())
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(200, 200)
        self.score = 0
        self.high_score = high_score
        self.update_score()

    # Reset score function
    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as data_file:
                data_file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_score()

    # update score
    def update_score(self):
        self.clear()
        self.write(f'000{self.score}  High Score: {self.high_score}', align='center', font=FONT)

    # increase score
    def increase_score(self):
        self.score += 1
        self.update_score()

    # game over
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)


