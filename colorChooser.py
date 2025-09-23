from tkinter import *
from tkinter import colorchooser # colorchooser is a sub-module and is not included in *

def click():
    #color = colorchooser.askcolor() # returns rgb and hex value of selected color in a tuple
    #colorHex = color[1] # 1 is the index of the hex value
    window.config(bg=colorchooser.askcolor()[1])

window = Tk()

window.geometry('420x420')
button = Button(text="Click Me!", command=click)
button.pack()

window.mainloop()