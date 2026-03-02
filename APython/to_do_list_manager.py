class to_do_list_manager:
    def __init__(self):
        self.to_do_list = []

    def add_task(self, task):
        self.to_do_list.append(task)
        print(f'Task "{task}" added to the to-do list.')

    def remove_task(self, task):
        if task in self.to_do_list:
            self.to_do_list.remove(task)
            print(f'Task "{task}" removed from the to-do list.')
        else:
            print(f'Task "{task}" not found in the to-do list.')
    def set_deadline(self, task, deadline):
        if task in self.to_do_list:
            print(f'Task "{task}" has a deadline set for {deadline}.')
        else:
            print(f'Task "{task}" not found in the to-do list. Cannot set deadline.')
    def assign_priority(self, task, priority):
        if task in self.to_do_list:
            print(f'Task "{task}" has been assigned a priority of {priority}.')
        else:
            print(f'Task "{task}" not found in the to-do list. Cannot assign priority.')
    def filter_tasks_by_project(self, project_name):
        print(f'Filtering tasks by project: {project_name}')
    def view_tasks(self):
        if not self.to_do_list:
            print("The to-do list is empty.")
        else:
            print("To-Do List:")
            for idx, task in enumerate(self.to_do_list, start=1):
                print(f"{idx}. {task}")


to_do_manager = to_do_list_manager()


while True:
    action = input("Enter '1' to add a task, '2' to remove a task, '3' to set a deadline, '4' to assign priority, '5' to filter tasks by project, '6' to view tasks, or '7' to exit: ")
    if action == "1":
        task = input("Enter the task you want to add: ")
        to_do_manager.add_task(task)
    elif action == "2":
        task = input("Enter the task you want to remove: ")
        to_do_manager.remove_task(task)
    elif action == "3":
        task = input("Enter the task you want to set a deadline for: ")
        deadline = input("Enter the deadline (e.g., YYYY-MM-DD): ")
        to_do_manager.set_deadline(task, deadline)
    elif action == "4":
        task = input("Enter the task you want to assign a priority to: ")
        priority = input("Enter the priority level (e.g., High, Medium, Low): ")
        to_do_manager.assign_priority(task, priority)
    elif action == "5":
        project_name = input("Enter the project name to filter tasks by: ")
        to_do_manager.filter_tasks_by_project(project_name)
    elif action == "6":
        to_do_manager.view_tasks()
    elif action == "7":
        print("Exiting the To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid action. Please enter a number between 1 and 7.")
