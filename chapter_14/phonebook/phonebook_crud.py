import sqlite3
MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

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

# The display_menu function displays the main menu.
def display_menu():
    print('\n----- Phonebook Menu -----')
    print('1. Create a Entry')
    print('2. Look up an Entry')
    print('3. Update an Entry')
    print('4. Delete an Entry')
    print('5. Exit the program')

# The get_menu_choice function gets the user's menu choice.
def get_menu_choice():
    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the input.
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}.')
        choice = int(input('Enter your choice: '))

    return choice


def create():
    print('Create New Entry')
    name = input('Name: ')
    phone_number = input('Phone number: ')
    insert_row(name, phone_number)
    

def read():
    name = input('Enter a name to search for: ')
    num_found = display_item(name)
    print(f'{num_found} row(s) found.')


def update():

    read()
    selected_id = int(input('Select an Entry ID: '))
    name = input('Enter the new name: ')
    phone_number = input('Enter the new phone number: ')

    # Update the row.
    num_updated = update_row(selected_id, name, phone_number)
    print(f'{num_updated} row(s) updated.')


def delete():

    read()

    selected_id = int(input('Select an Entry ID to delete: '))
    # Confirm the deletion.
    sure = input('Are you sure you want to delete this entry? (y/n): ')
    if sure.lower() == 'y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} row(s) deleted.')

def insert_row(name, phone_number):
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Entries (Name, PhoneNumber)
                    VALUES (?, ?)''',
                    (name, phone_number, ))
        print('Entry created.')
        conn.commit()
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn != None:
            conn.close()

def display_item(name):
    conn = None
    results = []
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Entries
                    WHERE lower(Name) == ?''',
                    (name.lower(),))
        results = cur.fetchall()
        for row in results:
            print(f'ID: {row[0]:<3} Name: {row[1]:<15} '
                  f'Phone number: {row[2]:<6}')
    except sqlite3.Error as err:
        print('Datebase Error', err)
    finally:
        if conn != None:
            conn.close()
    # Return the number of matching rows.
    return len(results)

def update_row(id, name, phone_number):
    conn = None
    num_updated = 0
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Entries
                    SET Name = ?, PhoneNumber = ?
                    WHERE EntryID == ?''',
                    (name, phone_number, id))
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
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Entries
                        WHERE EntryID == ?''',
                        (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None: 
            conn.close()
    
    return num_deleted

 # Execute the main function.
if __name__ == '__main__':
    main()