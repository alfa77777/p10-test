import tkinter as tk
from tkinter import messagebox
import pickle


def delete_task():
    if len(list_box.curselection()) != 0:
        task_index = list_box.curselection()[0]
        list_box.delete(task_index)
    else:
        tk.messagebox.showwarning('are you mazgi', 'you must select task')


def save_task():
    tasks = list_box.get(0, list_box.size())
    pickle.dump(tasks, open('tasks.dat', 'wb'))


def load_tasks():
    tasks = pickle.load(open('tasks.dat', 'rb'))
    for task in tasks:
        list_box.insert(tk.END, task)


def add_task():
    task = task_name_entry.get()
    if task != '':
        list_box.insert(tk.END, task)
        task_name_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Are you mazgi', 'You must enter task to add')


window = tk.Tk()
window.title('To-do app by devdavlat')

# Frame list
frame_window = tk.Frame(window)
frame_window.pack()
# Scroll bar
scroll_bar = tk.Scrollbar(frame_window, width=10)
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

# List box
list_box = tk.Listbox(frame_window, height=10, width=50)
list_box.pack(side=tk.RIGHT)

list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

# Task name entry
task_name_entry = tk.Entry(window, width=50)
task_name_entry.pack()

# Add button
add_button = tk.Button(window, text="Add", width=48, command=add_task)
add_button.pack()

# Delete button
add_button = tk.Button(window, text="Delete", width=48, command=delete_task)
add_button.pack()

# Save button
add_button = tk.Button(window, text="Save", width=48, command=save_task)
add_button.pack()

# Tasks list button
add_button = tk.Button(window, text="Show done task", width=48, command=load_tasks)
add_button.pack()

if __name__ == "__main__":
    window.mainloop()
