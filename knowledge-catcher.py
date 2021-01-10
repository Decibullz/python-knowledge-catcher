#  falling skies in python 3 

import turtle
import random
import os
import time

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Knowledge Catcher by Cody Snell")
wn.bgcolor("green")
wn.bgpic('background.gif')
wn.setup(width=800, height=600)
wn.tracer(0)

wn.register_shape("book.gif")
wn.register_shape("spike_ball.gif")
wn.register_shape("brain.gif")

#  add the player
# lowercase letters by convention
player = turtle.Turtle()
player.speed(0)
player.shape("brain.gif")
player.penup()
player.goto(100,-250)
player.direction="stop"

# create a list of good guys
good_guys = []

# Add the good guys
for _ in range(15):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("book.gif")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(100,250)
    good_guy.speed = random.randint(1 , 4)
    good_guys.append(good_guy)

bad_guys = []

for _ in range(10):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.shape("spike_ball.gif")
    bad_guy.color("red")
    bad_guy.penup()
    bad_guy.goto(-100,250)
    bad_guy.speed = random.randint(1 , 4)
    bad_guys.append(bad_guy)

# make the pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")
pen.shape("circle")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Knowledge: {} , Lives: {}".format(score, lives), align="center", font=font)
# functions

def go_left():
    player.direction = "left"

def go_right():
    player.direction = "right"

def go_nowhere():
    player.direction = "stop"

wn.listen()

wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_nowhere, "Up")




while True:
    wn.update()

    # move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)

    # check for border collision

    if player.xcor() > 390:
        player.setx(390)
    
    elif player.xcor() < -390:
        player.setx(-390)

    # Move the good guy
    # good_guy.sety(good_guy.ycor() - .25)
    for good_guy in good_guys:
        y = good_guy.ycor()
        y-= good_guy.speed
        good_guy.sety(y)
        if y < -300:
            x = random.randint(-300,300)
            y = random.randint(300, 400)
            good_guy.goto(x, y)

        # check for collision
        if good_guy.distance(player) < 30:
            x = random.randint(-300,300)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            os.system("afplay page_turn.wav&")
            score += 10
            pen.clear()
            pen.write("Knowledge: {} , Lives: {}".format(score, lives), align="center", font=font)



    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y-= bad_guy.speed
        bad_guy.sety(y)
        if y < -300:
            x = random.randint(-300,300)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
        

        # check for collision
        if bad_guy.distance(player) < 30:
            os.system("afplay page_tear.wav&")
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Knowledge: {} , Lives: {}".format(score, lives), align="center", font=font)
            time.sleep(1)
            for bad_guy in bad_guys:
                x = random.randint(-300,300)
                y = random.randint(300, 400)
                bad_guy.goto(x, y)

        if lives == 0:
            pen.clear()
            pen.write("Game Over! Knowledge: {}".format(score), align="center", font=("Courier", 24, "normal"))
            for good_guy in good_guys:
                good_guy.goto(100,250)

            for bad_guy in bad_guys:
                bad_guy.goto(-100,250)
            wn.update()
            time.sleep(5)
            score = 0
            lives = 3  

            pen.clear()
            pen.write("Knowledge: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

wn.mainloop()