#!/usr/bin/env python3

# @authors: Eric D'Urso, Nick DaSilva, Zachary Wilk, Arhant Gill 

import tkinter as tk

font = 'Courier'

def test_my_button():
    auth_frame.tkraise()
    usr_pwd_lbl = tk.Label(auth_frame, text=pwd_ent.get(), font=font)
    usr_pwd_lbl.pack()

# main window
root = tk.Tk()
root.wm_geometry('200x150')
root.title('Authorization')

login_frame = tk.Frame(root)
login_frame.grid(row=0, column=0, sticky='news')

username_lbl = tk.Label(login_frame, text='Username:', font=font)
username_lbl.pack()

username_ent = tk.Entry(login_frame, bd=3)
username_ent.pack(pady=5)

pwd_lbl = tk.Label(login_frame, text='Password:', font=font)
pwd_lbl.pack()

pwd_ent = tk.Entry(login_frame, bd=3, show='*')
pwd_ent.pack(pady=5)

login_btn = tk.Button(login_frame, text='Login', command=test_my_button)
login_btn.pack()

auth_frame = tk.Frame(root)
auth_frame.grid(row=0, column=0, sticky='news')

login_frame.tkraise()

root.mainloop()