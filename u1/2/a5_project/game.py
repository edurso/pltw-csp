#!/usr/bin/env python3

import random as rand
import turtle as util
import leaderboard as lb
import sys
import flappy
import time

# config
wn = util.Screen()
sc = util.Turtle()
score = flappy.Score()

# function to launch game
def launch_game() -> None:
    clear_start_screen()
    bird = flappy.init()
    wn.onkeypress(flappy.handle_key, flappy.KEYS.get("UP"))
    wn.onkeypress(flappy.handle_key, flappy.KEYS.get("SPACE"))
    wn.listen()
    score.set(flappy.play_game(bird))
    wn.clear()
    start_screen() 

# function to quit game
def quit_game() -> None:
    clear_start_screen()
    wn.clear()
    sys.exit()

# function to show initial screen
def start_screen() -> None:
    # TODO: Draw Leaderboard
    font_setup = ("Arial", 20, "normal")
    sc.speed('fastest')
    sc.clear()
    sc.penup()
    sc.goto(-200, 100)
    sc.hideturtle()
    sc.down()
    sc.write("Press Space To Start", font=font_setup)
    sc.penup()
    sc.goto(-200, 50)
    sc.down()
    sc.write('Press "q" To Quit', font=font_setup)
    wn.onkeypress(launch_game, flappy.KEYS.get("SPACE"))
    wn.onkeypress(quit_game, flappy.KEYS.get("Q"))
    wn.listen()
    wn.mainloop()

# clears start screen and removes text
def clear_start_screen() -> None:
    sc.clear()
    sc.hideturtle()

# APPLICATIONS BEGINS TO RUN HERE
# TODO: take name as input for leaderboard
start_screen()
