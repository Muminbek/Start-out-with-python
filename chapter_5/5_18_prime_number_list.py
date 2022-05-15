# prime number list

def main():
    print("\nThe prime numbers from 1 to 100 are listed below.")

    # first lets pass all numbers from 1 to 100 to our is_prime function.
    for num in range(1, 101):
        if is_prime(num):
            print(num, end='  ')
    
            
def is_prime(num):
    status = True
    counter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            counter += 1
            if counter >= 3:
                status = False
    return status

main()