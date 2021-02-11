#!/usr/bin/env python3

import tkinter as tk
import math
import numpy as np # NumPy
import cv2 # OpenCV

# encodes a given message and saves it to the given filepath
def encode():
    global msg_ent # message entry textbox
    global command_textbox # output textbox
    command_textbox.delete(1.0, tk.END) # clear output
    command_textbox.insert(tk.END, 'Encoding message . . .\n') # let user know we are encoding the message
    command_textbox.update() # update output
    msg_str = msg_ent.get() # get the message from user as a string
    msg_ascii = [ord(c) for c in msg_str] # make list of ordnial values of each character in message
    # print(msg_ascii) # debug
    size = int(math.sqrt(len(msg_ascii)))+1 # determine needed size of matrix
    mat = np.zeros((size, size), dtype=int, order='C') # maze an empty 2d matrix of zeros
    n = 0 # counter for msg ord
    for i in range(0,mat.shape[0]): # go through all rows
        for j in range(0,mat.shape[1]): # go through all columns
            #print('mat[{}][{}] = acsii[{}]'.format(i,j,n)) # debug
            if not len(msg_ascii) == 0: # while there are still ords in msg
                mat[i][j] = msg_ascii[0] # add first element of message to matrix
                del msg_ascii[0] # delete first element
            else:
                break # stop if message has already been converted
            n += 1 # inc counter
    #print(mat, '\nEMPTY: {}'.format(msg_ascii)) # debug
    #print('Encoded: {}'.format(mat)) # debug
    path = get_path() # get save path
    cv2.imwrite(path, mat) # write matrix to filepath
    command_textbox.delete(1.0, tk.END) # clear output
    command_textbox.insert(tk.END, 'Saved image to ' + path + '\n') # let user know where we saved the file
    command_textbox.update() # update output