from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="New Task").grid(column=0, row=0)
# input
data = StringVar()
ttk.Entry(frm, textvariable=data).grid(column=0, row=1)

#listbox
task_listbox = Listbox(frm, width=40)
task_listbox.grid(column=0, row=7)




# Create Function
def button_click():
        task = data.get()
        if task:
                task_listbox.insert(END, task)
                data.set("")

#add button
ttk.Button(frm, text="Add Task", command=button_click).grid(column=0, row=3)
# MyTask Label
ttk.Label(frm, text="My Task").grid(column=0, row=6)


#click label identify the index of it 

#delete function
def delete_task():
        selection = task_listbox.curselection()
        task_listbox.delete(selection)

#insert the delete button
ttk.Button(frm, text="delete Task", command=delete_task).grid(column=0, row=4)

#update task function
def update_task():
        #something
#insert update button
ttk.Button(frm, text="Update Task", command=update_task).grid(column=0, row=5)

root.mainloop()