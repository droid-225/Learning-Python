from tkinter import *

speed = 10

def move_up(event):
    canvas.move(myImage, 0, -speed)

def move_down(event):
    canvas.move(myImage, 0, speed)

def move_left(event):
    canvas.move(myImage, -speed, 0)

def move_right(event):
    canvas.move(myImage, speed, 0)

window = Tk()

# WASD 
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

# Arrow Keys
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file="skull.png")
myImage = canvas.create_image(0, 0, image=photoimage, anchor=NW)

window.mainloop()