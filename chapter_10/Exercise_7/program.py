import employee
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5
FILENAME = ('employee.dat')

def main():
    employee_dct = load_file()
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        if choice == LOOK_UP:
            look_up(employee_dct)
        elif choice == ADD:
            add(employee_dct)
        elif choice == CHANGE:
            change(employee_dct)
        elif choice == DELETE:
            delete(employee_dct)
    save_file(employee_dct)
        
def load_file():
    try:
        # Open the contacts.dat file.
        with open(FILENAME, 'rb') as input_file:
            # Unpickle the dictionary.
            employee_dct = pickle.load(input_file)
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        employee_dct = {}
        # Return the dictionary.
    return employee_dct

def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up an employee')
    print('2. Add a new emplyee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()
    # Get the user's choice.
    try:
        choice = int(input('Enter your choice: '))
        while choice < LOOK_UP or choice > QUIT:
            choice = int(input('Enter a valid choice: '))
        return choice
    except ValueError:
        choice = int(input('Enter a valid choice: '))
        
    # return the user's choice.

def look_up(emplyee_dct):
 # Get a name to look up.
    id = input('Enter an ID: ')
 # Look it up in the dictionary.
    print(emplyee_dct.get(id, 'That ID is not found.'))

def add(employee_dct):
    name = input('Name: ')
    id = input('ID: ')
    department = input('Department: ')
    job_title = input('Job title: ')

    entry = employee.Employee(name, id, department, job_title)

    if id not in employee_dct:
        employee_dct[id] = entry
        print('The entry has been added.')
    else:
        print('That ID already exists.')

def change(employee_dct):
    id = input('Enter an ID: ')

    if id in employee_dct:
        name = input('Name: ')
        department = input('Department: ')
        job_title = input('Job title: ')
        entry = employee.Employee(name, id, department, job_title)
        employee_dct[id] = entry
        print('Information updated.')
    else:
        print('That ID is not found.')

def delete(employee_dct):
    id = input('Enter an ID: ')
    if id in employee_dct:
        del employee_dct[id]
        print('Entry deleted.')
    else:
        print('That ID is not found')

def save_file(employee_dct):
    with open(FILENAME, 'wb') as infile:
        pickle.dump(employee_dct, infile)
    
if __name__ == '__main__':
    main()