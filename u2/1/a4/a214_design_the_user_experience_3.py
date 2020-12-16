#!/usr/bin/env python3

# @authors: Eric D'Urso, Nick DaSilva, Zachary Wilk, Arhant Gill 

import tkinter as tk

root = tk.Tk()
root.wm_geometry("400x400")
root.title("POG Awesome Color Grid")

blue_frame = tk.Frame(root, height=200, width=300, background="blue")
blue_frame.grid(column=0, row=0)

red_frame = tk.Frame(root, height=200, width=300, background="red")
red_frame.grid(column=0, row=1)

lime_frame = tk.Frame(root, height=200, width=100, background="lime")
lime_frame.grid(column=1, row=0) 

yellow_frame = tk.Frame(root, height=200, width=100, background="yellow")
yellow_frame.grid(column=1, row=1) 

root.mainloop()
