#!/usr/bin/env python3

# Authors: Patrick Halim, Jamie Zhou, Eric D'Urso

import turtle as trtl
import random

corner =  False #True # place holder variable for debugging, set to true to have dvd move to corner

#   background screen
wn = trtl.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("black")

#   list of colors
colors = ["blue", "green", "yellow", "red", "magenta", "purple", "cornflower blue"]

#   add images of dvds with different colors
prefix = "./img/"
ending = "-dvd.gif"
for color in colors:
    image_name = prefix + color + ending
    wn.addshape(image_name)

#   create dvd turtle starting with a random color
dvd = trtl.Turtle()
if not corner:
    dvd.goto(random.randint(100,300), random.randint(-200,200))
dvd.penup()
current_color = random.randint(0,6)
dvd.shape(prefix + colors[current_color] + ending)
dvd.speed(0)

#   configure initial heading using rng for some variability
heading_choices = [45, 135, 225, 315]  
heading = (40 if corner else random.choice(heading_choices))
dvd.setheading(heading)

#   infinite loop to move dvd forward
while True:
    dvd.forward(3)

    #   track coordinates of dvd
    x = dvd.xcor()
    y = dvd.ycor()

    #   change color and direction if dvd touches boundary
    if (x < -314) or (x > 307):
        current_color += 1
        dvd.shape(prefix + colors[current_color % 7] + ending)   #   use current_color % 7 to make the colors can repeat through the list
        heading = 180 - heading
        dvd.setheading(heading)
    if (y < -253) or (y > 257):
        current_color += 1
        dvd.shape(prefix + colors[current_color % 7] + ending)
        heading *= -1
        dvd.setheading(heading)

    #   end / celebration if reaches a corner - check which corner and set heading
    if (x > 302 and y > 255):
        heading = 40
        break
    if (x > 302 and y < - 249): 
        heading = -40
        break
    if (x < -310 and y > 255): 
        heading = 140
        break
    if (x < -310 and y < -249):  
        heading = -140
        break
    

#   create turtles
celebration1 = trtl.Turtle()
celebration1.shape("turtle")
celebration1.speed(0)
celebration1.pencolor(colors[current_color%7])
celebration1.penup()
heading += 90
celebration1.left(heading)
celebration1.goto(1.25*x, 1.25*y)
celebration1.turtlesize(2)

celebration2 = trtl.Turtle()
celebration2.shape("turtle")
celebration2.speed(0)
celebration2.pencolor(colors[(current_color + 1) % 7])  
celebration2.penup()
heading += 180 
celebration2.left(heading)
celebration2.goto(1.25*x, 1.25*y)
celebration2.turtlesize(2)

#   create a function to make turtles leave dots as they go in a circle
def move(turtle):
    n = 0
    while (n < 20):
        turtle.circle(radius,18)
        turtle.dot(dot_size)
        n += 1

#   celebration loop
count = 2
radius = count * 0.2 * abs(x)
dot_size = 10
while (count < 5):   
    #   celebration 1
    move(celebration1)
    radius *= -1.25     #   negative because changing direction of rotation
    dot_size += 5
    #   celebration 2
    move(celebration2)
    radius *= -1.25
    dot_size += 5
    #   repeat
    count += 1
    
wn.mainloop() # steady window