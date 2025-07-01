import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def add_task(listbox, entry):
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task(listbox):
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks(listbox):
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)

def create_todo_list(tab_frame):
    # Create input field and buttons
    task_frame = tk.Frame(tab_frame, bg="#f4f4f4")
    task_frame.pack(pady=10)

    task_entry = tk.Entry(task_frame, width=30, font=("Helvetica", 14), bd=2, relief=tk.GROOVE)
    add_button = tk.Button(task_frame, text="Add Task", font=("Helvetica", 12), bg="#00b894", fg="white", padx=10, pady=5,
                           command=lambda: add_task(task_listbox, task_entry))

    # Arrange entry and button horizontally
    task_entry.grid(row=0, column=0, padx=10, pady=10)
    add_button.grid(row=0, column=1, padx=10, pady=10)

    # Create listbox with a scrollbar
    listbox_frame = tk.Frame(tab_frame, bg="#f4f4f4")
    listbox_frame.pack(pady=10)

    scrollbar = tk.Scrollbar(listbox_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    task_listbox = tk.Listbox(listbox_frame, width=50, height=15, font=("Helvetica", 14), bd=2, relief=tk.GROOVE, yscrollcommand=scrollbar.set)
    scrollbar.config(command=task_listbox.yview)
    task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    # Create action buttons
    button_frame = tk.Frame(tab_frame, bg="#f4f4f4")
    button_frame.pack(pady=10)

    delete_button = tk.Button(button_frame, text="Delete Task", font=("Helvetica", 12), bg="#d63031", fg="white", padx=10, pady=5,
                               command=lambda: delete_task(task_listbox))
    clear_button = tk.Button(button_frame, text="Clear All Tasks", font=("Helvetica", 12), bg="#fdcb6e", fg="white", padx=10, pady=5,
                              command=lambda: clear_tasks(task_listbox))

    delete_button.grid(row=0, column=0, padx=10)
    clear_button.grid(row=0, column=1, padx=10)

# Initialize the main application window
root = tk.Tk()
root.title("Multi To-Do Lists")
root.geometry("600x700")
root.resizable(True, True)
root.configure(bg="#f4f4f4")

# Header label
header_label = tk.Label(root, text="Multi To-Do Lists", font=("Helvetica", 24, "bold"), bg="#6c5ce7", fg="white", pady=10)
header_label.pack(fill=tk.X)

# Create notebook for multiple tabs
notebook = tk.ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# Create tabs
for i in range(3):
    tab_frame = tk.Frame(notebook, bg="#f4f4f4")
    notebook.add(tab_frame, text=f"List {i + 1}")
    create_todo_list(tab_frame)

# Start the Tkinter main loop
root.mainloop()