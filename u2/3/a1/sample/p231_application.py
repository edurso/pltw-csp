#!/usr/bin/env python3

import tkinter as tk
import tkinter.scrolledtext as tksc
import os
import p231_custom_encoder

font = 'bahnschrift' # global font

# get file path from user
def get_path():
    global fpath_ent # file path entry
    return os.path.join(fpath_ent.get(), 'encoded.bmp') # the saved image file will be named 'encoded.bmp'

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
