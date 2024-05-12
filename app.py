"""
todo application
"""
import sys
import utils
import json
from enum import Enum
from uuid import uuid4
from prettytable import PrettyTable
task_table = PrettyTable()
task_table.field_names = ["Task", "Priority", "Id"]

tasks = []


class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class TaskItem:
    def __init__(self, name, priority, id):
        self.name = name
        self.priority = priority
        self.id = id


def load_tasks_from_file():
    # default_task = TaskItem("Welcome to Taskpulse",
    #                         Priority.HIGH.value, uuid4())
    # tasks = [default_task]
    try:
        task_file = open("tasks.json", "r")
        task_data = json.load(task_file)
        for task in task_data:
            task_item = TaskItem(task["name"], task["priority"], task["id"])
            tasks.append(task_item)
    except Exception as e:
        print(f"error {e} occurred")
    finally:
        return tasks


def save_tasks_to_file() -> None:
    task_dictionary_list = []
    for task in tasks:
        task_dict = task.__dict__.copy()
        task_dict["id"] = str(task_dict["id"])
        task_dictionary_list.append(task_dict)
    task_file = open("tasks.json", "w")
    json.dump(task_dictionary_list, task_file)


def initial_setup() -> None:
    global tasks
    tasks = load_tasks_from_file()
    save_tasks_to_file()


def display_welcome_message() -> None:
    print("Welcome to Taskpulse")


def get_user_selection() -> int:
    user_selection = input("Selection: ")
    return int(user_selection)


def display_tasks() -> None:
    for task in tasks:
        task_table.add_row([task.name, task.priority, task.id])
    print(task_table)
    task_table.clear_rows()


def add_task() -> None:
    no_of_tasks = int(input("Enter the number of tasks: "))
    for i in range(no_of_tasks):
        print(f"Task {i+1}:")
        name = input("Enter task name: ")
        priority = input("Enter task priority: ")
        id = uuid4()
        task = TaskItem(name, priority, id)
        tasks.append(task)
    save_tasks_to_file()
    print("task(s) successfully added")


def delete_task() -> None:
    global tasks
    id = input("Enter task id: ")
    tasks = list(filter(lambda task_item: task_item.id != id, tasks))
    print("delete task")


def display_menu() -> None:
    print("1. Display tasks")
    print("2. Create a task")
    print("3. Delete a task")
    print("4. Exit")


def run_menu() -> None:
    display_menu()
    user_selection = get_user_selection()
    utils.clear_console()
    if user_selection == 1:
        display_tasks()
    elif user_selection == 2:
        add_task()
    elif user_selection == 3:
        delete_task()
    elif user_selection == 4:
        sys.exit()


def main() -> None:
    initial_setup()
    display_welcome_message()
    while True:
        run_menu()


main()
