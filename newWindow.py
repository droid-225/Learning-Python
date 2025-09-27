from tkinter import *

def create_window():
    #new_window = Toplevel() # new window 'on top' of other windows, linked to a 'bottom' window.
    # here, the main window (window) is the bottom level window on top of which the new_window is made.
    # if the bottom window is closed, all windows on top of it are also closed.
    # but if the top level windows are closed, the bottom windows are not affected.

    new_window = Tk() # creates a new independent window
    # closing the main window does not affect the new independent window

    old_window.destroy() # closes the old window

old_window = Tk()

Button(old_window, text="Create New Window", command=create_window).pack()


old_window.mainloop()