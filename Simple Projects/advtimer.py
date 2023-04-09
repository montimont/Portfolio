from tkinter import *
from PIL import Image, ImageTk
from time import strftime, localtime

def update_clock():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)

    zone_string = strftime("%Z")
    zone_label.config(text=zone_string)

    date_string = strftime("%d %B %Y")
    date_label.config(text=date_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    # Schedule the next update after 1 second
    time_label.after(1000, update_clock)


# Create a Tkinter window
window = Tk()

# Create a canvas to display the world map
canvas_width = 600
canvas_height = 400
canvas = Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Load the world map image and display it on the canvas
world_map_image = Image.open("world_map.png")
world_map_photo = ImageTk.PhotoImage(world_map_image)
canvas.create_image(0, 0, anchor=NW, image=world_map_photo)

# Define the GPS location as a tuple of (latitude, longitude) in degrees
gps_location = (43.000000, -75.000000)

# Convert the GPS location to pixel coordinates on the canvas using a simple projection
x = (gps_location[1] + 180) * (canvas_width / 360)
y = (90 - gps_location[0]) * (canvas_height / 180)
gps_marker = canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")

# Create labels to display the date, time, and time zone
time_label = Label(window, font=("Georgia", 50), fg="green")
time_label.pack()

zone_label = Label(window, font=("Georgia", 50), fg="green")
zone_label.pack()

date_label = Label(window, font=("Georgia", 50), fg="green")
date_label.pack()

day_label = Label(window, font=("Georgia", 50), fg="green")
day_label.pack()

# Update the clock and start the Tkinter main loop
update_clock()
window.mainloop()