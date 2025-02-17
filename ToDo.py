tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


print("~~TO-DO List~~")
load_tasks()

def show_menu():
    print("\nMenu:", "1 - Add task", "2 - Remove task", "3 - Edit task", "4 - View tasks", "5 - Exit", sep="\n")


def add_task():
    task = input("\nEnter a task: ")
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' has been added to list")


def remove_task():
    view_task()
    '''task = input("Enter task to remove: ")
    assert isinstance(tasks.lower().remove, object)'''

    try:
        index = int(input("\nEnter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks()
            print(f"Task {removed_task} has been removed")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter valid number!!")


def edit_task():
    view_task()
    try:
        index = int(input("\nEnter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] = input("Enter edited task: ")
            save_tasks()
            print(f"Task number {index+1}, {tasks[index]} has been edited")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number!!")



def view_task():
    if not tasks:
        print("No tasks added")
    else:
        print("\nYour to-do list: ")
        i = 1
        for task in tasks:
            print(f"{i}. {task}")
            i += 1

def exit_program():
    print("\nExiting...!")
    global running
    running = False

menu_choice = {
    "1": add_task,
    "2": remove_task,
    "3": edit_task,
    "4": view_task,
    "5": exit_program
}

running = True

while running:
    show_menu()
    choice = input("\nEnter your choice: ")

    action = menu_choice.get(choice)
    if action:
        action()
    else:
        print("Invalid choice, please try again!")
