# name and email addresses
import pickle

def main():
    emails = load_file()
    again = 'y'

    while again.lower() == 'y':
        user_choice = get_choice()
        if user_choice == 1:
            AddNewName(emails)
        elif user_choice == 2:
            Change(emails)
        elif user_choice == 3:
            Delete(emails)
        elif user_choice == 4:
            ShowDataFor(emails)
        elif user_choice == 5:
            break
        else:
            print("You entered an invalid option.\n")
        again = input("\nYou want to continue? (y or n): ")

        save_file(emails)
        print('\nEXITED')

def load_file():
    try:
        with open('name_email.dat', 'rb') as infile:
            dict = pickle.load(infile)

    except FileNotFoundError:
        dict = {}
    return dict

def get_choice():
    print()
    print("MENU")
    print("1: Add a new name and email address")
    print("2: Change an existing email address")
    print("3: Delete an existing email address")
    print("4: Show data for")
    print("5: Exit")
    print("------------------------------------")
    try:
        user_choice = int(input("Please enter a choice among the menu (1,2,3,4,5): "))
        return user_choice
    except ValueError:
        print('Please enter a choice among the menu (1,2,3,4,5)')
        get_choice()

def save_file(emails):
        with open('name_email.dat', 'wb') as infile:
            pickle.dump(emails, infile)
    
def AddNewName(emails):
    name = input("Please enter the name: ")
    if name.lower() not in emails:
        emails[name.lower()] = input("E-mail: ")
        print(f"The registry for {name} has been recorded.")
    else:
        print("That name already exists.")
    return emails

def Change(emails):
    name = input("Please enter the name: ")
    if name.lower() in emails:
        emails[name.lower()] = input("E-mail: ")
        print(f"The registry for {name} has been updated.")
    else:
        print("It is not found in the file.")
    return emails

def Delete(emails):
    name = input("Please enter the name: ")
    if name.lower() in emails:
        del emails[name.lower()]
        print(f"The registry for {name} has been deleted.")
    else:
        print("It is not found in the file.")
    return emails
    
def ShowDataFor(emails):
    name = input("What is the name you are looking for?: ")
    try:
        print(f"Email address: {emails[name.lower()]}")
    except KeyError:
        print(f"The name <<{name}>> is not found.")
        print()

main()