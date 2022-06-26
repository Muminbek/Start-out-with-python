# guess number
import random

def main():
    QUIT = 'y'
    
    while QUIT != 'n':
        random_num = get_random_num()
        user_number = int(input('\nPlease try to guess random number from 1 through 100: '))
        counter = 1
        
        while random_num != user_number:
            if random_num > user_number:
                print('Your number is too low')
            else:
                print('Your number is too high')
            user_number = int(input('Please try again: '))
            counter += 1
            
        print('\nCongrotulation! You found the number!')
        print("You have found correct number after", counter, "tryings" )
        QUIT = input('Do you want to play again? Enter y/n ')
    
def get_random_num():
    return random.randint(1, 100)

main()
    