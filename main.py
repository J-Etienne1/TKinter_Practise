

# https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&ab_channel=thenewboston


# LESSON 1 - INTRODUCTION

"""
from tkinter import *

root = Tk()
theLabel = Label(root, text="Simple Message \n" * 10)
theLabel.pack()
root.mainloop()
"""


# LESSON 2 - Organizing your Layout
"""
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

## adding buttons/widgits
button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="green")
button4 = Button(bottomFrame, text="Button 4", fg="purple")

## now that created we need to specify that we want to dsplay them
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


root.mainloop()
"""



# LESSON 3 - Fitting Widgets in your Layout
"""
from tkinter import *
root = Tk()

one = Label(root, text='One', bg='red', fg='white')
one.pack()

two = Label(root, text='two', bg='green', fg='black')
two.pack(fill=X)

three = Label(root, text='three', bg='red', fg='white')
three.pack(side=LEFT, fill=Y)

root.mainloop()
"""



# LESSON 4 + 5 - Grid Layout + More on the Grid Layout
"""
from tkinter import *
root = Tk()

label_1 = Label(root, text='Name')
label_2 = Label(root, text='Password')

entry_1 = Entry(root)
entry_2 = Entry(root)


label_1.grid(row=0, sticky=E) # E = East i.e right aligned
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text='Keep me logged in')
c.grid(columnspan=2)


root.mainloop()
"""


# LESSON 6 - Binding Functions to Layouts

from tkinter import *
root = Tk()



root.mainloop()
















