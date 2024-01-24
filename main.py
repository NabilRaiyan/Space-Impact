import time
import turtle
from turtle import Screen
from player import Player
from enemy import Enemy
from boss import Boss
from scoreboardAndLevel import ScoreBoard
from scoreboardAndLevel import Level
from health import Health
import math

game_level = 1

# creating screen, player, enemy objects
screen = Screen()
screen.listen()
screen.tracer(0)

players = Player()
enemy = Enemy()
level = Level()
score = ScoreBoard()
health = Health()


if game_level == 1:
    boss = Boss('assets/boss1.gif')
elif game_level == 2:
    boss = Boss('assets/boss2.gif')

    turtle.ontimer(boss.auto_shoot, 1000)  # Start the auto-shoot after 1000 milliseconds (1 seconds)

# setting up the screen
screen.title("Space Impact")
screen.setup(width=700, height=500)
screen.bgcolor("#81BB7A")


game_is_on = True
if game_level == 1:
    level.create_level('assets/bg.gif')




while game_is_on:
    time.sleep(0.01)
    screen.update()

    screen.onkey(key="Up", fun=players.move_up)
    screen.onkey(key='Down', fun=players.move_down)

    screen.onkey(key='s', fun=players.create_bullet)

    players.shoot()

    if game_level == 1:
        enemy.create_enemy('assets/enemy1.gif')
    elif game_level == 2:
        enemy.create_enemy('assets/enemy2.gif')
    elif game_level == 3:
        enemy.create_enemy('assets/enemy3.gif')
        enemy.create_enemy('assets/enemy2.gif')
        enemy.create_enemy('assets/enemy1.gif')
    enemy.enemy_move()
    enemy.enemy_shoot()
    if enemy.enemy_count == 100 and game_level == 2:
        boss.boss_move()
        boss.boss_shoot()

    # detecting collision with bullet and enemy
    for bullet in players.bullets_list:
        for e in enemy.enemy_list:
            if bullet.distance(e) < 20:
                enemy.enemy_list.remove(e)
                e.hideturtle()
                score.increase_score()



    # Function to check if there is a collision between two turtles
    def is_collision(t1, t2, radius1, radius2):
        distance = math.sqrt((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2)
        return distance < (radius1 + radius2)

    # detect collision with enemy bullet and player
    for bullet in enemy.enemy_bullet_list:
        if bullet.distance(players.player) < 10:
            bullet.hideturtle()
            enemy.enemy_bullet_list.remove(bullet)
            players.player_hit_count += 1
            print(players.player_hit_count)
            if players.player_hit_count == 2:
                health.remove_health()
            elif players.player_hit_count == 4:
                health.remove_health()
            elif players.player_hit_count == 6:
                health.remove_health()
                score.reset()



    # Detect collision with enemy and player
    for e in enemy.enemy_list:
        if is_collision(players.player, e, 5, 24):
            players.player_hit_count += 1
            enemy.enemy_list.remove(e)
            e.hideturtle()
            if players.player_hit_count == 2:
                health.remove_health()
            elif players.player_hit_count == 4:
                health.remove_health()
            elif players.player_hit_count == 6:
                health.remove_health()
                score.reset()



screen.mainloop()






#from bvPlayer import bvPlayer
#bvPlayer("assets/funny.mp4", draggable = True, fps = 28, dim = (800, 450), pos = (300,50))
