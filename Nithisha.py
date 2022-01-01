from tkinter import *

root = Tk()


ent = Entry(bg="red",
            fg="white",
            bd=5,
            cursor="dot",
            justify="left",
            selectbackground="yellow",
            selectforeground="green",
            width=20)
ent.pack()

btn = Button(text="Click me")
btn.pack()


bt = Button(text="N")
bt.pack()




root.mainloop()