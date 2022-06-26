#number analysis program

def main():
    number = get_number()
    total = 0.0
    index = 0

    while index < len(number):
        total += number[index]
        index += 1

    print()
    print(f'The total of numbers is {total}')
    print(f'The average of numbers is {total/len(number)}')

    print(f'The minimum of numbers is {min(number)}')
    print(f'The maximum of numbers is {max(number)}')

def get_number():
    number = []
    index = 0
    while index < 20:
        number.append(float(input(f'Enter the number #{index +1}: ')))
        index += 1

    return number

main()

