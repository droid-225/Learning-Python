from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='Info Message Box', message='You are a person.')
    #messagebox.showwarning(title='Warning Message Box', message='You are a person!')
    #messagebox.showerror(title='Error!', message='You are a person?')

    #if messagebox.askokcancel(title='Ask Ok Cancel', message='You are a person.'):
    #    print('You agree!')
    #else:
    #    print('You are still a person!')

    #if messagebox.askretrycancel(title='Ask Retry Cancel', message='Wan\'t to try that again?'):
    #    print('You did it again!')
    #else:
    #    print('You gave up!')

    #if messagebox.askyesno(title='Ask Yes No', message='Are you a person?'):
    #    print('You are a person!')
    #else:
    #    print('You are not a person!')

    #answer = messagebox.askquestion(title='ask question', message='Do you like pie?') # returns a string
    #if answer == 'yes':
    #    print("Yippie!")
    #else:
    #    print("Y tho?")

    answer = messagebox.askyesnocancel(title='ask yes no cancel', message='Do you like to code?', icon='error')
    if answer:
        print("Yay!")
    elif answer == False:
        print("You should!")
    else:
        print("Answer the question!")

window = Tk()

button = Button(window, command=click, text='Click Me!')
button.pack()

window.mainloop()