total_bugs = 0

for day in range(5):
    daily_bugs = int(input('How many bugs did you collected today? '))
    total_bugs += daily_bugs
    
print('\nYou have collected ', total_bugs, 'bugs.')
    