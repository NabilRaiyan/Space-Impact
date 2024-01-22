import turtle
import random


class Enemy:
    def __init__(self):
        self.enemy_list = []
        self.enemy_bullet_list = []
        self.enemy_movement = 2

    def create_enemy(self):
        if random.randint(1, 40) == 2:
            enemy = turtle.Turtle()
            turtle.register_shape('assets/enemy.gif')
            enemy.shape('assets/enemy.gif')
            enemy.setheading(180)
            enemy.penup()
            x_position = 500
            random_y = random.randint(-50, 200)
            enemy.goto(x_position -10, random_y + 10)
            self.enemy_list.append(enemy)

            self.enemy_bullet(enemy.xcor(), enemy.ycor())

    def enemy_move(self):
        for enemy in self.enemy_list:
            enemy.forward(self.enemy_movement)

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