from os import environ
from os import name as os_name

from src.query import (
    execute_query,
    create_connection,
    CREATE_TABLE,
    valid_id
)
from src.option import view, add, delete, edit

WELCOME_MSG = """
Welcome to Yunyi's command line to do list application.
Please select the options below.
"""

OPTIONS_MSG = """
(V)iew all tasks. (A)dd tasks. (D)elete tasks. (E)dit tasks. E(x)it.
"""

def get_home_folder():
    if os_name == 'nt':
        return str(environ['USERPROFILE'])
    else:
        return str(environ['HOME'])
    
def main():
    """
    Main loop of the program.
    """
    print(WELCOME_MSG)
    c = create_connection(get_home_folder() + '/test.sqlite')
    execute_query(c, CREATE_TABLE)
    while c != None:
        menu_input = str(input(OPTIONS_MSG))
        if menu_input.upper() == 'V':
            view(c)
        elif menu_input.upper() == 'A':
            add(c)
        elif menu_input.upper() == 'D':
            view(c)
            delete_task_id = int(input("Input task ID to delete: "))
            try:
                if valid_id(c, delete_task_id):
                    delete(c, delete_task_id)
            except ValueError:
                print("Please input an integer ID value")
            else:
                print("Invalid ID.")
        elif menu_input.upper() == 'E':
            view(c)
            edit_task_id = str(input("Input task ID to edit: "))
            try:
                if valid_id(c, edit_task_id):
                    edit(c, edit_task_id)
            except ValueError:
                print("Please input an integer ID value")
            else:
                print("Invalid ID.")
        elif menu_input.upper() == 'X':
            exit()
        else:
            print("Invalid input.")
    exit()

if __name__ == '__main__':
    main()

