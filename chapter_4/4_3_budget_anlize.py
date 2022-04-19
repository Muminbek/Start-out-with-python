
budget_per_month = float(input('Enter the budget per month: '))

total_expense = 0
keep_going = 'y'
counter = 0
while keep_going == 'y' or keep_going == 'Y':
    expense = float(input(f'Enter credit for {counter + 1} day: '))

    total_expense += expense
    counter += 1
    keep_going = input("If you want to add another total_expense please type 'y'. To end type 'n'")
    
saved = budget_per_month - total_expense
overspent = total_expense - budget_per_month

print('Total buget: $', format(budget_per_month, '.2f'), sep='' )
print('You have spent: $', format(total_expense, '.2f'), sep='')

if budget_per_month >= total_expense:
    print('You saved $', format(saved, '.2f'), sep='')
else:
    print('You overspent $', format(overspent, '.2f'), sep='')
    