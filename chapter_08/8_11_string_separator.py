# stirng separator

def main():
    print("Example: StopAndSmellTheRoses\n")
    user_string = input("Enter a string like one above: ") 

    separator(user_string)

def separator(string):
    
    print(string[0], end='')

    index = 1
    while index < len(string):
        if string[index].isupper():
            print(' ', string[index].lower(), end='')
        else:
            print(string[index], end='')
        index += 1

    print('.')


main()
