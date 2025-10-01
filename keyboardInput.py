from tkinter import *

def doSomething(event):
    # print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>", doSomething) # ("<key>", function)
# using "<Key>" allows function activation for any key pressed

label = Label(window, font=("Helvetica", 100))
label.pack()

window.mainloop()