def display_action():  
    # Display the action to be taken
    print("====To-do List====")
    print("1. Add task")
    print("2. Delete task")
    print("3. Mark task as done")
    print("4. Exit")

def display_tasks(tasks):
    # Display current tasks with their status
    if tasks:
        print("Current tasks:")
        for task in tasks:
            print(f" - {task['task']} [{'Done' if task['done'] else 'Pending'}]")
    else:
        print("No tasks available.")

def add_tasks(tasks):  
    n_task = int(input("How many tasks would you like to add? "))
    for i in range(n_task):
        add_task = input(f"Enter task {i+1}: ")
        tasks.append({"task": add_task, "done": False})
    return tasks

def delete_task(tasks): 
    remove_task = int(input("How many tasks would you like to delete? "))
    for i in range(remove_task):
        del_task = input(f"Enter task {i+1} to delete: ")
        for task in tasks:
            if task["task"] == del_task:
                tasks.remove(task)
                print(f"Task '{del_task}' deleted.")
                break
        else:
            print(f"Task '{del_task}' not found.")
    return tasks            

def mark_done(tasks):
    mark = int(input("How many tasks would you like to mark as done? "))
    for i in range(mark):
        mark_task = input(f"Enter task {i+1} to mark as done: ")
        for task in tasks:
            if task["task"] == mark_task:
                task["done"] = True
                print(f"Task '{mark_task}' marked as done.")
                break
        else:
            print(f"Task '{mark_task}' not found.")
    return tasks 

# Main program
tasks = []
while True:
    display_action()
    choice = input("Enter your choice: ")
    
    if choice == "1":
        tasks = add_tasks(tasks)
        display_tasks(tasks)
    elif choice == "2":
        tasks = delete_task(tasks)
        display_tasks(tasks)
    elif choice == "3":
        tasks = mark_done(tasks)
        display_tasks(tasks)
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
