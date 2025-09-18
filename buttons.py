from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file='shrek.png')

button = Button(window,
                text="Click Me!",
                command=click, # callback to function to be executed on button click
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00", # the active bg and fg are the colors used when button is clicked (active)
                activebackground="black",
                state=ACTIVE, # sets the state of the button, DISABLED stops the button from being clicked ACTIVE by default
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()