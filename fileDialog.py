from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\aryan\\Desktop\\Progammin\\Python\\Learning Python",
                                          title="open file okay?",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    # returns the file path of selected file, opens to last opened directory by default
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="open", command=openFile)
button.pack()

window = mainloop()