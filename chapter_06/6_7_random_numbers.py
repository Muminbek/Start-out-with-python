import random


def main():

    try:
        user_amount = int(input('Enter amount of numbers: '))
        filename = input('Please input file path: ')
        infile = open(filename, 'w')
        
        for i in range(user_amount):
            rand_num = random.randint(1, 500)
            infile.write(f'{rand_num}\n')
            
        print("The numbers are generated and written to <random_numbers.txt>. ")
        infile.close()
        
    except Exception  as err:
        print(err)
        

main()   