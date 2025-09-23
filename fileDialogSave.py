from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", '.txt'),
                                        ("HTML file", '.html'),
                                        ("All files", '.*')
                                    ],
                                    initialdir="C:\\Users\\aryan\\Desktop\\Progammin\\Python\\Learning Python")
    if file is None:
        return
    filetext = str(text.get('1.0', END))
    #filetext = input("Enter some text:") # getting input from console (takes a second to come up)
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()