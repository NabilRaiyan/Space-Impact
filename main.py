
#importing all the class


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
import pygame

# initial game level
game_level = 1

# Setting up the screen
screen = Screen()
screen.listen()
screen.tracer(0)

game_is_on = False
show_menu = True
menu_pen = None
FONT = ("Comic sans", 20, 'bold')

# function to play enu click sound
def play_sound(file_path):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()

# function to generate current level
def current_level():
    cr_level = Turtle()
    cr_level.hideturtle()
    cr_level.penup()
    cr_level.color('black')
    cr_level.goto(0, 200)
    cr_level.clear()
    cr_level.write(f'Level: {game_level}', align='center', font=FONT)



# Function to draw menu options
def draw_menu():
    global menu_pen
    menu_pen = Turtle()
    menu_pen.hideturtle()
    menu_pen.clear()
    menu_pen.penup()
    menu_pen.goto(0, 100)
    menu_pen.write("Space Impact", align="center", font=("Arial", 24, "bold"))
    menu_pen.goto(0, 50)
    menu_pen.write(" Start New Game", align="center", font=("Arial", 16, 'bold'))
    menu_pen.goto(0, 20)
    menu_pen.write(" Exit", align="center", font=("Arial", 16, 'bold'))

# Hide menu options
def hide_menu():
    global menu_pen
    if menu_pen is not None:
        menu_pen.clear()


# Function to handle mouse clicks
def handle_click(x, y):
    global game_is_on, show_menu, menu_pen
    if show_menu:
        if 40 < y < 70:  # Start New Game
            play_sound('sounds/click.mp3')
            show_menu = False
            hide_menu()
            game_is_on = True
            draw_game_element()
        elif 10 < y < 30:  # Exit Game
            screen.bye()

# drawing game elements
def draw_game_element():
    global game_is_on
    global show_menu
    global game_level

    players = Player()
    enemy = Enemy()
    level = Level()
    score = ScoreBoard()
    health = Health()
    level.create_level('assets/bg.gif')
    current_level()

    # game on loop
    while game_is_on:
        time.sleep(0.01)
        screen.update()

        # event listener
        screen.onkey(key="Up", fun=players.move_up)
        screen.onkey(key='Down', fun=players.move_down)

        screen.onkey(key='s', fun=players.create_bullet)

        players.shoot()

        # enemy generate logic
        if score.score < 50:
            enemy_img = 'assets/enemy1.gif'
            enemy.create_enemy(enemy_img)


        elif score.score >= 50 and score.score <= 100:
            enemy_img = 'assets/enemy2.gif'
            enemy.create_enemy(enemy_img)

        elif score.score > 100:
            enemy_img = 'assets/enemy1.gif'
            enemy_img = 'assets/enemy2.gif'
            enemy_img = 'assets/enemy3.gif'
            enemy.create_enemy(enemy_img)
        enemy.enemy_move()
        enemy.enemy_shoot()
        if score.score > 50 and game_level == 1:
            # for e in enemy.enemy_list:
            #     e.hideturtle()
            # enemy.enemy_list.clear()
            boss1.boss_move()
            boss1.boss_shoot()

        elif score.score > 200 and game_level == 2:
            boss1.boss_move()
            boss1.boss_shoot()


        # detecting collision with player bullet and enemy
        for bullet in players.bullets_list:
            for e in enemy.enemy_list:
                if bullet.distance(e) < 20:
                    enemy.enemy_list.remove(e)
                    e.hideturtle()
                    players.bullets_list.remove(bullet)
                    bullet.hideturtle()
                    score.increase_score()


        # Function to check if there is a collision between two game object
        def is_collision(t1, t2, radius1, radius2):
            distance = math.sqrt((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2)
            return distance < (radius1 + radius2)

        # detect collision with enemy bullet and player
        for bullet in enemy.enemy_bullet_list:
            if bullet.distance(players.player) < 10:
                bullet.hideturtle()
                enemy.enemy_bullet_list.remove(bullet)
                players.player_hit_count += 1
                if players.player_hit_count == 2:
                    health.remove_health()
                elif players.player_hit_count == 4:
                    health.remove_health()
                elif players.player_hit_count == 6:
                    health.remove_health()
                    score.reset()
                    game_is_on = False
                    score.game_over()

            # detect collision with boss bullet and player
            for boss_bullet in boss1.boss_bullet_list:
                if boss_bullet.distance(players.player) < 10:
                    boss_bullet.hideturtle()
                    boss1.boss_bullet_list.remove(boss_bullet)
                    players.player_hit_count += 1
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

        # detect collision between boss and player bullet
        for bullet in players.bullets_list:
            if is_collision(boss1.boss, bullet, 5, 24):
                boss1.boss_hit_count += 1
                score.score += 1
                if boss1.boss_hit_count > 100:
                    boss1.boss.clear()
                    for bullet_boss in boss1.boss_bullet_list:
                        bullet_boss.hideturtle()
                    boss1.boss_bullet_list.clear()
                    boss1.boss.hideturtle()
                    game_level += 1
                    boss1.boss_hit_count = 0

# setting the game level
if game_level == 1:
    boss_img = 'assets/boss1.gif'
    boss1 = Boss(boss_img)
    turtle.ontimer(boss1.auto_shoot, 1000)  # Start the auto-shoot after 1000 milliseconds (1 second)
elif game_level == 2:
    boss_img1 = 'assets/boss2.gif'
    boss1 = Boss(boss_img1)
    turtle.ontimer(boss1.auto_shoot, 1000)  # Start the auto-shoot after 1000 milliseconds (1 second)


# setting up the screen
screen.title("Space Impact")
screen.setup(width=700, height=500)
screen.bgcolor("#81BB7A")

# draw menu options
draw_menu()
screen.onclick(handle_click)
screen.mainloop()
