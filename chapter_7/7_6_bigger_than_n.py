def main():
    try:
        number_list = [2,4,6,7,9,45,76,23,76,89,34,33]
        user_number = int(input('Enter the number: '))

        check_number(number_list, user_number)
    except ValueError:
        print("You entered non integer value.")
        main()

def check_number(a, b):
    print(f'\nThe numbers greater than {b} in the list are listed below: ')
    print('-------------------------------------------------------')
    status = False
    for i in a:
        if i > b:
            print(i)
            status = True
    if not status:
        print("There are 0 numbers that are greater than the number you provided:", b)
        
main()