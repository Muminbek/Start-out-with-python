# world series winners

def main():
    with open('WorldSeriesWinners.txt', 'r') as infile:
        win_list = infile.read().splitlines()
    
    winning_times = WinningTimes(win_list)
    winner_team = WinningTeam(win_list)
    
    keep_going = "y"
    while keep_going.lower() == 'y':
        try:
            year = int(input("Please enter a year: "))
            if year in winner_team:
                print(f"The winner that year is {winner_team[year]} and it has won the cup {winning_times[winner_team[year]]} times.")
            elif year == 1904 or year == 1994:
                print("World series was not played in this year.") 
            else: 
                print("ERROR: Please enter a valid year between 1903 through 2008.")
            keep_going = input("You want to continue? (y/n): ")
        except ValueError:
            print('ERROR: invalid value')
        print()       

def WinningTimes(list):
    count = 1
    dict = {}
    for line in list:
        if line not in dict:
            dict[line] = count
        else:
            dict[line] += 1
    return dict

def WinningTeam(list):
    dict = {}
    year = 1903

    for team in list:   
        if year != 1904 and year != 1994:
            dict[year] = team
        else:
            year += 1
            dict[year] = team
        year +=1
    return dict

main()



    

