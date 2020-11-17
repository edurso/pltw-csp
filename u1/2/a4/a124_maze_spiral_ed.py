#!/usr/bin/env python3

import turtle as trtl
import random as rand

wn = trtl.Screen()
wall = trtl.Turtle()
num_walls = 25
path_width = 20
wall_color = 'black'

def draw_perp_wall(t, path_width):
    t.pendown()
    t.right(90)
    t.forward(path_width)
    t.right(180)
    t.forward(path_width)
    t.right(90)

def init_maze(t, num_walls, path_width, wall_color='black'):
    init = 10
    door_size = path_width
    t.speed('fastest')
    t.left(90)
    t.penup()
    t.goto(path_width, 0)
    t.pendown()
    t.pencolor(wall_color)
    t.pensize(5)
    for n in range(num_walls):
        if(n < 4):
            continue
        wall_size = path_width + init*n
        door_start = rand.randint(0, wall_size)
        door_end = door_start + door_size
        start_wall_location = rand.randint(0, wall_size)
        while door_start < start_wall_location and start_wall_location > door_end:
            start_wall_location = rand.randint(0, wall_size)
        wall_location_end = wall_size - start_wall_location
        seg1 = 0 # 0 to start 1st discontinuity
        seg2 = 0 # length 1st discontinuity
        seg3 = 0 # distance between end of 1st discontinuity and start of 2nd
        seg4 = 0 # length 2nd discontinuity
        seg5 = 0 # distance between end of 2nd discontinuity and end
        if start_wall_location < door_start: # barrier is 1st
            seg1 = start_wall_location
            seg2 = 0
            seg3 = door_start - start_wall_location
            seg4 = door_size
            seg5 = wall_size - seg1 - seg2 - seg3 - seg4
            t.forward(seg1)
            if n < (num_walls - 5):
                draw_perp_wall(t, path_width)
            t.forward(seg2)
            t.forward(seg3)
            t.penup()
            t.forward(seg4)
            t.pendown()
            t.forward(seg5)
            t.left(90)
        else:
            seg1 = door_start
            seg2 = door_size
            seg3 = start_wall_location - door_start
            seg4 = 0
            seg5 = wall_size - seg1 - seg2 - seg3 - seg4
            t.forward(seg1)
            t.penup()
            t.forward(seg2)
            t.pendown()
            t.forward(seg3)
            t.forward(seg4)
            if n < (num_walls - 5):
                draw_perp_wall(t, path_width)
            t.forward(seg5)
            t.left(90)
        #t.forward(start_wall_location)
        #if n < (num_walls - 5):
        #    draw_perp_wall(t, path_width)
        #t.forward(wall_location_end)
        #t.left(90)
    t.hideturtle()

init_maze(wall, num_walls, path_width, wall_color)

wn.mainloop()