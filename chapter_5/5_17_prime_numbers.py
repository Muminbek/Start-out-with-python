#prime numbers

def main():
    
    user_number=int(input("\nPlease enter a number to check if it is prime or not: "))
    
    if is_prime(user_number):
        print('Your number', user_number, 'is a prime number.')
    else:
        print("Your number", user_number, "is NOT a prime number.")
            
def is_prime(user_number):
    status = True
    counter = 0
    for i in range(1, user_number + 1):
        if user_number % i == 0:
            print("It can be divided by", i)
            counter += 1
            if counter >= 3:
                status = False
    return status

main()