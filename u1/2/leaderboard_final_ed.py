#!/usr/bin/env python3

# set the levels of scoring
bronze_score = 15
silver_score = 20
gold_score = 25

# load leaderboard from file
def load_leaderboard(file_name, leader_names, leader_scores):
    with open(file_name, 'r') as leaderboard_file:
        for line in leaderboard_file:
            leader_name, leader_score = list(map(str, line.strip().split(',')))
            leader_names.append(leader_name)
            leader_scores.append(int(leader_score))

# update leaderboard by inserting the current player and score to the list at the correct position
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

# draw leaderboard and display a message to player
def draw_leaderboard(leader_names, leader_scores, high_scorer, turtle_object, player_score):

    # clear the screen and move turtle object to (-200, 100) to start drawing the leaderboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-200, 100)
    turtle_object.hideturtle()
    turtle_object.down()
    leader_index = 0

    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'
    while leader_index < len(leader_names):
        turtle_object.write(str(leader_index + 1) + "\t" + leader_names[leader_index] + "\t" + str(
            leader_scores[leader_index]), font=font_setup)
        turtle_object.penup()
        turtle_object.goto(-200, int(turtle_object.ycor())-50)
        turtle_object.down()
        leader_index = leader_index + 1

    # display message about player making/not making leaderboard based on high_scorer
    if (high_scorer):
        turtle_object.write(
            "Congratulations! You made the leaderboard!", font=font_setup)
    else:
        turtle_object.write(
            "Sorry, you didn't make the leaderboard. Maybe next time!", font=font_setup)

    # move turtle to a new line
    turtle_object.penup()
    turtle_object.goto(-200, int(turtle_object.ycor())-50)
    turtle_object.pendown()

    # display a gold/silver/bronze message if player earned a gold/silver/or bronze medal; display nothing if no medal
    if (player_score >= bronze_score and player_score < silver_score):
        turtle_object.write("... Bronze medal!", font=font_setup)
    elif (player_score >= silver_score and player_score < gold_score):
        turtle_object.write("... Silver medal!", font=font_setup)
    elif (player_score >= gold_score):
        turtle_object.write("... Gold medal!", font=font_setup)
