from tkinter import *
from tkinter import messagebox


root = Tk() # create root widget
root.title("Hello, World")
root.configure(background="yellow")
root.minsize(200, 200)
root.geometry("300x300+50+50") # w 'x' h, +x, +y

# Create Label in our window
text = Label(root, text="Nothing will work unless you do.")
text.pack()
text2 = Label(root, text="- Maya Angelou")
text2.pack()

# Create a button
def onButton():
  print("Button Clicked!")
  messagebox.askokcancel(title="Button Clicked", message="Are you sure?")


button = Button(root, text="Hi", command=onButton)
button.pack()

root.mainloop()
