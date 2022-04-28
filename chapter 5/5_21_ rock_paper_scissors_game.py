#  rock, paper, scissors game

import random

from numpy import False_

def main():
    print('Possible option are:')
    print('1) Rock')
    print('2) Paper')
    print('3) Scissors')
    
    status = True
    while status == True:
        user_choice = int(input('\nPlease enter choice as number: '))
        computer_chose = computer_choice()
        show_result_user(user_choice)
        show_result_computer(computer_chose)
        print()
        status = who_win(user_choice, computer_chose)
        
def computer_choice():
    return random.randint(1, 3)

def show_result_user(user_choice):
    if user_choice == 1:
        print('You chose rock.')
    elif user_choice == 2:
        print('You chose paper.')
    else:
        print('You chose scissors.')
    
def show_result_computer(computer_choice):
    if computer_choice == 1:
        print('Computer chose rock.')
    elif computer_choice == 2:
        print('Computer chose paper.')
    else:
        print('Computer chose scissors.')
        
def who_win(user_choice, computer_chose):
    status = False
    if user_choice == 1 and computer_chose == 2:
        print('You lost. Paper wraps rock')
    elif user_choice == 1 and computer_chose == 3:
        print('You won. Rock smashes scissors.')
    elif user_choice == 2 and computer_chose == 1:
        print('You won. Paper wraps rock.')
    elif user_choice == 2 and computer_chose == 3: 
        print('You lost. Scissors cuts paper.')
    elif user_choice == 3 and computer_chose == 1:
        print('You lost. Rock smashes scissors.')
    elif user_choice == 3 and computer_chose == 2:
        print('You won. Scissors cuts paper.')
    elif user_choice == computer_chose:
        print('*****It is a draw try again*****')
        status = True
    return status

main()