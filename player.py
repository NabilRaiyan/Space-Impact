import turtle
class Player:
    def __init__(self):

        self.bullets_list = []
        self.player = turtle.Turtle()
        turtle.register_shape('assets/player.gif')
        self.player.shape("assets/player.gif")
        self.player.penup()
        self.player.goto(-310, 0)
        self.movement_speed = 25

    def mover_ight(self):
        new_xcor_right = self.player.xcor() + self.movement_speed
        self.player.goto(new_xcor_right, self.player.ycor())

    def move_left(self):
        new_xcor_left = self.player.xcor() - self.movement_speed
        self.player.goto(new_xcor_left, self.player.ycor())
    def move_up(self):
        new_ycor_up = self.player.ycor() + self.movement_speed
        self.player.goto(self.player.xcor(), new_ycor_up)

    def move_down(self):
        new_ycor_down = self.player.ycor() - self.movement_speed
        self.player.goto(self.player.xcor(), new_ycor_down)

    def create_bullet(self):
        bullet = turtle.Turtle('square')
        bullet.shapesize(stretch_len=0.2, stretch_wid=0.1)
        bullet.penup()
        bullet.color('black')
        bullet.goto(self.player.xcor(), self.player.ycor())
        self.bullets_list.append(bullet)

    def shoot(self):
        for bullet in self.bullets_list:
            bullet.forward(20)