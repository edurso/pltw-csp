# a213_multi_factor.py
import tkinter as tk
import a213_multifactorgui as mfg

# create a multi-factor interface to a restircteownlo app
my_auth = mfg.MultiFactorAuth()

# set the users authentication information
question = "What is Nick DaSilva's favorite color"
answer = "seven"
my_auth.set_authorization("admin", "240fa47c09")
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
