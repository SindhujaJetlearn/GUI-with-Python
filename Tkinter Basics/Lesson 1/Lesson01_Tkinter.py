# import everything from tkinter module
from tkinter import *

# create a tkinter window
root = Tk()

#output window size
root.geometry('500x500')

# Create a Button
btn = Button(root, text="Click Me !", bd='5' , background="cyan",command=root.destroy)

# Set the position of button on the top of window.
#try side = bottom, right, left,top
btn.pack(side="bottom")

root.mainloop()





