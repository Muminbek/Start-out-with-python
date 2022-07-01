# Recursive power method
def main():
    print('Program will raise a number to a power')
    x = int(input('Enter number: '))
    y = int(input('Enter exponent: '))
    print(f'Result: {power_method(x, y)}')
def power_method(x, y):
    if y == 1:
        return x
    else:
        return x * power_method(x, y-1)
if __name__ == '__main__':
    main()

