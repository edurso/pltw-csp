#!/usr/bin/env python3
import turtle as trtl
painter = trtl.Turtle()
painter.speed(0)
painter.shape("circle")
painter.hideturtle()
painter.penup()
y = 200
while (y > -200): 
  y -= 50
  x = -200
  painter.goto(x,y)
  painter.color("purple")
  painter.stamp()
  while (x < 200):
    x += 50
    painter.goto(x,y)
    painter.color("orange")
    painter.stamp()
wn = trtl.Screen()
wn.mainloop()