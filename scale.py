from tkinter import *

def submit():
    print("The temperature is " + str(scale.get()) + " degrees F")

window = Tk()

photo = PhotoImage(file='skull.png')

hotLabel = Label(image=photo)
hotLabel.pack()

scale = Scale(window,
              from_=100, # lower bound, top value
              to=0, # upper bound, bottom value
              length=500,
              orient=VERTICAL, # orientation of scale, VERTICAL by default
              font=("Consolas", 20),
              tickinterval=10, # intervals on side of scale
              showvalue=1, # hides exact value of slider if 0, 1 by default
              troughcolor='#69EAFF', # changes the color of the slider trough
              fg="#FF1C00",
              bg="black")
scale.set(((scale['from'] - scale['to']) / 2) + scale['to']) # initial value

scale.pack()

coldLabel = Label(image=photo)
coldLabel.pack()

button = Button(window,
                text="submit",
                command=submit)
button.pack()

window.mainloop()