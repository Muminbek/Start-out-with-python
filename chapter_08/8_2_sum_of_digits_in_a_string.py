# sum of digits in a string

def main():
    try:
        numbers = input('Enter a series of single-digit numbers (such as 12445): ')
        total = 0
        for n in numbers:
            total += int(n)
    
        print('The sum of digits in the number of', numbers, "is", total)

    except ValueError:
        print("You can't enter letters in the numbers string. Try again!")
        print("---------------------------------------------------------")
        main()
main()

