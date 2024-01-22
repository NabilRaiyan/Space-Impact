import time
from turtle import Screen
from player import Player
from enemy import Enemy

screen = Screen()
screen.listen()
screen.tracer(0)

player = Player()
enemy = Enemy()

screen.title("Space Impact")
screen.setup(width=700, height=500)
screen.bgcolor("#7A9E81")



game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.01)
    screen.onkey(key="Left", fun=player.move_left)
    screen.onkey(key='Right', fun=player.mover_ight)
    screen.onkey(key="Up", fun=player.move_up)
    screen.onkey(key='Down', fun=player.move_down)

    screen.onkey(key='s', fun=player.create_bullet)

    player.shoot()
    enemy.create_enemy()
    enemy.enemy_move()


screen.mainloop()






#from bvPlayer import bvPlayer
#bvPlayer("assets/funny.mp4", draggable = True, fps = 28, dim = (800, 450), pos = (300,50))
