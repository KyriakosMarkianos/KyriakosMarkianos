'''
To-Do List Example with SQLite and Python
Objective: Create a script to manage a to-do list. It will allow users to:
- Add tasks.
- View tasks.
- Mark tasks as complete.
- Delete tasks.
'''
import sqlite3

# Connect to the database (Create if it does not exists)
db = sqlite3.connect("index_KM.db")

# Create a Cursor for execution
cursor = db.cursor()

# Write commands after the cursor
cursor.execute('''
    CREATE TABLE IF NOT EXISTS todo (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(50),
        description TEXT,
        complete TEXT DEFAULT ('Incomplete') CHECK (complete IN ('Complete', 'Incomplete')),
        owner VARCHAR(50),
        date_due DATE DEFAULT (DATETIME('now'))
    )
''')

# Responsible for adding a new task
def add_task(task_name, task_description, task_owner):
    cursor.execute('''
            INSERT INTO todo (name, description, owner)
            VALUES (?, ?, ?)
            ''', 
            (task_name, task_description, task_owner)
            )
    db.commit()

# Reading and displaying tasks
def view_tasks():
    cursor.execute("SELECT * FROM todo")
    tasks = cursor.fetchall()

    for task in tasks:
        print(task)

# Marking tasks as completed
def mark_complete(task_id):
    cursor.execute('''
        UPDATE todo SET complete = 'Complete' WHERE id = ?
''', (task_id))
    db.commit()


# Deleting a task
def delete(task_id):
    cursor.execute('''
        DELETE FROM todo WHERE id = ?
''', (task_id))
    db.commit()


message = '''
 Enter an action you'd want to perform
 1. Add task
 2. View tasks
 3. Mark task as complete
 4. Delete the task
 5. Exit
'''

def main():
    while True:
        print(message)

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            task_description = input("Enter the task description: ")
            task_owner = input("Enter your name: ")
            add_task(task_name, task_description, task_owner)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = input("Enter the task id to be updated: ")
            mark_complete(task_id)
        elif choice == "4":
            task_id = input("Enter the task id you'd need to delete: ")
            delete(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice: Please try again")

main()
db.close()