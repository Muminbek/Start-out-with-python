def main():
    counter = 0
    file_name = input('Please input file path: ')
    my_file = open(file_name, 'r')

    for name in my_file:
        counter += 1
    my_file.close()  
    
    print(f'Amount of names in the file: {counter}')

main()
