I chose to use Python's tkinter and time packages to create my clock because they provided the most efficient way to make a user-friendly interface for a clock with time, time zone, date, and time of day elements. Tkinter offered a variety of methods to create a GUI for the clock, and the time package had a rich set of functions that allowed me to access the time and date elements needed for the clock. Furthermore, the time package also provided options to easily access and update the time zone and time of day elements essential for this clock.

In addition, I fooled around with making a GPS tracker based upon a given location. You can see the code below.


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
