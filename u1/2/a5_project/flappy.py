#!/usr/bin/env python3

from getkey import getkey, keys # https://github.com/kcsaff/getkey
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
    def get_grav(self):
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

class PipeSet():
    def __init__(self, x, y) -> None:
        self.top = trtl.Turtle(shape=(filepath+"top_pipe.gif"))
        self.bottom = trtl.Turtle(shape=(filepath+"bottom_pipe.gif"))

# configure constants
GROUND = -200
GRAV_COEF = Grav(grav=1,grav_inc=0.03,inverse=-2)

# init config
filepath = "./img/"
bird_image = "bird.gif"
bg_image = "flappy-bird.gif"
leaderboard_file = "flappy-leaderboard.txt"
user_score = 0

# setup window
wn = trtl.Screen()
wn.screensize(474,600)
wn.bgpic(filepath + bg_image)
wn.register_shape(filepath + bird_image)

# config variables
bird = trtl.Turtle(shape=(filepath+bird_image))
bird.penup()

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

# game function
def play_game():  
    while not bird_crashed():
        update_bird()
        # Update Floor/ Pipe Positions

# configure key presses
wn.onkeypress(handle_key, "space")
wn.onkeypress(handle_key, "Up")

# listen key presses
wn.listen()

# play game
play_game()

# main loop
wn.mainloop()