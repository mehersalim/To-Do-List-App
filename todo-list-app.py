"""
To-Do List Application (Command Line Interface Version)
This script allows users to manage tasks through a simple command line interface.
Features include adding, viewing, completing, and deleting tasks.
Tasks are saved to a file for persistence between sessions.
"""

import os
import json
from datetime import datetime

# Constants for file operations
TASKS_FILE = "tasks.json"

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns a list of tasks, or an empty list if file doesn't exist or is empty.
    """
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            return tasks
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    """
    Save the current list of tasks to the JSON file.
    Args:
        tasks: List of tasks to be saved
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    """
    Add a new task to the list.
    Args:
        tasks: Current list of tasks
    Returns:
        Updated list of tasks
    """
    title = input("Enter task title: ")
    description = input("Enter task description (optional): ")
    due_date = input("Enter due date (YYYY-MM-DD, optional): ")
    
    # Validate and parse due date
    parsed_date = None
    if due_date:
        try:
            parsed_date = datetime.strptime(due_date, "%Y-%m-%d").isoformat()
        except ValueError:
            print("Invalid date format. Task will be saved without due date.")
    
    new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'due_date': parsed_date,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")
    return tasks

def view_tasks(tasks, show_completed=False):
    """
    Display all tasks in a formatted way.
    Args:
        tasks: List of tasks to display
        show_completed: Whether to show completed tasks
    """
    if not tasks:
        print("No tasks found.")
        return
    
    print("\n--- TASK LIST ---")
    for task in tasks:
        if task['completed'] and not show_completed:
            continue
            
        status = "✓" if task['completed'] else " "
        due_info = f" (Due: {task['due_date']})" if task['due_date'] else ""
        print(f"{task['id']}. [{status}] {task['title']}{due_info}")
        if task['description']:
            print(f"   Description: {task['description']}")
    print("----------------\n")

def complete_task(tasks):
    """
    Mark a task as completed.
    Args:
        tasks: Current list of tasks
    Returns:
        Updated list of tasks
    """
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to mark as complete: "))
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = True
                task['completed_at'] = datetime.now().isoformat()
                save_tasks(tasks)
                print("Task marked as complete!")
                return tasks
        print("Task ID not found.")
    except ValueError:
        print("Please enter a valid number.")
    return tasks

def delete_task(tasks):
    """
    Delete a task from the list.
    Args:
        tasks: Current list of tasks
    Returns:
        Updated list of tasks
    """
    view_tasks(tasks, show_completed=True)
    try:
        task_id = int(input("Enter task ID to delete: "))
        tasks = [task for task in tasks if task['id'] != task_id]
        save_tasks(tasks)
        print("Task deleted successfully!")
        return tasks
    except ValueError:
        print("Please enter a valid number.")
    return tasks

def main():
    """
    Main function to run the To-Do List application.
    Handles user input and menu navigation.
    """
    tasks = load_tasks()
    
    while True:
        print("\nTO-DO LIST MENU")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            tasks = add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            tasks = complete_task(tasks)
        elif choice == '4':
            tasks = delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()