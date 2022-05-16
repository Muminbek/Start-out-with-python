
def main():
    filename = input('Please input file path: ')
    infile = open(filename, 'r')

    total = 0
    amount = 0
    for line in infile:
        line = line.rstrip('\n')
        print(line)
        total += float(line)
        amount += 1

    
    print(f"There are {amount}, numbers in the <random_numbers.txt> file.")
    print("And their total is", total)

main()