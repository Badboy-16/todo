import getpass
from os import environ
from os import name as os_name
import sqlite3
from sqlite3 import Error
import sys

WELCOME_MSG = """
Welcome to Yunyi's command line to do list application.
Please select the options below.
"""

OPTIONS_MSG = """
(V)iew all tasks. (A)dd tasks. (S)earch tasks. (D)elete tasks.
(E)dit tasks. E(x)it.
"""

# SQL query to create the todolist table if it doesn't exist yet.
CREATE_TABLE = """
CREATE TABLE IF NOT EXIST todolist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(40) NOT NULL,
    description VARCHAR(256),
    priority VARCHAR(16) NOT NULL,
    category VARCHAR(40) NOT NULL,
    due DATE,
    location VARCHAR(256),
    status VARCHAR(16) NOT NULL
);
"""

# SQL query to view all tasks.
VIEW_TODO_LIST = "SELECT * FROM todolist"

def get_home_folder():
    if os_name == 'nt':
        home_folder_path = str(environ['USERPROFILE'])
    else:
        home_folder_path = str(environ['HOME'])
    return home_folder_path

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to database successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = connection.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def view():
    execute_read_query(c, VIEW_TODO_LIST)

def add():

    name = input("Name of the task: ")
    description = input("Description of the task: ")
    priority = input("Priority: (H)igh/(M)edium/(L)ow")
    category = input("Category: ")
    due = input("Due date (YYYY-MM-DD): ")
    location = input("Location: ")
    status = 'in progress'

    _ADD_TASK = f"""
    INSERT INTO
        todolist (name, description, priority, category, due, location,
                  status)
    VALUES
        ({name}, {description}, {priority}, {category}, {due},
         {location}, {status});
    """
    execute_query(c, _ADD_TASK)

def search(search_term):
    pass


def delete(delete_task_id):
    _delete_task = f"DELETE FROM todolist WHERE id = {delete_task_id}"
    execute_query(c, _delete_task)

def edit(edit_task_id):
    edit_fields = input("""
    Which field(s) would you like to edit?
    For multiple fields edits, separate the field names with commas.
    """)
    edit_fields.replace(' ', '')
    edit_fields_list = edit_fields.split(',')
    edit_fields_values = []
    for field in edit_fields_list:
        value = input(f"Please input the updated {field}: ")
        edit_fields_values.append(value)
    edit_fields_pairs = list(zip(edit_fields_list, edit_fields_values))

    for field, value in edit_fields_pairs:
        _update_task = f"""
        UPDATE
            todolist
        SET
            {field} = {value}
        WHERE
            id = edit_task_id
        """
        execute_query(c, _update_task)

def main():
    """
    Main loop of the program.
    """
    print(WELCOME_MSG)
    c = create_connection(get_home_folder())
    execute_query(c, CREATE_TABLE)
    while c != None:
        menu_input = str(input(OPTIONS_MSG))
        if menu_input.upper() = 'V':
            view()
        elif menu_input.upper() = 'A':
            add()
        elif menu_input.upper() = 'S':
            search_term = str(input("Input the search term: "))
            search(search_term)
        elif menu_input.upper() = 'D':
            view()
            delete_task_id = int(input("Input task ID to delete: "))
            delete(delete_task_id)
        elif menu_input.upper() = 'E':
            view()
            edit_task_id = int(input("Input task ID to edit: "))
            edit(edit_task_id)
        elif menu_input.upper() = 'X':
            c = None
    sys.exit()

