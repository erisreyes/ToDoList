import tkinter as tk

# Create a window
window = tk.Tk()
window.title("To-Do List App")

# Create a label for the input field
input_label = tk.Label(window, text="Enter a task:")
input_label.pack()

# Create an input field
input_field = tk.Entry(window)
input_field.pack()

# Create a listbox to display tasks
listbox = tk.Listbox(window)
listbox.pack()

# Define a function to add a task to the listbox
def add_task():
    task = input_field.get()
    listbox.insert(tk.END, task)
    input_field.delete(0, tk.END)

# Create a button to add tasks
add_button = tk.Button(window, text="Add task", command=add_task)
add_button.pack()

# Create a function to remove a task from the listbox
def remove_task():
    task_index = listbox.curselection()[0]
    listbox.delete(task_index)

# Create a button to remove tasks
remove_button = tk.Button(window, text="Remove task", command=remove_task)
remove_button.pack()

# Start the main event loop
window.mainloop()
