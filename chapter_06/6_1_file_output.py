def main():
    try:
        file_name = input('Please input file path: ')
        my_file = open(file_name, 'r')
        file = my_file.read()
        print(file)
        my_file.close()
    except IOError as err:
        print(err)
main()
