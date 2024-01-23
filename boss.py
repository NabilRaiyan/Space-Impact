import turtle

FINISHING_LINE_X = 250
SET_HEADING = 180
MOVEMENT_SPEED = 1
STARTING_POSITION = (400, 0)

class Boss:
    def __init__(self):
        self.boss = turtle.Turtle()
        turtle.register_shape('assets/boss1.gif')
        self.boss.shape('assets/boss1.gif')
        self.boss.penup()
        self.boss.setheading(SET_HEADING)
        self.boss.goto(STARTING_POSITION)
        self.y_move = 100
        self.boss_current_pos_y = self.boss.ycor()


    def boss_move(self):
        self.boss.forward(MOVEMENT_SPEED)
        if self.boss.xcor() < FINISHING_LINE_X:
            self.boss.goto(FINISHING_LINE_X, 0)





































# STARTING_POSITION = (300, 0)
# MOVEMENT_DISTANCE = 2
# FINISHING_LINE_X = 250
# SET_HEADING = 180
# class Boss:
#     def __init__(self):
#         self.boss = turtle.Turtle()
#         turtle.register_shape('assets/boss1.gif')
#         self.boss.shape('assets/boss1.gif')
#         self.boss.penup()
#         self.boss.setheading(SET_HEADING)
#         self.boss.goto(STARTING_POSITION)
#
#     def boss_move(self):
#         self.boss.forward(MOVEMENT_DISTANCE)
#         if self.boss.xcor() < FINISHING_LINE_X:
#             self.boss.goto(FINISHING_LINE_X, 0)



