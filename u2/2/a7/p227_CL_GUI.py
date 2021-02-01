# Eric D'Urso
# Nick DaSilva
# Raymond Mei
# Zack Wilk
# Ken Sandburg

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

font = 'bahnschrift' #'webdings'

def do_command(cmd):
    global command_textbox, url_entry
    hostname = url_entry.get()
    print(cmd, hostname)
    full_command = cmd + " " + hostname
    subprocess.call(full_command)
    global command_textbox
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, cmd + " working....\n")
    command_textbox.update()
    p = subprocess.Popen(
        cmd + " ::1", stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )  # v2
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)
    # If url_entry is blank, use localhost IP address
    url_val = url_entry.get()
    if len(url_val) == 0:
        # url_val = "127.0.0.1"
        url_val = "::1"
    p = subprocess.Popen(
        cmd + " ::1", stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )  # v2


# Save function.
def mSave():
    filename = asksaveasfilename(
        defaultextension=".txt",
        filetypes=(
            ("Text files", "*.txt"),
            ("Python files", "*.py *.pyw"),
            ("All files", "*.*"),
        ),
    )
    if filename is None:
        return
    file = open(filename, mode="w")
    text_to_save = command_textbox.get("1.0", tk.END)

    file.write(text_to_save)
    file.close()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10, bg="black")  # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(
    frame_URL,
    text="URL: ",
    compound="center",
    font=(font, 14),
    bd=0,
    relief=tk.FLAT,
    cursor="circle",
    fg="mediumpurple3",
    bg="black",
)
url_label.pack(side=tk.LEFT)
url_entry = tk.Entry(frame_URL, font=(font, 14))  # change font
url_entry.pack(side=tk.LEFT)

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(
    frame, 
    text="Ping", 
    command=lambda:do_command("ping"),
    compound="center",
    font=(font, 12),
    bd=0, 
    relief="flat",
    cursor="trek",
    bg="purple",
    activebackground="white")
ping_btn.pack() 

# Makes the command button pass it's name to a function using lambda
nslookup_btn = tk.Button(
    frame, 
    text="NS Lookup", 
    command=lambda:do_command("nslookup"),
    compound="center",
    font=(font, 12),
    bd=0, 
    relief="flat",
    cursor="trek",
    bg="purple",
    activebackground="white")
nslookup_btn.pack() 

trc_btn = tk.Button(
    frame, 
    text="Trace", 
    command=lambda:do_command("tracert"),
    compound="center",
    font=(font, 12),
    bd=0, 
    relief="flat",
    cursor="trek",
    bg="purple",
    activebackground="white")
trc_btn.pack() 

save_btn = tk.Button(
    frame,
    text="Save",
    command=mSave,
    compound="center",
    font=(font, 12),
    bd=0, 
    relief="flat",
    cursor="shuttle",
    bg="pink",
    activebackground="white"
)
save_btn.pack()

frame = tk.Frame(root, bg="black")  # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()

root.mainloop()
