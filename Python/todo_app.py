def show_menu():
    print("\n----- TO-DO LIST -----")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)  # list method
    print("Task added!")


def mark_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index] += " ✔️"
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)  # list method
                print("Task deleted.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
