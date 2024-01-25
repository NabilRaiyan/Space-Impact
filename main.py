import time
import turtle
from turtle import Screen, Turtle
from player import Player
from enemy import Enemy
from boss import Boss
from scoreboardAndLevel import ScoreBoard
from scoreboardAndLevel import Level
from health import Health
import math

game_level = 3

# creating screen, player, enemy objects
screen = Screen()
screen.listen()
screen.tracer(0)

game_is_on = False
show_menu = True





# Function to draw menu options
def draw_menu():
    menu_pen = Turtle()
    menu_pen.hideturtle()
    menu_pen.clear()
    menu_pen.penup()
    menu_pen.goto(0, 100)
    menu_pen.write("Space Impact", align="center", font=("Arial", 24, "bold"))
    menu_pen.goto(0, 50)
    menu_pen.write("1. Start New Game", align="center", font=("Arial", 16, 'bold'))
    menu_pen.goto(0, 20)
    menu_pen.write("3. Exit", align="center", font=("Arial", 16, 'bold'))



# Function to handle mouse clicks
def handle_click(x, y):
    global game_is_on, show_menu
    if show_menu:
        if 40 < y < 70:  # Start New Game
            show_menu = False
            game_is_on = True
            draw_game_element()
        elif 10 < y < 30:  # Exit
            screen.bye()

def draw_game_element():
    global game_is_on

    players = Player()
    enemy = Enemy()
    level = Level()
    score = ScoreBoard()
    health = Health()
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
                    game_is_on = False
                    score.game_over()

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
                    game_is_on = False
                    score.game_over()


# assigning game boss depending on level
if game_level == 1:
    boss = Boss('assets/boss1.gif')
elif game_level == 2:
    boss = Boss('assets/boss2.gif')

    turtle.ontimer(boss.auto_shoot, 1000)  # Start the auto-shoot after 1000 milliseconds (1 seconds)

# setting up the screen
screen.title("Space Impact")
screen.setup(width=700, height=500)
screen.bgcolor("#81BB7A")


draw_menu()
screen.onclick(handle_click)
screen.mainloop()






#from bvPlayer import bvPlayer
#bvPlayer("assets/funny.mp4", draggable = True, fps = 28, dim = (800, 450), pos = (300,50))
