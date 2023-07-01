from tkinter import *

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

root.mainloop()
