def main():
    file_name = input('please input file : ')
    my_file = open(file_name, 'r')
    
    for i in range(5):
        
        file = my_file.readline()
        file = file.rstrip('\n')
        print(file)

    my_file.close()

main()
