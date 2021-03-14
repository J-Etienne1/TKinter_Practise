# https://www.youtube.com/watch?v=RJB1Ek2Ko_Y&ab_channel=thenewboston


####################### LESSON 1 - INTRODUCTION

"""
from tkinter import *

root = Tk()
theLabel = Label(root, text="Simple Message \n" * 10)
theLabel.pack()
root.mainloop()
"""

####################### LESSON 2 - Organizing your Layout
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

####################### LESSON 3 - Fitting Widgets in your Layout
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

####################### LESSON 4 + 5 - Grid Layout + More on the Grid Layout
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

####################### LESSON 6 - Binding Functions to Layouts / Events

"""
from tkinter import *
root = Tk()

def printName():
    print('Hello my name is Jason')


button_1 = Button(root, text='Print my name', command = printName)
button_1.pack()

root.mainloop()
"""

# another way to bind functions to widgets maybe a better approach using EVENTS

"""
from tkinter import *
root = Tk()

def printName(event):
    print('Hello my name is Jason')


button_1 = Button(root, text='Print my name')
button_1.bind('<Button-1>', printName)
button_1.pack()

root.mainloop()
"""

####################### LESSON 7 - Mouse Click Events
"""
from tkinter import *
root = Tk()

def leftClick(event):
    print('Left')

def MiddleClick(event):
    print('Middle')

def RightClick(event):
    print('Right')


frame = Frame(root, width=300, height=250)
frame.bind('<Button-1>', leftClick)
frame.bind('<Button-2>', MiddleClick)
frame.bind('<Button-3>', RightClick)


frame.pack()

root.mainloop()
"""

####################### LESSON 8 - Mouse Click Events
"""
from tkinter import *


class Buttons:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text='Print Message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print('Wow, this actually worked')


root = Tk()
b = Buttons(root)

root.mainloop()
"""





####################### LESSON 9 - Creating Drop Down Menus
"""
from tkinter import *

def doNothing():
    print('I dont work yet....')

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project....', command=doNothing)
subMenu.add_command(label='New', command=doNothing)
subMenu.add_command(label='New Scratch File', command=doNothing)
subMenu.add_command(label='Open.....', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Settings', command=doNothing)
subMenu.add_command(label='File Properties', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=doNothing)


editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=doNothing)
editMenu.add_command(label='Redo', command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Cut', command=doNothing)
editMenu.add_command(label='Copy', command=doNothing)


root.mainloop()
"""



####################### LESSON 10 - Creating a Toolbar
"""
from tkinter import *

def doNothing():
    print('I dont work yet....')

root = Tk()

# ********* Main Menu *********

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project....', command=doNothing)
subMenu.add_command(label='New', command=doNothing)
subMenu.add_command(label='New Scratch File', command=doNothing)
subMenu.add_command(label='Open.....', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Settings', command=doNothing)
subMenu.add_command(label='File Properties', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=doNothing)


editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=doNothing)
editMenu.add_command(label='Redo', command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Cut', command=doNothing)
editMenu.add_command(label='Copy', command=doNothing)

# ********* The Toolbar *********

toolbar = Frame(root, bg='magenta')

insertStuff = Button(toolbar, text='Insert Image', command=doNothing)
insertStuff.pack(side=LEFT, padx= 2, pady=2)
printStuff = Button(toolbar, text='Print', command=doNothing)
insertStuff.pack(side=LEFT, padx= 2, pady=2)

toolbar.pack(side=TOP,fill=X) #x/y need to be in CAPS


root.mainloop()
"""




####################### LESSON 11 - Adding the Status Bar
"""
from tkinter import *

def doNothing():
    print('I dont work yet....')

root = Tk()

# ********* Main Menu *********

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project....', command=doNothing)
subMenu.add_command(label='New', command=doNothing)
subMenu.add_command(label='New Scratch File', command=doNothing)
subMenu.add_command(label='Open.....', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Settings', command=doNothing)
subMenu.add_command(label='File Properties', command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=doNothing)


editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=doNothing)
editMenu.add_command(label='Redo', command=doNothing)
editMenu.add_separator()
editMenu.add_command(label='Cut', command=doNothing)
editMenu.add_command(label='Copy', command=doNothing)

# ********* The Toolbar *********

toolbar = Frame(root, bg='magenta')

insertStuff = Button(toolbar, text='Insert Image', command=doNothing)
insertStuff.pack(side=LEFT, padx= 2, pady=2)
printStuff = Button(toolbar, text='Print', command=doNothing)
insertStuff.pack(side=LEFT, padx= 2, pady=2)

toolbar.pack(side=TOP,fill=X) #x/y need to be in CAPS


# ********* Status Bar *********


status = Label(root, text='Preparing to do nothing....', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
"""



####################### LESSON 12 - Messagebox
"""
from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Tile', 'Would you like to Exit?')

answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces?')

if answer == 'yes':
    print(' 8==D~ ')

root.mainloop()
"""



####################### LESSON 13 - Shapes and Graphics

























