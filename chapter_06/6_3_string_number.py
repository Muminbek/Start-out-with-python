def main():
    file_name = input('Please input file path: ')
    my_file = open(file_name, 'r')
    
    line_num = 1
    for line in my_file:

        line = line.rstrip('\n')
        print(f'{line_num}: {line}')
        line_num += 1

    my_file.close()

main()
