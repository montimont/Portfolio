from tkinter import *
from time import *

def update():
  time_string = strftime("%H:%M:%S")
  time_label.config(text=time_string)

  zone_string = strftime("%Z")
  zone_label.config(text = zone_string)

  date_string = strftime("%d %B %Y")
  date_label.config(text = date_string)

  day_string = strftime("%A")
  day_label.config(text = day_string)

  time_label.after(1000,update)


window = Tk()

time_label = Label(window, font=("Georgia",50), fg="green")
time_label.pack()

zone_label = Label(window, font=("Georgia",50), fg="green")
zone_label.pack()

date_label = Label(window, font=("Georgia",50), fg="green")
date_label.pack()

day_label = Label(window, font=("Georgia",50), fg="green")
day_label.pack()

update()

window.mainloop()
