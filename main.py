

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



# LESSON 3