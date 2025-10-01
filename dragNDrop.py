from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x # makes a new variable for label called startX and assigns it the current x value of the mouse
    widget.startY = event.y # same but for y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    # label.winfo_x() gets top left coordinate of label relative to window
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, bg="red", width=10, height="5")
label.place(x=0, y=0)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2 = Label(window, bg="blue", width=10, height="5")
label2.place(x=100, y=100)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

window.mainloop()