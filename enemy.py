import turtle
import random

# enemy class
class Enemy:
    def __init__(self):
        self.enemy_list = []
        self.enemy_bullet_list = []
        self.enemy_movement = 2
        self.enemy_count = 0
        self.totalEnemy = 500

    #creating enemy
    def create_enemy(self, enemy_img):
        if self.totalEnemy > self.enemy_count:
            if random.randint(1, 40) == 2:
                enemy = turtle.Turtle()
                turtle.register_shape(enemy_img)
                enemy.shape(enemy_img)
                enemy.setheading(180)
                enemy.penup()
                x_position = 500
                random_y = random.randint(-50, 190)
                enemy.goto(x_position - 10, random_y + 10)
                self.enemy_list.append(enemy)
                self.enemy_count += 1
                # creating enemy bullet
                self.enemy_bullet(enemy.xcor(), enemy.ycor())

    # creating enemy movement
    def enemy_move(self):
        for enemy in self.enemy_list:
            enemy.forward(self.enemy_movement)

    # creating enemy bullet
    def enemy_bullet(self, x, y):
        bullet = turtle.Turtle('square')
        bullet.penup()
        bullet.color('black')
        bullet.shapesize(stretch_len=0.2, stretch_wid=0.1)
        bullet.goto(x, y)
        self.enemy_bullet_list.append(bullet)

    def enemy_shoot(self):
        for bullet in self.enemy_bullet_list:
            bullet.setheading(180)
            bullet.forward(3)