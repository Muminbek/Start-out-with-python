# maximum of two


def main():
    
    first_num  = int(input('Enter first number: '))
    second_num  = int(input('Enter second number: '))
    
    max(first_num, second_num)
    
def max(first_num, second_num):
    if first_num > second_num:
        print(first_num, 'is maximum of two numbers')
    elif first_num == second_num:
        print('Two numbers are equal') 
    else:
        print(second_num, 'is maximum of two numbers')


main()
