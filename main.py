tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added")

def listTasks():
    if not tasks:
        print("List is empty")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Please enter which number to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
        else:
            print(f"Task #{taskToDelete} was not found")
    except:
        print("Invalid Input")

if __name__ == "__main__":
    ### Create a loop to run app
    print("List starting")
    while True:
        print("\n")
        print("Select one of the options")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List task(s)")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if (choice == "1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")