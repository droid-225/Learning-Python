# listbox: a listing of selectable text items within it's own container

from tkinter import *

def submit():
    food = []

    for index in lb.curselection():
        food.insert(index, lb.get(index))

    print("Your Have Ordered:")

    for index in food:
        print(index)

    #print(lb.get(lb.curselection())) # for single selection

def add():
    lb.insert(lb.size(), entryBox.get())
    lb.config(height=lb.size())  # dynamically changes the height value of the listbox

def delete():
    for index in reversed(lb.curselection()): # the selection needs to be reversed to properly delete selected items
        lb.delete(index)

    # for single selection:
    #lb.delete(lb.curselection()) # curselection is short for current selection
    lb.config(height=lb.size())  # dynamically changes the height value of the listbox

window = Tk()

lb = Listbox(window,
             bg="#f7ffde",
             font=("Constantia", 35),
             width=12,
             selectmode=MULTIPLE) # MULTIPLE option allows for multiple items to be selected as once
lb.pack()

lb.insert(1, "Pizza")
lb.insert(2, "Soup")
lb.insert(3, "Paster")
lb.insert(4, "Garlic Bread")
lb.insert(5, "Salad")

lb.config(height=lb.size()) # dynamically changes the height value of the listbox

submit_button = Button(window,
                       text="submit",
                       command=submit)
submit_button.pack()

entryBox = Entry(window)
entryBox.pack()

add_button = Button(window,
                       text="add",
                       command=add)
add_button.pack()

delete_button = Button(window,
                       text="delete",
                       command=delete)
delete_button.pack()

window.mainloop()