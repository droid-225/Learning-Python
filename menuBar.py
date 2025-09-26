from tkinter import *

def openfile():
    print("You opened a file!")

def savefile():
    print("The file has been saved.")

def cut():
    print("You cut some text.")

def copy():
    print("You copied some text.")

def paste():
    print("You pasted some text.")

window = Tk()

openImage = PhotoImage(file="skull.png") # imagine these are different
saveImage = PhotoImage(file="skull.png")
exitImage = PhotoImage(file="skull.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
# set tearoff to 1 if you don't remember what it is
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openfile, image=openImage, compound='left')
fileMenu.add_command(label="Save", command=savefile, image=saveImage, compound='left')
fileMenu.add_separator() # puts line between options
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound='left')

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()