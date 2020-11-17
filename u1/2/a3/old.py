#!/usr/bin/env python3

import turtle as trtl
import random as rand

class Letter(trtl.Turtle):
    def set_letter(self, letter):
        self.letter = letter
    def get_letter(self):
        return self.letter

apple_image = "apple.gif"
pear_image = "pear.gif"
ground = -120
keys = ["A", "B"]#, "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) 
wn.addshape(pear_image) 
wn.bgpic("background.gif")
wn.tracer(False)

def init_apple_pos(active_apple):
    active_apple.shape(apple_image if rand.randint(0,100) % 2 == 1 else pear_image)
    active_apple.goto(rand.randint(-175,175), rand.randint(-25,80))
    wn.update()

def update_letter_pos(active_apple, active_letter):
    active_letter.clear()
    active_letter.goto(active_apple.xcor() - 12, active_apple.ycor() - 30)
    active_letter.color("white")
    active_letter.write(active_letter.get_letter(), font=("Arial", 25, "bold"))

apples, letters = [], []
for _ in range(len(keys)):
    apple = trtl.Turtle()
    apple.penup()
    apples.append(apple)
    init_apple_pos(apple)

    letter = Letter()
    letter.penup()
    letter.hideturtle()
    letter.set_letter(keys.pop(rand.randint(0,len(keys)-1)))
    letters.append(letter)
    update_letter_pos(apple, letter)

def fall(active_apple, active_letter):
    print('Apple {} fell'.format(active_letter.get_letter()))
    active_apple.sety(ground)
    update_letter_pos(active_apple, active_letter)
    wn.update()

for apple, letter in zip(apples,letters):
    print('Mapping key {} to turtle'.format(letter.get_letter().lower()))
    wn.onkeypress(lambda: fall(apple, letter), letter.get_letter().lower())

wn.listen()
trtl.mainloop()
