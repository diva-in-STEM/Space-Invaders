import turtle
from turtle import Turtle, Screen
import math
import random
import winsound
import time

# Define Globals
player = Turtle()
wn = Screen()
score = 0
scorestring = 'Score: %s' %score

# Register Graphics
turtle.register_shape('enemy.gif')
turtle.register_shape('player.gif')

wn.setup(700, 700)
wn.title('Space Invaders')
wn.bgcolor('black')
wn.bgpic('background.gif')
bp = Turtle()
bp.speed(10)
bp.color('white')
bp.penup()
bp.setposition(-300, -300)
bp.pendown()
bp.pensize(3)
for side in range(4):
        bp.fd(600)
        bp.left(90)
        bp.hideturtle()

en = 10
enemies = []
for i in range(en):
    enemies.append(Turtle())

player.color('blue')
player.speed(10)
player.shape('player.gif')
player.penup()
player.setposition(0, -250)
player.setheading(90)
for enemy in enemies:
    enemy.color('red')
    enemy.shape('enemy.gif')
    enemy.penup()
    enemy.speed(10)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemyspeed = random.randint(2, 10)
    enemy.setposition(x, y)


playerspeed = 15

# Create Player Weapon
bullet = Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(10)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 20
# Define Bullet States
# ready - ready to fire
# fire - bullet is firing
bulletstate = 'ready'

# Scoring
sp = Turtle()
sp.speed(0)
sp.color('white')
sp.penup()
sp.setposition(-290, 280)
sp.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
sp.hideturtle()

# Move the player


def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = - 280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire():
    global bulletstate
    if bulletstate == 'ready':
        bulletstate = 'fire'
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y +10)
        bullet.showturtle()
        winsound.PlaySound('shoot.wav', winsound.SND_ASYNC)


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2))+math.pow(t1.ycor()-t2.ycor(),2)
    if distance < 65:
        return True
    else:
        return False


wn.listen()
wn.onkey(move_left, 'Left')
wn.onkey(move_right, 'Right')
wn.onkey(fire, 'space')


# Main Game Loop
while True:

    # Moving the enemy
    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 10
                e.sety(y)
                winsound.PlaySound('cartoon060.wav', winsound.SND_ASYNC)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 10
                e.sety(y)
                winsound.PlaySound('cartoon060.wav', winsound.SND_ASYNC)
            enemyspeed *= -1

        # Bullet and enemy collision
        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0, -400)
            enemy.hideturtle()
            score = score + 10
            scorestring = 'Score: %s' % score
            sp.clear()
            sp.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
            winsound.PlaySound('invaderkilled.wav', winsound.SND_ASYNC)

        # Player and enemy collision
        if isCollision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            score = score - score
            print('Game Over!')
            winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)
            time.sleep(3)
            exit()

    # Moving the bullet
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Bullet Border Checking
    if bullet.ycor() > 300:
        bullet.hideturtle()
        bulletstate = 'ready'



wn.mainloop()
