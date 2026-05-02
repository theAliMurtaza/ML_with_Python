import json
import os

FILE_NAME = "todo.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except:
            return []  # handle corrupted file
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)   # ✅ FIXED
    save_tasks(tasks)
    print(f"Task '{task}' added successfully.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No task available")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def delete_task(task):
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' deleted successfully.")
    else:
        print(f"Task '{task}' not found.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")      
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task = input("Enter the task to delete: ")
            delete_task(task)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()