import turtle
import pygame

class Player:
    def __init__(self):

        self.bullets_list = []
        self.player = turtle.Turtle()
        turtle.register_shape('assets/player.gif')
        self.player.shape("assets/player.gif")
        self.player.penup()
        self.player.goto(-300, 0)
        self.movement_speed = 25
        self.player_hit_count = 0

    # player movements
    def move_up(self):
        new_ycor_up = self.player.ycor() + self.movement_speed
        self.player.goto(self.player.xcor(), new_ycor_up)

    def move_down(self):
        new_ycor_down = self.player.ycor() - self.movement_speed
        self.player.goto(self.player.xcor(), new_ycor_down)

    # play sound
    def play_sound(self, file_path):
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()

    # create bullet
    def create_bullet(self):
        bullet = turtle.Turtle('square')
        bullet.shapesize(stretch_len=0.2, stretch_wid=0.1)
        bullet.penup()
        bullet.color('black')
        bullet.goto(self.player.xcor(), self.player.ycor())
        self.play_sound('sounds/shoot_sound.WAV')

        self.bullets_list.append(bullet)

    # create shooting
    def shoot(self):
        for bullet in self.bullets_list:
            bullet.forward(20)

