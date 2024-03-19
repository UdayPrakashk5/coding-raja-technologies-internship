import json
import os
from datetime import datetime

# Function to load tasks from file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['title']} - Priority: {task['priority']} - Due Date: {task.get('due_date', 'None')} - {'Completed' if task['completed'] else 'Incomplete'}")

# Function to add a task
def add_task(tasks):
    title = input("Enter task title: ")
    priority = input("Enter priority (high/medium/low): ").lower()
    due_date = input("Enter due date (YYYY-MM-DD) [Optional]: ")
    new_task = {"title": title, "priority": priority, "completed": False}
    if due_date:
        new_task["due_date"] = due_date
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    choice = int(input("Enter the number of the task to remove: "))
    if 1 <= choice <= len(tasks):
        del tasks[choice - 1]
        save_tasks(tasks)
        print("Task removed successfully!")
    else:
        print("Invalid task number!")

# Function to mark a task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    choice = int(input("Enter the number of the task to mark as completed: "))
    if 1 <= choice <= len(tasks):
        tasks[choice - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number!")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. Display tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

    print("Thank you for using the to-do list!")

if _name_ == "_main_":
    main()