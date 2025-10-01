from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x) + ", " + str(event.y))

window = Tk()

window.bind("<Motion>", doSomething)
# "<Button-1>" : left click
# "<Button-2>" : wheel click
# "<Button-3>" : right click
# "<ButtonRelease>" : button up
# "<Enter>" : when mouse enters window
# "<Leave>" : when mouse leaves window
# "<Motion>" : where the mouse moved, when the mouse moves

window.mainloop()