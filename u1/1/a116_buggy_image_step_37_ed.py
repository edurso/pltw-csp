#!/usr/bin/env python3
import turtle as trtl

spider = trtl.Turtle()
spider.speed(0)

# Function to Move Spider Without Drawing Anything
def move(x, y):
  spider.penup()
  spider.goto(x, y)
  spider.pendown()

# Draw Body
move(0, 0)
spider.pensize(40)
spider.circle(20)

# Draw Head
move(0, -40)
spider.circle(5)

# Draw Eyes
spider.pensize(1)
spider.color('red')
move(-10, -35)
spider.circle(3)
move(5, -35)
spider.circle(3)

# Config Legs
num_legs = 4#8
spider.pensize(5)
spider.color('black')

# Draw Legs
for leg in range(num_legs):
  # One Side
  move((leg * 5), (leg * -10))
  spider.setheading(70 + (leg * 10))
  spider.circle(50, 200)
  # Other Side
  move((leg * -5), (leg * 10))
  spider.setheading(240 + (leg * 10))
  spider.circle(50, -200)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
