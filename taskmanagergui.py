import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
    else:
        messagebox.showwarning("Warning", "No task selected!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        task_listbox.insert(tk.END, f'{task["task"]} [{status}]')

def clear_all_tasks():
    tasks.clear()
    update_tasks()

# Create the main window
root = tk.Tk()
root.title("Task Manager")
root.configure(bg="#f0f0f0")

# Create and place the widgets
task_label = tk.Label(root, text="Enter a task:", bg="#f0f0f0")
task_label.pack(pady=5)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#f44336", fg="white")
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task, bg="#2196F3", fg="white")
complete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all_tasks, bg="#9E9E9E", fg="white")
clear_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Start the main loop
root.mainloop()
