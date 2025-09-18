from tkinter import *

food = ["pizza", "hamburder", "hotdog"]

def order():
    if(x.get() == 0):
        print("You Chose Pizza!")
    elif (x.get() == 1):
        print("You Chose Hamburger!")
    elif (x.get() == 2):
        print("You Chose Hotdog!")

window = Tk()

photo = PhotoImage(file="skull.png")
foodImages = [photo, photo, photo] # imagine these are different images lol

x = IntVar()

for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],
                               variable=x, # groups radio buttons if they share the same variable
                               value=i, # assigns each radio button a different value
                               padx=25,
                               font=("Impact", 30),
                               image=foodImages[i],
                               compound="left",
                               indicatoron=0, # removed circle indicators
                               width=375, # sets width of radio buttons
                               command=order)
    radio_button.pack(anchor=W) # anchor sets the direction of alignment

window.mainloop()