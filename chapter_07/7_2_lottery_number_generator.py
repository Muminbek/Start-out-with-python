# lottery number generator
import random

def main():
    number = rand_num_gen()
    print("The lucky numbers are below. Thanks for participating.")
    print()
    index=0 

    while index < len(number):
        print(number[index], end= ' ')
        index +=1

def rand_num_gen():
    number = []

    for i in range(7):
        number.append(random.randrange(10))
    
    return number

main()
