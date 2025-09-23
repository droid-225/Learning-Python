from tkinter import *

# text widget : basically a text area

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=('Ink Free', 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="blue")
# the font size is directly tied to the size of the text area
text.pack()
button = Button(window, text='submit', command=submit)
button.pack()

window.mainloop()