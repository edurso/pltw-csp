#!/usr/bin/env python3

import turtle as util
import leaderboard as lb
import flappy
import sys

# config
wn = util.Screen()
sc = util.Turtle()
score = flappy.Score(input('Enter Name: '))

# function to launch game
def launch_game() -> None:
    clear_start_screen()
    bird = flappy.init()
    wn.onkeypress(flappy.handle_key, flappy.KEYS.get("UP"))
    wn.onkeypress(flappy.handle_key, flappy.KEYS.get("SPACE"))
    wn.listen()
    score.set(flappy.play_game(bird, sc))
    wn.clear()
    start_screen(False) 

# function to quit game
def quit_game() -> None:
    clear_start_screen()
    wn.clear()
    sys.exit()

# function to show initial screen
def start_screen(first_game) -> None:
    sc.speed('fastest')
    sc.clear()
    leader_names, leader_scores = [], []
    lb.load_leaderboard(flappy.LB_FILE, leader_names, leader_scores)
    if not first_game:
        lb.update_leaderboard(flappy.LB_FILE, leader_names, leader_scores, score.get_name(), score.get())
    lb.draw_leaderboard(leader_names, leader_scores, sc)
    font_setup = ("Arial", 20, "normal")
    sc.penup()
    sc.goto(-200, 200)
    sc.hideturtle()
    sc.down()
    sc.write("Press Space To Start", font=font_setup)
    sc.penup()
    sc.goto(-200, 150)
    sc.down()
    sc.write('Press "q" To Quit', font=font_setup)
    sc.penup()
    sc.goto(-200, 50)
    sc.down()
    sc.write('Leaderboard', font=font_setup)
    wn.onkeypress(launch_game, flappy.KEYS.get("SPACE"))
    wn.onkeypress(quit_game, flappy.KEYS.get("Q"))
    wn.listen()
    wn.mainloop()

# clears start screen and removes text
def clear_start_screen() -> None:
    sc.clear()
    sc.hideturtle()

# APPLICATIONS BEGINS TO RUN HERE
start_screen(True)
