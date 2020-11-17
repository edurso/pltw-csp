#!/usr/bin/env python3
import turtle as trtl
def move():
    robot.dot(10)
    robot.forward(50)
def turn_left():
    robot.speed(0)
    robot.left(90)
    robot.speed(2)
def turn_right():
    robot.speed(0)
    robot.right(90)
    robot.speed(2)
startx = -100
starty = -100
wn = trtl.Screen()
wn.setup(width=400, height=420)
robot_image = "./robot.gif"
wn.addshape(robot_image)
robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.penup()
robot.pencolor("darkorchid")
robot.setheading(90)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()
wn.bgpic("./maze3.png")


# i = 0
# while (i < 4):
#     turn_right()
#     move()
#     turn_left()
#     move()
#     if i == 1:
#         robot.pencolor("orange")
#     i += 1

def go():
    turn_right()
    move()
    turn_left()
    move()

i = 0
while i < 1:
    j = 0
    while j < 2:
        go()
        j += 1
    robot.pencolor("orange")
    k = 0
    while k < 2:
        go()
        k +=1
    i += 1

wn.mainloop()