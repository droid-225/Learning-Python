from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
x_vel = 3
y_vel = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bg_photo = PhotoImage(file="cemetary.png")
bg = canvas.create_image(0, 0, image=bg_photo, anchor=NW)

pimage = PhotoImage(file="skull.png")
skull = canvas.create_image(0, 0, image=pimage, anchor=NW)

img_width = pimage.width()
img_height = pimage.height()

while True:
    coordinates = canvas.coords(skull)
    print(coordinates)

    if(coordinates[0] >= (WIDTH - img_width) or coordinates[0] < 0):
        x_vel *= -1

    if(coordinates[1] >= (HEIGHT - img_height) or coordinates[1] < 0):
        y_vel *= -1

    canvas.move(skull, x_vel, y_vel)
    window.update()
    time.sleep(0.01)

window.mainloop()