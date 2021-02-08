#!/usr/bin/env python3

import tkinter as tk
import tkinter.scrolledtext as tksc

font = 'bahnschrift'

def encode():
    # read message from textbox

    # convert message to binary

    # write a byte to a pixel in a list

    # make an image from the list of pixels using some random width/heigth component

    # write image *somewhere*

    return None

def decode():
    # read image from filepath

    # convert to one dimensional list of pixels

    # decode each pixel

    # string together for a final message

    # return the message & print to output path
    return None

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
    command=encode,
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
