# label : an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()

photo = PhotoImage(file='shrek.png')

label = Label(window, # size of widget accommodates all components inside of it
              text="Hello World!",
              font=('Arial', '40', 'bold'),
              fg='#00FF00', # fg means foreground color (text color), it can take color names or hex values
              bg='black', # bg means background color, it can take color names or hex values
              relief=RAISED, # relief is the border style
              bd=10, # border width in px
              padx=20, # padding between label x value and border
              pady=20, # padding between label y value and border
              image=photo, # places an image into the label
              compound='bottom') # sets location of image in relation to text
label.pack() # places widget on top center of the window
#label.place(x=0, y=0) # places widget in specified location in window (based on top left corner)

window.mainloop()