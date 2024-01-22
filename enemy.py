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

    def enemy_move(self):
        for enemy in self.enemy_list:
            enemy.forward(self.enemy_movement)