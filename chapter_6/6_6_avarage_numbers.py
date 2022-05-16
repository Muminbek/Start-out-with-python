def main():

    try: 
        filename = input('Please input file path: ')
        infile = open(filename, 'r')
        total = 0
        counter = 0

        for line in infile:
            total += int(line)
            counter += 1
        print(f'The average of numbers is {total / counter}')
        infile.close()
    except IOError as err:
        print(err)
    except ValueError as err:
        print(err)
main()
