todo_list = []

def add_task(tasks: list, task: str) -> None:
    tasks.append(task)
    return None

def show_all_tasks(tasks: list) -> None:
    if len(tasks) == 0:
        print("")
        print(f"list is empty")
    else:
        for i, j in enumerate(tasks):
            print(f"{i + 1}. {j}")

def get_index(relative_str) -> int:
    the_index = int(input(relative_str))
    return the_index - 1

def delete_task(tasks: list, index: int):
    if len(tasks) == 0:
        print("")
        print("list is empty")
    else:
        tasks.pop(index)

def edit_task(tasks: list, index: int):
    if len(tasks) == 0:
        print("")
        print("list is empty")
    else:
        tasks[index] = input("enter your new task to replace the old one: ")


def  get_user_choice() -> str:
    print("")
    print("1. add a task")
    print("2. show list")
    print("3. delete a task")
    print("4. rewrite a task")
    print("5. exit")
    choice = input("enter the number of your action's choice: ")
    print("")
    return choice