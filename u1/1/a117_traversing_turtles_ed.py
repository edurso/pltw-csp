#!/usr/bin/env python3

#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = [ "arrow", "turtle", "circle", "square", "triangle", "classic", "turtle", "circle", "square", "triangle", "classic" ]
turtle_colors = [ "red"  , "blue"  , "green" , "orange", "purple"  , "gold"   , "green" , "orange", "purple", "gold"    , "blue"    ]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)

# initialize turtle position placeholders
startx = -100
starty = 100
heading = 45
distance = 100

# make all the turtles move in a pattern
for t in my_turtles:
  color = turtle_colors.pop()
  t.pensize(5)
  t.fillcolor(color)
  t.pencolor(color)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.setheading(heading)    
  t.forward(distance)

  # increment variables so next turtle goes somewhere else	
  startx = t.xcor()
  starty = t.ycor()
  heading = t.heading() - (32 + (8 / 11))
  distance += 25

wn = trtl.Screen()
wn.mainloop()