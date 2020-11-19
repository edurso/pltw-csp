#!/usr/bin/env python3

import random as rand
import turtle as trtl
import leaderboard as lb
import time

# class for gravity object
class Grav():
    # constructor initilizes values
    def __init__(self, grav, grav_inc, inverse) -> None:
        self.grav = grav
        self.grav_inc = grav_inc
        self.inverse = inverse
    # returns value of gravity multiplier
    def get_grav(self) -> int:
        return self.grav
    # sets gravity multiplier
    def set_grav(self, grav) -> None:
        self.grav = grav
    # increments gravity coefficient
    def increment(self) -> None:
        self.grav += self.grav_inc
    # invert gravity value to make bird go up
    def invert(self) -> None:
        self.grav = self.inverse

# class for a set of pipes
class PipeSet():
    # constructor creates new pipe object and sets its position
    def __init__(self, x, stroke, filepath, pipe_range_low, pipe_range_high, pipe_spacing, top_pipe_path, bottom_pipe_path) -> None:
        self.stroke = stroke
        self.x = x
        self.filepath = filepath 
        height_top = rand.randint(pipe_range_low, pipe_range_high)
        height_bottom = height_top - pipe_spacing 
        self.top = trtl.Turtle(shape=(self.filepath + top_pipe_path))
        self.top.hideturtle()
        self.top.speed('fastest')
        self.top.penup()
        self.top.setx(x)
        self.top.sety(height_top)
        self.top.showturtle()
        self.bottom = trtl.Turtle(shape=(self.filepath + bottom_pipe_path))
        self.bottom.hideturtle()
        self.bottom.speed('fastest')
        self.bottom.penup()
        self.bottom.setx(x)
        self.bottom.sety(height_bottom)
        self.bottom.showturtle()
    # function moves the pipe by the configured step
    def move(self) -> None:
        self.x -= self.stroke
        self.top.setx(self.top.xcor()-self.stroke)
        self.bottom.setx(self.bottom.xcor()-self.stroke)
    # function returns the x position of the pipe set
    def getx(self) -> int:
        return self.x
    # function removes the pipes from view 
    def hide(self) -> None:
        self.top.clear()
        self.top.hideturtle()
        self.bottom.clear()
        self.bottom.hideturtle()

# configure constants
GROUND = -200
LEFT_BORDER = -600
PIPE_STROKE = 5
PIPE_INIT = 150
PIPE_SPACING = 250
SCREEN_WIDTH = 474
SCREEN_HEIGHT = 600
PIPE_LOW = 150
PIPE_HIGH = 350
PIPE_SPACING_VERT = 500
GRAV_COEF = Grav(grav=4,grav_inc=0.6,inverse=-8) # (grav=1,grav_inc=0.03,inverse=-2)
FILEPATH = "./img/"
BIRD_IMG = "bird.gif"
TOP_PIPE_PATH = "top-pipe.gif"
BOTTOM_PIPE_PATH = "bottom-pipe.gif"
BG_IMAGE = "flappy-bird.gif"
LB_FILE = "flappy-leaderboard.txt"

# setup window
wn = trtl.Screen()
wn.screensize(SCREEN_WIDTH,SCREEN_HEIGHT)
wn.bgpic(FILEPATH + BG_IMAGE)
wn.register_shape(FILEPATH + BIRD_IMG)
wn.register_shape(FILEPATH + TOP_PIPE_PATH)
wn.register_shape(FILEPATH + BOTTOM_PIPE_PATH)

# function creates a new pipe object
def new_pipe(pos):
    return PipeSet(pos, PIPE_STROKE, FILEPATH, PIPE_LOW, PIPE_HIGH, PIPE_SPACING_VERT, TOP_PIPE_PATH, BOTTOM_PIPE_PATH)

# config variables
user_score = 0
pipes = []
for i in range(5):
    pipes.append(new_pipe(PIPE_INIT + i*PIPE_SPACING))
bird = trtl.Turtle(shape=(FILEPATH+BIRD_IMG))
bird.penup()

# function to update pipe positions
def update_pipes():
    for pp in pipes:
        pp.move()
        if pp.getx() < LEFT_BORDER:
            pp.hide()
            pipes.remove(pp)
            pipes.append(new_pipe(pipes[len(pipes)-1].getx() + PIPE_SPACING))

# function to update position of bird
def update_bird():
    bird.sety(bird.ycor()-1*GRAV_COEF.get_grav())
    GRAV_COEF.increment()

# function to handle key press events
def handle_key():
    GRAV_COEF.invert()

# function to determine if bird has hit a pipe
def bird_crashed():
    return bird.ycor() < GROUND
    manage_leaderboard()

# game function
def play_game():  
    time.sleep(5)
    while not bird_crashed():
        update_bird()
        update_pipes()

# configure key presses
wn.onkeypress(handle_key, "space")
wn.onkeypress(handle_key, "Up")

# listen key presses
wn.listen()

# play game
play_game()

# main loop
wn.mainloop()