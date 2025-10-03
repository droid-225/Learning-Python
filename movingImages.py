from tkinter import *

speed = 10

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-speed)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+speed)

def move_left(event):
    label.place(x=label.winfo_x()-speed, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+speed, y=label.winfo_y())

window = Tk()
window.geometry("500x500")

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

myImage = PhotoImage(file='skull.png')
label = Label(window, image=myImage,)
label.place(x=0, y=0)

window.mainloop()