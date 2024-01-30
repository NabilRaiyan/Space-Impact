import turtle

# initializing the boss variables
FINISHING_LINE_X = 250
SET_HEADING = 180
MOVEMENT_SPEED = 1
STARTING_POSITION = (400, 0)

class Boss:
    def __init__(self, boss_img):
        self.boss_bullet_list = []
        self.boss = turtle.Turtle()
        turtle.register_shape(boss_img)
        self.boss.shape(boss_img)
        self.boss.penup()
        self.boss.setheading(SET_HEADING)
        self.boss.goto(STARTING_POSITION)
        self.y_move = 16
        self.boss_hit_count = 0

    # boss move function
    def boss_move(self):
        self.boss.forward(MOVEMENT_SPEED)
        if self.boss.xcor() < FINISHING_LINE_X:
            self.boss.goto(FINISHING_LINE_X, 0)

    # creating boss bullet
    def boss_bullet(self, x, y):
        bullet = turtle.Turtle('square')
        bullet.penup()
        bullet.color('black')
        bullet.shapesize(stretch_len=0.3, stretch_wid=0.2)
        bullet.goto(x, y)
        self.boss_bullet_list.append(bullet)


    # boss shooting function
    def boss_shoot(self):
        for bullet in self.boss_bullet_list:
            bullet.setheading(180)
            bullet.forward(3)

    # boss auto shooting function
    def auto_shoot(self):
        self.boss_bullet(self.boss.xcor() - 10, self.boss.ycor())
        turtle.ontimer(self.auto_shoot, 1000)  # Auto shoot every 1000 milliseconds (1 second)






