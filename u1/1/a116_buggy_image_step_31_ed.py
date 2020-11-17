#!/usr/bin/env python3
import turtle as trtl

spider = trtl.Turtle()

# Function to Move Spider Without Drawing Anything
def move(x, y):
  spider.penup()
  spider.goto(x, y)
  spider.pendown()

# Draw Body
spider.pensize(40)
spider.circle(20)

# Draw Head
move(50, 15)
spider.circle(5)

# Draw Eyes
spider.pensize(2)
spider.color('red')
move(60, 10)
spider.circle(1)
move(60, 25)
spider.circle(1)
spider.color('black')

# Config Legs
num_legs = 8
leg_length = 70
leg_spacing = 300 / num_legs
spider.pensize(5)

# Draw Some Legs
for curr_leg in range(num_legs//2): 
  move(0, 20)
  spider.setheading(leg_spacing * curr_leg + 45)
  spider.forward(leg_length)

# Draw Some More Legs
for curr_leg in range(num_legs//2): 
  move(0, 20)
  spider.setheading(leg_spacing * curr_leg - 157.5)
  spider.forward(leg_length)  

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()