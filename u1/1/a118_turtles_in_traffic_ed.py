#!/usr/bin/env python3

# Move turtles horizontally and vertically across screen.
# Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes and colors
horiz_colors = ["orchid", "blue", "green", "darkorchid", "purple", "gold"]
vert_colors = ["darkgreen", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 75
for hc, vc in zip(horiz_colors, vert_colors):
    # turtle for horizontal axis
    ht = trtl.Turtle(shape='turtle')
    horiz_turtles.append(ht)
    ht.speed(0)
    ht.penup()
    ht.fillcolor(hc)
    ht.goto(-475, tloc)
    ht.setheading(0)
    # turtle for vertical axis
    vt = trtl.Turtle(shape='turtle')
    vert_turtles.append(vt)
    vt.speed(0)
    vt.penup()
    vt.fillcolor(vc)
    vt.goto(-tloc, 475)
    vt.setheading(270)
    # increase turtle location on next iteration
    tloc += 75

# move turtles across and down screen, stopping for collisions
steps = 0
step_size = 5
while steps < 80:
    # detect collisions
    for ht, vt in zip(horiz_turtles, vert_turtles):
        # check if ht has hit vt
        if( ( abs(ht.xcor() - vt.xcor()) < 20 ) and ( abs(ht.ycor() - vt.ycor()) < 20 ) ):
            # oh no, they crashed
            ht.fillcolor('red')
            ht.shape('circle')
            vt.fillcolor('red')
            vt.shape('circle')
            step_size_small = 1
            ht.speed(3)
            vt.speed(3)
            back = 10
            vfwd = 40
            hfwd = back + vfwd
            # move them around each other
            for i in range(back):
                ht.goto(ht.xcor() - step_size_small, ht.ycor())
            for i in range(vfwd):
                vt.goto(vt.xcor(), vt.ycor() -  step_size_small)
            for i in range(hfwd):
                ht.goto(ht.xcor() + step_size_small, ht.ycor())
            ht.speed(0)
            vt.speed(0)
            # keep turtles red to indicate they have crashed, but change back to normal shape
            ht.shape('turtle')
            vt.shape('turtle')
        # move turtles
        else:
            ht.goto(ht.xcor() + step_size, ht.ycor())
            vt.goto(vt.xcor(), vt.ycor() - step_size)
    steps += 1

for t in (horiz_turtles + vert_turtles):
    t.shape('turtle')
    t.color('green')

wn = trtl.Screen()
wn.mainloop()

