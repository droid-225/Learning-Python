# entry widget : textbox that accepts a single line of user input

from tkinter import *

def submit():
    text = entry.get() # returns string entered in the entry box
    print("Submission: ", text)
    #entry.config(state=DISABLED) # disables entry box after submission

def delete():
    entry.delete(0, END) # deletes all character from entry box between first value and last value
    print("Entry Box Emptied!")

def backspace():
    entry.delete(len(entry.get()) - 1, END)
    print("BACKSPACE!")

window = Tk()

entry = Entry(window,
              font=('Arial', 50),
              fg="#00FF00",
              bg="black",
              show=";") # shows specific character instead of text, like for passwords
entry.insert(0, 'Say Something!') # sets default text
entry.pack(side=LEFT)

submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="delete",
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                       text="backspace",
                       command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()