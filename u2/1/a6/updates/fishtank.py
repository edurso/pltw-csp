
import tkinter as tk
import tkinter.messagebox as mb
import os

#
#    Module fishtank.py
#      (c) 2019 PLTW 
#
#    Monitors important fish tank settings to keep your salt water
#    tank in optimal health
#

# import factors to monitor
import alkalinity 
import calcium 
import magnesium
import ph 
import phosphate
import salinity
import temperature

class FishTank(tk.Tk):

  # check fish tank enviornment factors
  #  - ph levels should be between 8.1 and 8.3
  #  - alkalinity should be between 7 and 12 
  #  - salinity should be between 28 and 35
  #  - temperature range should be 50 to 75
  #  - calcium should between 380 and 445
  #  - magnesium should be between 1250 and 1350
  #  - phosphate should be less than .3
  #
  def monitor(self):

    msg = "ENVIRONMENTAL FACTORS:\n"
    msg = msg + ph.monitor() + "\n"
    msg = msg + alkalinity.monitor() + "\n"
    msg = msg + salinity.monitor() + "\n"
    msg = msg + temperature.monitor() + "\n"
    msg = msg + "\nTRACE CHEMICALS:\n"
    msg = msg +  calcium.monitor() + "\n"
    msg = msg + magnesium.monitor() + "\n"
    msg = msg + phosphate.monitor()

    mb.showinfo("Status Check", msg)

  # the GUI for the monitoring software
  def __init__(self):
    tk.Tk.__init__(self)
    
    # reference a png to use as teh backround image
    dirname = os.path.dirname(__file__)
    print(dirname)
    tank_picture = os.path.join(dirname, 'tank.png')

    self.title("Fish Tank Monitor")
    self.geometry("750x500") # size of tank image
    self.image_tank = tk.PhotoImage(file=tank_picture)

    self.background = tk.Label(self, image=self.image_tank)
    self.background.image = self.image_tank  
    #self.background = tk.Label(self, background="aqua") # debug only
    self.background.pack(fill="both", expand=True)

    self.frame_info = tk.Frame(self.background, background="white")
    self.frame_info.pack(pady=75)

    font_setup = ("Arial", 20, "bold")
    self.lbl_username = tk.Label(self.frame_info, font=font_setup, background="white", text="Fish Tank Monitor")
    self.lbl_username.pack(pady=5)

    font_setup = ("Arial", 16, "normal")
    self.lbl_username = tk.Label(self.frame_info, background="white", text="Current Status:\n All factors OK")
    self.lbl_username.pack(pady=5)

    self.btn_login = tk.Button(self.frame_info, text="Perform Manual Check", command=self.monitor)
    self.btn_login.pack(pady=20, padx=20)
    