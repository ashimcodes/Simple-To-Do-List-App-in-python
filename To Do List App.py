def display_menu():
    print("\nWelcome to the To-Do List App\n")
    print("1. Show current list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    return choice

def show_list(task_list):
    if len(task_list) == 0:
        print("No tasks found.")
    else:
        for i, task in enumerate(task_list):
            print(i+1, ")", task)

def add_task(task_list):
    task = input("Enter a task: ")
    task_list.append(task)
    print("Task added successfully.")

def remove_task(task_list):
    task_index = int(input("Enter the index of the task to remove: "))
    if task_index > 0 and task_index <= len(task_list):
        task_list.pop(task_index-1)
        print("Task removed successfully.")
    else:
        print("Invalid index.")

task_list = []
choice = display_menu()
while choice != 4:
    if choice == 1:
        show_list(task_list)
    elif choice == 2:
        add_task(task_list)
    elif choice == 3:
        remove_task(task_list)
    else:
        print("Invalid choice.")
    choice = display_menu()

print("Goodbye!")
