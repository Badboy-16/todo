from os import environ
from os import name as os_name
import sys

from src.query import (
    execute_query,
    create_connection,
    CREATE_TABLE,
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
        home_folder_path = str(environ['USERPROFILE'])
    else:
        home_folder_path = str(environ['HOME'])
    return home_folder_path

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
            delete(c, delete_task_id)
        elif menu_input.upper() == 'E':
            view(c)
            edit_task_id = str(input("Input task ID to edit: "))
            edit(c, edit_task_id)
        elif menu_input.upper() == 'X':
            sys.exit()
    sys.exit()

if __name__ == '__main__':
    main()

