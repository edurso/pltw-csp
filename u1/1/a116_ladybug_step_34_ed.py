#!/usr/bin/env python3

import turtle as trtl

# draw legs, THIS CODE IS REUSED FROM THE SPIDER STEP, though there have been some minor changes

spider = trtl.Turtle()

# Function to Move Spider Without Drawing Anything
def move(x, y):
  spider.penup()
  spider.goto(x, y)
  spider.pendown()

# Config Legs
num_legs = 6
leg_length = 55
leg_spacing = 300 / num_legs
spider.pensize(5)

# Draw Some Legs
for curr_leg in range(num_legs//2): 
  move(0, -33)
  spider.setheading(leg_spacing * curr_leg - 60)
  spider.forward(leg_length)

# Draw Some More Legs
for curr_leg in range(num_legs//2): 
  move(0, -33)
  spider.setheading(-leg_spacing * curr_leg + 240)
  spider.forward(leg_length)

spider.hideturtle()

# END REUSED CODE

# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  ypos += 25 # This read xpos = ypos + 25 : this was the first bug, should be setting ypos not xpos
  xpos += 5 # This read xpos = xpos + 5 : though not a bug, I changed this because I think it is better.
  num_dots += 1 # This read num_dot = num_dots + 1 : this was the second bug, should set num_dots not num_dot

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()