#!/usr/bin/env python3

from getkey import getkey, keys # https://github.com/kcsaff/getkey
import random as rand
import turtle as trtl
import leaderboard as lb
import time 

# init config
filepath = "./img/"
bird_image = "bird.gif"
pipe_top_image = "top_pipe.gif"
pipe_bottom_image = "bottom_pipe.gif"
bg_image = "flappy-bird.gif"
floor_image = "floor.gif"
leaderboard_file = "flappy-leaderboard.txt"
pipes = [] 

# setup window
wn = trtl.Screen()
wn.register_shape(filepath + pipe_top_image)
wn.register_shape(filepath + pipe_bottom_image)
#wn.register_shape(filepath + bg_image)
#wn.register_shape(filepath + floor_image)

top_pipe = trtl.Turtle(shape= filepath + pipe_top_image)
top_pipe.penup()
top_pipe.setx(200)
pipes.append(top_pipe)
bottom_pipe = trtl.Turtle(shape= filepath + pipe_bottom_image)
bottom_pipe.penup()
bottom_pipe.setx(200)
pipes.append(bottom_pipe)


# Animated background
# https://healeycodes.com/bf53663c1cd5c3e03cf4a29bce51856e/flappy-bird.gif

# function to update the position of the pipes
def move_pipes():
    for pp in pipes: 
        pp.setx(pp.xcor() - 1) 
# function to update position of bird

# function to determine if bird has hit a pipe
def bird_crashed():
    return False

# function to randomize pipe positions 
def random_pipe(): 
    height_top = rand.randint(100, 200)
    height_bottom = height_top - 50 
    pipes[0].sety(height_top)
    pipes[1].sety(height_bottom)

# game function
def play_game():
    random_pipe()
    while not bird_crashed():
        move_pipes()
        # update bird pos

# Add a point when the bird passes pipe
 
def points():
    points = 0
    if (bottom_pipe.xcor() <= bird.xcor()):
        points += 1

def update_leaderboard():
    # leaderboard variables
    leader_names_list = []
    leader_scores_list = []
    player_name = input ("Please enter your name:")

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
    global leader_scores_list
    global leader_names_list
    global score
    global spot

    # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

# play game
play_game()

# main loop
wn.mainloop()