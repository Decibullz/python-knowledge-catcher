#  falling skies in python 3 

import turtle

wn = turtle.Screen()
wn.title("Falling Skies by Cody Snell")
wn.bgcolor("green")
wn.setup(width=800, height=600)


#  add the player
# lowercase letters by convention
player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0,-250)






wn.mainloop()