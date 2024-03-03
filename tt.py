todo_list = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully!")
    elif choice == '2':
        task = input("Enter the task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found!")
    elif choice == '3':
        if todo_list:
            print("Your To-Do List:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
        else:
            print("Your To-Do List is empty!")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
