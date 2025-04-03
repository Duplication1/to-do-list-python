from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="New Task").grid(column=0, row=0)
# input
data = StringVar()
ttk.Entry(frm, textvariable=data).grid(column=0, row=1)

# Create Function
def button_click():
        data.get()
        ttk.Label(frm, textvariable=data).grid(column=0, row=5)
    
# button
ttk.Button(frm, text="Add Task", command=button_click).grid(column=0, row=3)

# MyTask Label
ttk.Label(frm, text="My Task").grid(column=0, row=4)
root.mainloop()