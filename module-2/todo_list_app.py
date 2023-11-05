# Define an empty list to represent the to-do list
todo_list = []

# Function to add a task to the to-do list
def add_task(task):
    todo_list.append(task)
    print("Task added:", task)

# Function to view the tasks in the to-do list
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to remove a task from the to-do list
def remove_task(index):
    if 1 <= index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Removed: {removed_task}")
    else:
        print("Invalid index.")

# Main loop for user interaction
while True:
    print("\nOptions:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_description = input("Enter the task description: ")
        add_task(task_description)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_index = input("Enter the index of the task to remove (or 0 to cancel): ")
        if task_index.isdigit():
            task_index = int(task_index)
            if task_index == 0:
                continue
            remove_task(task_index)
        else:
            print("Invalid input. Please enter a valid index.")
    elif choice == "4":
        print("Exiting the to-do list application.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
