#!/usr/bin/env python3

import tkinter as tk
import tkinter.scrolledtext as tksc
import math
import numpy as np # NumPy
import os
import cv2 # OpenCV

font = 'bahnschrift' # global font

# get file path from user
def get_path():
    global fpath_ent # file path entry
    return os.path.join(fpath_ent.get(), 'encoded.bmp') # the saved image file will be named 'encoded.bmp'

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

# root window
root = tk.Tk()
root.title('MSG')

# encod frame
encode_frame = tk.Frame(root, pady=10, bg='white')
encode_frame.pack()

# message label
msg_lbl = tk.Label(
    encode_frame,
    text='Enter Message: ',
    font=(font, 12),
    cursor='trek',
    fg='white',
    bg='black'
)
msg_lbl.pack()

# message textbox
msg_ent = tk.Entry(encode_frame, font=(font, 12))
msg_ent.pack()

# encode button
encode_btn = tk.Button(
    encode_frame,
    text='Encode Message',
    command=encode,
    font=(font, 12),
    bg='green',
    fg='white',
    cursor='trek'
)
encode_btn.pack()

# decode frame
decode_frame = tk.Frame(root, pady=10, bg='black')
decode_frame.pack()

# file path label
fpath_lbl = tk.Label(
    decode_frame,
    text='Enter Encoded Matrix Filepath: ',
    font=(font, 12),
    cursor='trek',
    fg='black',
    bg='white'
)
fpath_lbl.pack()

# file path entry
fpath_ent = tk.Entry(decode_frame, font=(font, 12))
fpath_ent.pack()

# button to decode message
decode_btn = tk.Button(
    decode_frame,
    text='Decode Message',
    command=decode,
    font=(font, 12),
    bg='red',
    fg='black',
    cursor='trek'
)
decode_btn.pack()

# output frame
out_frame = tk.Frame(root, pady=10, bg='white')
out_frame.pack()

# output textbox
command_textbox = tksc.ScrolledText(out_frame, height=10, width=100)
command_textbox.pack()

# run main thread
root.mainloop()
