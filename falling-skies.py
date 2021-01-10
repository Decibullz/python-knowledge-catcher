#  falling skies in python 3 

import turtle
import random

wn = turtle.Screen()
wn.title("Falling Skies by Cody Snell")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)


#  add the player
# lowercase letters by convention
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0,-250)
player.direction="stop"

# create a list of good guys
good_guys = []

# Add the good guys
for _ in range(15):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.penup()
    good_guy.goto(0,250)
    good_guy.speed = random.randint(1 ,2)
    good_guys.append(good_guy)


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
        x -= 1
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 1
        player.setx(x)

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
        if good_guy.distance(player) < 20:
            x = random.randint(-300,300)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
wn.mainloop()