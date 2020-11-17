#!/usr/bin/env python3

# imports
import turtle as trtl
import random as rand
from getkey import getkey # https://github.com/kcsaff/getkey

# letter turtle
class Letter(trtl.Turtle):
    def set_letter(self, letter):
        self.letter = letter
    def get_letter(self):
        return self.letter

# apple turtle
class Apple(trtl.Turtle):
    def set_apple_type(self, apple_type):
        self.apple_type = apple_type
    def get_apple_type(self):
        return self.apple_type

# image locations
apple_image = "apple.gif"
pear_image = "pear.gif"

# position of ground on screen
ground = -120

# alphabet
keys_ = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# number of apples on tree at any given time
num_apples = 5

# init screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 
wn.addshape(pear_image) 
wn.bgpic("background.gif")
wn.tracer(False)

# function to init apple position and shape
def init_apple_pos(active_apple):
    active_apple.set_apple_type(apple_image if rand.randint(0,100) % 2 == 1 else pear_image)
    active_apple.shape(active_apple.get_apple_type())
    active_apple.goto(rand.randint(-175,175), rand.randint(-25,80))
    wn.update()

# function to update a letters position relative to an apple
def update_letter_pos(active_apple, active_letter):
    active_letter.clear()
    active_letter.goto(active_apple.xcor() - 12, active_apple.ycor() - 30)
    active_letter.color("white")
    active_letter.write(active_letter.get_letter(), font=("Arial", 25, "bold"))

# function to make an apple "fall" to the ground
def fall(active_apple, active_letter):
    active_apple.sety(ground)
    update_letter_pos(active_apple, active_letter)
    wn.update()

# function to duplicate an apple at its fallen location
def show_fallen(active_apple):
    fallen = trtl.Turtle()
    fallen.penup()
    fallen.shape(active_apple.get_apple_type())
    fallen.goto(active_apple.xcor(), active_apple.ycor())

# apple / letter lists
apples, letters = [], []

# init program's apples and letters
for _ in range(num_apples):
    apple = Apple()
    apple.penup()
    apples.append(apple)
    init_apple_pos(apple)
    letter = Letter()
    letter.penup()
    letter.hideturtle()
    letter.set_letter(keys_.pop(rand.randint(0,len(keys_)-1)))
    letters.append(letter)
    update_letter_pos(apple, letter)

# main game loop
while True:
    # get key pressed (if any)
    key = getkey() 

    # search all apple/letter pairs for a matching key
    for apple, letter in zip(apples,letters):
        if key == letter.get_letter().lower():

            # if keypressed matches an apple's letter, the apple falls 
            fall(apple, letter)

            # a new apple is now on the tree, while the fallen one remains letterless on ground
            keys_.append(letter.get_letter())
            show_fallen(apple)
            init_apple_pos(apple)
            letter.set_letter(keys_.pop(rand.randint(0,len(keys_)-1)))
            update_letter_pos(apple, letter)
