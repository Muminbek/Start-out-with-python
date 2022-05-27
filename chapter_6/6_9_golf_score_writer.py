# Programm to write players names and their scores

def main():
    
    status = True
    while status == True:
        try:
            option()
            user_choice = int(input('Please enter number of option: '))
            if user_choice == 1:
                writer()
            elif user_choice == 2:
                reader()
            elif user_choice == 3:
                print('Exit....')
                status = False
            else:
                raise Exception('Error: Invalid value')
                
        except Exception as err:
            print(f'{err}\n')



def writer():
    status = True
    golf_file = open('golf.txt', 'a')
    while status == True:
        try:
            names = input('\nEnter name of the player: ')
            scores = float(input('Enter score of the player: '))
            golf_file.write(names + '\n')
            golf_file.write(f'{scores} \n')
            print('Success!')
            user_choice = input('Please enter "y" to continue or any button to return menu: ')
            if user_choice.upper() != 'Y':
                status = False
        except Exception as err:
            print(err)
    golf_file.close()
    print("\nThe names and scores are written to <golf.txt>. ")

def reader():
    golf_file = open('golf.txt', 'r')
    number = 1
    print('Players\t\tScores')
    print('-----------------------')
    for line in golf_file:
        line = line.rstrip()
        
        print(f"{number}.  {line}", end = " ............... ")
        
        line = golf_file.readline()
        print(line, end='')
        number += 1
    golf_file.close()
    input('Press Enter to return back menu...')
    
def option():
    print('Enter 1 to wrtie in the file <golf.txt>')
    print('Enter 2 to read from the file <golf.txt>')
    print('Enter 3 to exit')

main()
