#population

population = float(input('Enter the population of organisms: '))
increasing_per_day = float(input('Enter increasing population percantage per day: '))
amount_day = int(input('Enter amount of days: '))
increasing_per_day = increasing_per_day / 100

print('\nDays\t\tPopulation')

for day in range(1, amount_day + 1):
    
    print(day, '\t\t', format(population, '.1f'))
    
    population += population * increasing_per_day
    
    
    