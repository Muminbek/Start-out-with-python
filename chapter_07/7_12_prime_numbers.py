#prime numbers

def main():
     
    user_number = int(input('Please enter number: '))
    while user_number <= 1:
        user_number = int(input('Pleaes enter number above 1'))

    number_list = []
    for i in range(2, user_number+1):
        number_list.append(i)

    
    print(f'\nPrime numbers until {user_number} are below: ')
    for i in number_list:
        if is_prime(i) == True:
            print(i, end=' ')
    print()

def is_prime(user_number):
    status = True
    counter = 0
 
    for i in range(1, user_number + 1):
        if user_number % i == 0:
            counter += 1
            if counter >= 3:
                status = False
    return status
    
main()