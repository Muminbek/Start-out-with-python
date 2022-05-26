## world series champions

def main():
    with open('WorldSeriesWinners.txt','r') as winners_file:
        winners_list = winners_file.read().splitlines()

    user_choice = input('Please enter the team (first letters of each word capital): ')
    total_winning = WinnerTeam(winners_list, user_choice)

    print(f'The team: {user_choice} has been winner {total_winning} times.')

def WinnerTeam(list, choice):
    index = 0
    total_winning = 0

    for team in list:
        if team == choice:
            total_winning +=1
            index +=1
    return total_winning
    

main()