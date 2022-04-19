#loosing_weight

loosing_weight = 1.5
weight = float(input('Enter your current weight: '))

print('\ndecrease consuming 500 calories per day helps loose your weight 1,5 kg per month')

print('\nafter month\tyour weight')
print('----------------------------')

for month in range(6):
    weight -= loosing_weight
    print(month + 1,'\t\t', weight)
        