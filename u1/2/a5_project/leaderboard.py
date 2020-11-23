#!/usr/bin/env python3

# function to load leaderboard from file
def load_leaderboard(file_name, leader_names, leader_scores):
    with open(file_name, 'r') as leaderboard_file:
        for line in leaderboard_file:
            leader_name, leader_score = list(map(str, line.strip().split(',')))
            leader_names.append(leader_name)
            leader_scores.append(int(leader_score))

# function to update leaderboard file
def update_leaderboard(file_name, leader_names, leader_scores, player_name, player_score):
    leader_index = 0
    while (leader_index < len(leader_scores)):
        if (player_score >= leader_scores[leader_index]):
            break
        else:
            leader_index += 1
    leader_scores.insert(leader_index, player_score)
    leader_names.insert(leader_index, player_name)
    if (len(leader_names) == 6):
        leader_names.pop()
    if (len(leader_scores) == 6):
        leader_scores.pop()
    with open(file_name, "w") as leaderboard_file:
        leader_index = 0
        while (leader_index < len(leader_names)):
            leaderboard_file.write(leader_names[leader_index] + "," + str(leader_scores[leader_index]) + "\n")
            leader_index += 1

# function to draw leaderboard
def draw_leaderboard(leader_names, leader_scores, turtle_object):
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-200, 0)
    turtle_object.hideturtle()
    turtle_object.down()
    leader_index = 0
    while leader_index < len(leader_names):
        turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(leader_scores[leader_index]), font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-200, int(turtle_object.ycor())-50)
        turtle_object.down()
        leader_index += 1
