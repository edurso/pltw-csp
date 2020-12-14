#!/usr/bin/env python3

import tkinter as tk

# class Window(tk.Tk):
#     def __init__(self):
#         #super.__init__(self)
#         self.wm_geometry('400x400')
#         self.title('App')
#         self.create_widgets()
# 
#     def create_widgets(self):
#         self.blue    = tk.Frame(self.master, bg='blue')
#         self.green   = tk.Frame(self.master, bg='green')
#         self.red     = tk.Frame(self.master, bg='red')
#         self.yellow  = tk.Frame(self.master, bg='yellow')
# 
#         self.blue    .grid(row=0, column=0, rowspan=2, columnspan=2)
#         self.green   .grid(row=0, column=1, rowspan=2, columnspan=1)
#         self.red     .grid(row=1, column=0, rowspan=2, columnspan=2)
#         self.yellow  .grid(row=1, column=1, rowspan=2, columnspan=1)

root = tk.Tk()
root.wm_geometry('400x400')
root.title('App')

main = tk.Frame(root)

blue    = tk.Frame(main, bg='blue')
green   = tk.Frame(main, bg='green')
red     = tk.Frame(main, bg='red')
yellow  = tk.Frame(main, bg='yellow')

blue    .grid(row=0, column=0, rowspan=2, columnspan=2)
green   .grid(row=0, column=1, rowspan=2, columnspan=1)
red     .grid(row=1, column=0, rowspan=2, columnspan=2)
yellow  .grid(row=1, column=1, rowspan=2, columnspan=1)

tk.mainloop()