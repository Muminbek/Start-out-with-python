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
    print('\n-----Students Menu -----')
    print('1. Add a new Student')
    print('2. Search for an existing Student')
    print('3. Update an existing Student')
    print('4. Delete an existing Student')
    print('5. Show a list of all Students')
    print('6. Exit the program')


def get_menu_choice():

    choice = int(input('Enter your choice: '))


    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
        choice = int(input('Enter your choice: '))

    return choice


def create():
    name = input('Name: ')
    majorID = None
    departmentID = None
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Majors')
        results = cur.fetchall()
        print('Majors list')
        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15}')
        majorID = int(input('Enter MajorID: '))
        print('Departments list')
        cur.execute('SELECT * FROM Departments')
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15}')
        departmentID = int(input('Enter DepartmentID: '))

    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn is not None:
            conn.close()
    print('Add a new Student')

    insert_row(name, majorID, departmentID)


def read():
    name = input('Enter a name to search for: ')
    num_found = display_student(name)
    print(f'{num_found} row(s) found.')


def update():

    read()
    selected_id = int(input('Select an Student ID: '))
    name = input('Enter the new name: ')
    majorID = None
    departmentID = None
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM Majors')
        results = cur.fetchall()
        print('Majors list')
        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15}')
        majorID = int(input('Enter new MajorID: '))
        print('Departments list')
        cur.execute('SELECT * FROM Departments')
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15}')
        departmentID = int(input('Enter new DepartmentID: '))

    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn is not None:
            conn.close()
    # Update the row.
    num_updated = update_row(selected_id, name, majorID, departmentID)
    print(f'{num_updated} row(s) updated.')


def delete():

    read()

    selected_id = int(input('Select an Student ID to delete: '))
    # Confirm the deletion.
    sure = input('Are you sure you want to delete this Student? (y/n): ')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')


def insert_row(name, majorID, departmentID):
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        # Enable foreign key enforcement.
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''INSERT INTO Students (Name, MajorID, DeptID)
                    VALUES (?, ?, ?)''',
                    (name, majorID, departmentID))
        print('Student added.')
        conn.commit()
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn is not None:
            conn.close()

def display_student(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT * FROM Students
                    WHERE lower(Name) == ?''',
                    (name.lower(),))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15} '
                  f'MajorID: {row[2]:<3} DeptID: {row[3]:<3}')
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn is not None:
            conn.close()

    return len(results)

def update_row(id, name, majorID, departmentID):
    conn = None
    num_updated = 0
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        # Enable foreign key enforcement.
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''UPDATE Students
                    SET Name = ?, MajorID = ?, DeptID = ?
                    WHERE StudentID == ?''',
                    (name, id, majorID, departmentID))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn is not None:
            conn.close()

    return num_updated

def delete_row(id):
    conn = None
    #4
    num_deleted = 0
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        # Enable foreign key enforcement.
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''DELETE FROM Students
                        WHERE StudentID == ?''',
                        (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn is not None:
            conn.close()

    return num_deleted

def show():
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        # Enable foreign key enforcement.
        cur.execute('PRAGMA foreign_keys=ON')
        cur.execute('''SELECT Students.StudentID, Students.Name, Majors.Name, Departments.Name
                    FROM Majors, Departments
                    INNER JOIN Students 
                    ON Students.MajorID == Majors.MajorID AND
                    Students.DeptID == Departments.DeptID''')
        results = cur.fetchall()
        print(f"{'ID':<5}{'Name':<15}{'Major':<20}{'Department':<15}")
        print('------------------------------------------------')
        for row in results:
            print(f'{row[0]:<5}{row[1]:<15}{row[2]:<20}{row[3]:15}')
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn is not None:
            conn.close()

 # Execute the main function.
if __name__ == '__main__':
    main()
