import sqlite3
MIN_CHOICE = 1
MAX_CHOICE = 6
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
SHOW = 5
EXIT = 6

def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()

        if choice == CREATE:
            create()
        elif choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()
        elif choice == SHOW:
            show()

def display_menu():
    print('\n-----Major Menu -----')
    print('1. Add a new major')
    print('2. Search for an existing major')
    print('3. Update an existing major')
    print('4. Delete an existing major')
    print('5. Show a list of all majors')
    print('6. Exit the program')


def get_menu_choice():

    choice = int(input('Enter your choice: '))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
        choice = int(input('Enter your choice: '))

    return choice

def create():
    print('Add a new major')
    name = input('Name: ')
    insert_row(name)
    
def read():
    name = input('Enter a name to search for: ')
    num_found = display_major(name)
    print(f'{num_found} row(s) found.')


def update():

    read()

    selected_id = int(input('Select an Major ID: '))
    name = input('Enter the new name: ')

    # Update the row.
    num_updated = update_row(selected_id, name)
    print(f'{num_updated} row(s) updated.')


def delete():

    read()

    selected_id = int(input('Select an Major ID to delete: '))
    # Confirm the deletion.
    sure = input('Are you sure you want to delete this major? (y/n): ')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')

def insert_row(name):
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Majors (Name)
                    VALUES (?)''',
                    (name,))
        print('Major added.')
        conn.commit()
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn != None:
            conn.close()

def display_major(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Majors
                    WHERE lower(Name) == ?''',
                    (name.lower(),))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn != None:
            conn.close()

    return len(results)

def update_row(id, name):
    conn = None
    num_updated = 0
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Majors
                    SET Name = ?
                    WHERE MajorID == ?''',
                    (name, id))
        conn.commit()
        num_updated = cur.rowcount
        
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None: 
            conn.close()

    return num_updated

def delete_row(id):
    conn = None
    #4
    num_deleted = 0
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Majors
                        WHERE MajorID == ?''',
                        (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None: 
            conn.close()
    
    return num_deleted

def show():
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Majors')
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn != None:
            conn.close()

 # Execute the main function.
if __name__ == '__main__':
    main()