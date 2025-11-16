TASK_FILE = "tasks.txt"

def add_task():
    task = input("Enter task: ")
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")
    print("Task added!\n")

def view_tasks():
    print("\n=== Your Tasks ===")
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.\n")
                return
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        print()
    except FileNotFoundError:
        print("No tasks found.\n")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()

        if 1 <= task_no <= len(tasks):
            del tasks[task_no - 1]
            with open(TASK_FILE, "w") as file:
                file.writelines(tasks)
            print("Task deleted!\n")
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

while True:
    print("==== To-Do LIST APP ====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option! Try Again.\n")
