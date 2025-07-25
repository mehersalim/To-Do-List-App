# To-Do List CLI Application
## Developer: Meher Salim

![Python](https://img.shields.io/badge/python-3.6%2B-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple command-line To-Do List application written in Python that helps you manage your tasks efficiently.

## Features

- Add new tasks with titles, descriptions, and due dates
- View all your pending tasks in an organized list
- Mark tasks as completed
- Delete tasks you no longer need
- Automatic saving of tasks to a JSON file for persistence
- Optional due dates with validation
- Timestamps for task creation and completion

## Installation

1. Ensure you have Python 3.6 or later installed
2. Clone this repository or download the script directly
   ```bash
   git clone https://github.com/yourusername/todo-cli.git
   cd todo-cli

## Usage

Run the script with Python:
bash
python todo.py

Menu Options:
  1. Add Task: Create a new task with optional description and due date
  2. View Tasks: Display all your pending tasks
  3. Mark Task as Complete: Check off completed tasks
  4. Delete Task: Remove tasks you no longer need
  5. Exit: Quit the application
The application automatically saves your tasks to tasks.json in the same directory.

## File Structure

![image](https://github.com/user-attachments/assets/b2637d66-50d3-4a81-8bec-fb6618c697c5)

## Requirements

- Python 3.6+
- No external dependencies required

## Data Storage

Tasks are stored in tasks.json with the following structure for each task:

json

![image](https://github.com/user-attachments/assets/6fd6bbc0-e94b-4915-bf9f-f26d9320381d)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License.
