# To-Do List CLI Application
# Add, view, and remove tasks

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\n--- YOUR TASKS ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

while True:
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting To-Do App...")
        break
    else:
        print("Invalid choice")