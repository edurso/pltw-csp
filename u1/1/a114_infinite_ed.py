#!/usr/bin/env python3
import turtle as trtl
painter = trtl.Turtle()
painter.penup()
painter.goto(-200, 0)
painter.pendown()
x = -200
y = 0
move_x = 1
move_y = 1
while True:
    while (x < 200):
        while (y < 100):
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = -1
        while (y > 0):
            x += move_x
            y += move_y
            painter.goto(x, y)
        move_y = 1
    while (x > -200):
        while (y > -100):
            x -= move_x
            y -= move_y
            painter.goto(x, y)
        move_y = -1
        while (y < 0):
            x -= move_x
            y -= move_y
            painter.goto(x, y)
        move_y = 1
wn = trtl.Screen()
wn.mainloop()
