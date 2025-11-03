from tl_functions import todo_list
from tl_functions import add_task
from tl_functions import show_all_tasks as show_tasks
from tl_functions import get_user_choice as get_choice
from tl_functions import delete_task
from tl_functions import get_index
from tl_functions import edit_task


def main() -> None:
    while True:
        choice = get_choice()
        if choice == "1":
            print("")
            add_task(todo_list, input("enter task: "))
        elif choice == "2":
            show_tasks(todo_list)
        elif choice == "3":
            show_tasks(todo_list)
            if len(todo_list) == 0:
                continue
            while True:
                print("")
                for_delete = get_index("enter the number of the task you want to delete: ")
                if type(for_delete) != int or for_delete > len(todo_list) or for_delete < 1:
                    print("")
                    print("invalid entry,")
                    print("please try again.")
                else:
                    delete_task(todo_list, for_delete)
                    break
        elif choice == "4":
            show_tasks(todo_list)
            if len(todo_list) == 0:
                continue
            while True:
                print("")
                for_edit = get_index("enter the number of the task you want to rewrite: ")
                if type(for_edit) != int or for_edit > len(todo_list) or for_edit < 1:
                    print("")
                    print("invalid entry,")
                    print("please try again.")
                else:
                    edit_task(todo_list, for_edit)
                    break 
        elif choice == "5":
            break
        else:
            print("")
            print("invalid choice.")
            print("these are your only options")
main()