#!/usr/bin/env python3
import turtle as trtl

# Initialize Turtle
spider = trtl.Turtle()

# Draw Body
spider.pensize(40)
spider.circle(20)

# Configure Spider/Variables for Drawing Legs
num_legs = 6
leg_length = 70
leg_spacing = 380 / num_legs
# print("z=", leg_spacing)
spider.pensize(5)

# Draw Legs
for curr_leg in range(num_legs): 
  spider.goto(0,0)
  spider.setheading(leg_spacing * curr_leg)
  spider.forward(leg_length)
  # print("z*n=", leg_spacing * curr_leg)

# Goodbye Turtle!
spider.hideturtle()

# Continue Showing Screen . . .
wn = trtl.Screen()
wn.mainloop()