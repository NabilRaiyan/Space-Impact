import time
import turtle
from turtle import Screen
from player import Player
from enemy import Enemy
from boss import Boss
from scoreboardAndLevel import Level

# creating screen, player, enemy objects
screen = Screen()
screen.listen()
screen.tracer(0)

player = Player()
enemy = Enemy()
boss = Boss()
level = Level()
turtle.ontimer(boss.auto_shoot, 1000)  # Start the auto-shoot after 1000 milliseconds ( seconds)

# setting up the screen
screen.title("Space Impact")
screen.setup(width=700, height=500)
screen.bgcolor("#7A9E81")


game_is_on = True
game_level = 3
if game_level == 1:
    level.create_level('assets/level_1-bg.gif')


while game_is_on:
    time.sleep(0.01)
    screen.update()

    screen.onkey(key="Up", fun=player.move_up)
    screen.onkey(key='Down', fun=player.move_down)

    screen.onkey(key='s', fun=player.create_bullet)

    player.shoot()

    if game_level == 1:
        enemy.create_enemy('assets/enemy1.gif')
    elif game_level == 2:
        enemy.create_enemy('assets/enemy2.gif')
    elif game_level == 3:
        enemy.create_enemy('assets/enemy1.gif')
        enemy.create_enemy('assets/enemy2.gif')
    enemy.enemy_move()
    enemy.enemy_shoot()
    if enemy.enemy_count == 5:
        boss.boss_move()
        boss.boss_shoot()










screen.mainloop()






#from bvPlayer import bvPlayer
#bvPlayer("assets/funny.mp4", draggable = True, fps = 28, dim = (800, 450), pos = (300,50))
