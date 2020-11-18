#!/usr/bin/env python3

from getkey import getkey, keys # https://github.com/kcsaff/getkey
import random as rand
import turtle as trtl
import time

# init config
filepath = "./img/"
bird_image = "bird.gif"
pipe_top_image = "pipe-top.gif"
pipe_bottom_image = "pipe-bottom.gif"
bg_image = "bg.gif"

# setup window

# function to update position of bird

# main event loop
while True:
    key = getkey()
    if key == keys.SPACE or key == keys.UP:
        # update bird pos
