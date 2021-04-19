from .query import(
    execute_query,
    execute_read_query,
    column_names,
    VIEW_TODO_LIST
)

def view(connection):
    print (column_names(connection))
    for task in execute_read_query(connection, VIEW_TODO_LIST):
        print(task)

def add(connection):

    name = input("Name of the task: ")
    description = input("Description of the task: ")
    priority = input("Priority (High/Medium/Low): ")
    category = input("Category: ")
    due = input("Due date (YYYY-MM-DD): ")
    location = input("Location: ")
    status = 'in progress'

    _ADD_TASK = f"""
    INSERT INTO
        todolist (name, description, priority, category, due, location,
                  status)
    VALUES
        ('{name}', '{description}', '{priority}', '{category}', '{due}',
         '{location}', '{status}');
    """

    execute_query(connection, _ADD_TASK)

def delete(connection, delete_task_id):
    _delete_task = f"DELETE FROM todolist WHERE id = '{delete_task_id}'"
    execute_query(connection, _delete_task)

def edit(connection, edit_task_id):
    edit_fields = input("""
    Which field(s) would you like to edit?
    For multiple fields edits, separate the field names with commas.
    """)
    edit_fields = edit_fields.replace(' ', '')
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
            '{field}' = '{value}'
        WHERE
            id = '{edit_task_id}'
        """
        execute_query(connection, _update_task)

