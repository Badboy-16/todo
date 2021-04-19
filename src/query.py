import sqlite3
from sqlite3 import Error

# SQL query to create the todolist table if it doesn't exist yet.
CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS todolist (
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
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def column_names(connection):
    cursor = connection.cursor()
    cursor.execute(VIEW_TODO_LIST)
    cursor.fetchall()
    column_names = [description[0] for description in cursor.description]
    return tuple(column_names)

