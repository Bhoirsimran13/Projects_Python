import json
import os

FILENAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("0. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found! ")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("\nEnter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to delete: "))
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed['title']}' deleted.")
        except (ValueError, IndexError):
            print("⚠ Invalid task number. Please try again.")

def mark_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter task number to mark as done: "))
            tasks[task_num - 1]["done"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_num - 1]['title']}' marked as done!")
        except (ValueError, IndexError):
            print("⚠ Invalid task number. Please try again.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("\nEnter choice (0-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "0":
            print("\nExiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
