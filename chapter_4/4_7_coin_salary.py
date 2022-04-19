
days = int(input('Enter working days: '))
salary = 0.01
 
print('\nDays\t\tSalary')
print('----------------------')

for day in range(1, days + 1):
    
    print(day,'\t\t', '$', format(salary, ',.2f'), sep='')
    salary *= 2
    
    
print('\nTotal salary in ', day, ' days is $', format(salary, ',.2f'), sep='')
