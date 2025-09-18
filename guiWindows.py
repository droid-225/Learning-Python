# widgets : GUI elements like buttons, textboxes, labels, images, etc.
# windows : serves as a container to hold or contain these widgets

from tkinter import *

window = Tk() # instantiate an instance of a window
window.geometry("420x420")
window.title("First GUI")

icon = PhotoImage(file='shrek.png') # converts image into a photoimage to be used as a icon
window.iconphoto(True, icon)
window.config(background="#5cffcf") # can be set to a color name or hex value

window.mainloop() # places window on screen and listens to events
