#!/usr/bin/env python3

import tkinter as tk
import numpy as np # NumPy
import cv2 # OpenCV

# decodes message from given filepath
def decode():
    global command_textbox # get output textbox
    path = get_path() # get path where encoded file is
    command_textbox.delete(1.0, tk.END) # clear output
    command_textbox.insert(tk.END, 'Reading encoded message from ' + path + '\n') # let user know we are readint the message
    command_textbox.update() # update textbox
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE) # read image matrix from path
    msg = np.array(img).flatten() # flatten image
    msg = msg[msg != 0] # filter out added zeros
    #print(msg) # debug
    msg_final = ''.join([chr(m) for m in msg]) # splice together all the characters from the numbers
    #print(msg_final) # debug
    command_textbox.delete(1.0, tk.END) # clear textbox
    command_textbox.insert(tk.END, 'Decoded message:\n' + msg_final + '\n') # print decoded message
    command_textbox.update() # update textbox