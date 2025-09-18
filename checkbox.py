from tkinter import *

def display():
    #if (x.get() == 1):
    #    print("YOU AGREE!!!!")
    #else:
    #    print("YOU DON'T AGREE!")
    if (x.get()):
        print("Agree!")
    else:
        print("Don't Agree!")

window = Tk()

x = BooleanVar() # initializes x as an boolean value
#x = IntVar() # initializes x as an integer value

photo = PhotoImage(file="skull.png")

check_button = Checkbutton(window,
                           text="I agree!",
                           variable=x, # variable to be set when check box is checked
                           onvalue=True, # value when checked (on), 1 by default
                           offvalue=False, # value when unchecked (off), 0 by default
                           command=display,
                           font=('Arial', 20),
                           fg="#00FF00",
                           bg="black",
                           activebackground="black",
                           activeforeground="#00FF00",
                           padx=25,
                           pady=10,
                           image=photo,
                           compound="right")
check_button.pack()

window.mainloop()