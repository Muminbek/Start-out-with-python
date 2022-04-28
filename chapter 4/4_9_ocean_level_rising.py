

level_up: float = 1.6
total_up: float = 0


print('Years\t\tRising level in mm')
print('---------------------------------')
for year in range(25):
    total_up += level_up
    
    print(year + 1, '\t\t', format(total_up, '.1f'))