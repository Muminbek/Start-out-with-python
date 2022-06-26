def main():
    try: 
        filename = input('Please input file path: ')
        infile = open(filename, 'r')
        total = 0
        for line in infile:
            total += int(line)

        print(f'Sum of numbers: {total}')
    except Exception as err:
        print(err)
        

main()