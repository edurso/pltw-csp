#!/usr/bin/env python3

import tkinter as tk
import tkinter.scrolledtext as tksc
import math
import numpy as np
import os
import cv2

font = 'bahnschrift'

def get_path():
    global fpath_ent
    return os.path.join(fpath_ent.get(), 'generated.jpg')

def encode():
    global msg_ent
    global command_textbox
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, 'Encoding message . . .\n')
    command_textbox.update()
    msg_str = msg_ent.get()
    msg_ascii = [ord(c) for c in msg_str]
    print(msg_ascii)
    size = int(math.sqrt(len(msg_ascii)))
    mat = np.zeros((size+1, size+1), dtype=int, order='C')
    n = 0
    for i in range(0,mat.shape[0]):
        for j in range(0,mat.shape[1]):
            #print('mat[{}][{}] = acsii[{}]'.format(i,j,n))
            if not len(msg_ascii) == 0:
                mat[i][j] = msg_ascii[0]
                del msg_ascii[0]
            else:
                break
            n += 1
    #print(mat, '\nEMPTY: {}'.format(msg_ascii))
    #print('Encoded: {}'.format(mat))
    path = get_path()
    img = cv2.imwrite(path, mat)
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, 'Saved image to ' + path + '\n')
    command_textbox.update()

def decode():
    global command_textbox
    path = get_path()
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, 'Reading encoded message from ' + path + '\n')
    command_textbox.update()
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    msg = np.array(img).flatten()
    msg = msg[msg > 5]
    print(msg)
    msg_final = ''.join([chr(m) for m in msg])
    #print(msg_final)
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, 'Decoded message:\n' + msg_final + '\n')
    command_textbox.update()

root = tk.Tk()
root.title('MSG')

encode_frame = tk.Frame(root, pady=10, bg='white')
encode_frame.pack()

msg_lbl = tk.Label(
    encode_frame,
    text='Enter Message: ',
    font=(font, 12),
    cursor='trek',
    fg='white',
    bg='black'
)
msg_lbl.pack()

msg_ent = tk.Entry(encode_frame, font=(font, 12))
msg_ent.pack()

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

decode_frame = tk.Frame(root, pady=10, bg='black')
decode_frame.pack()

fpath_lbl = tk.Label(
    decode_frame,
    text='Enter Encoded Matrix Filepath: ',
    font=(font, 12),
    cursor='trek',
    fg='black',
    bg='white'
)
fpath_lbl.pack()

fpath_ent = tk.Entry(decode_frame, font=(font, 12))
fpath_ent.pack()

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

out_frame = tk.Frame(root, pady=10, bg='white')
out_frame.pack()

command_textbox = tksc.ScrolledText(out_frame, height=10, width=100)
command_textbox.pack()

root.mainloop()
