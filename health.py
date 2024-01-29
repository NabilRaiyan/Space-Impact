import turtle

class Health:
    def __init__(self):
        self.health_count = 3
        self.health_list = []
        for i in range(3):
            self.create_health(-300 + i*30, 220)

    # create health
    def create_health(self, x, y):
        health = turtle.Turtle()
        turtle.register_shape('assets/health.gif')
        health.shape('assets/health.gif')
        health.penup()
        health.goto(x, y)
        self.health_list.append(health)

    #remove health
    def remove_health(self):
        if self.health_count > 0:
            self.health_count -= 1
            health_to_remove = self.health_list.pop()
            health_to_remove.hideturtle()






