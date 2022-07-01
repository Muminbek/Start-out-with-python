# sum of numbers

def main():
    print('Program will sum numbers from 1 up to your input number')
    x = int(input('Enter number: '))
    print(sum_of_number(x))

def sum_of_number(x):
    if x == 1:
        return 1
    else:
        return x + sum_of_number(x - 1)

if __name__ == '__main__':
    main()
