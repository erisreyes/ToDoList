import json

# Define the file name
filename = "tasks.json"

# Load the tasks from the file
try:
    with open(filename, "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

def view_task():
    # View all the tasks in the list
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")


# Create a loop that allows the user to add, edit, or delete tasks
while True:
    # Display options to the user
    print("1. Add task")
    print("2. Edit task")
    print("3. Delete task")
    print("4. View tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Handle user's choice
    if choice == "1":
        # Add a new task to the list
        task = input("Enter task: ")
        tasks.append(task)

        # Write the tasks to the file
        with open(filename, "w") as f:
            json.dump(tasks, f)

        print('\n********')
        view_task()
    elif choice == "2":
        # Edit an existing task in the list
        index = int(input("Enter task number: ")) - 1
        new_task = input("Enter new task: ")
        tasks[index] = new_task

        # Write the tasks to the file
        with open(filename, "w") as f:
            json.dump(tasks, f)
    elif choice == "3":
        view_task()

        # Delete an existing task from the list
        print('\n')
        index = int(input("Enter task number: ")) - 1
        del tasks[index]

        # Write the tasks to the file
        with open(filename, "w") as f:
            json.dump(tasks, f)
    elif choice == "4":
        view_task()

        # Ask the user if they want to display options again
        print('\n********')
        display_options = input("Do you want to display options again? (y/n): ")
        if display_options.lower() == "y":
            print('\n')
            continue
        else:
            break
    elif choice == "5":
        # Exit the loop
        break
    else:
        print("Invalid choice. Please try again.")



