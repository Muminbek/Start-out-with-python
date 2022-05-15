#Magic date
month = int(input('Enter the month: '))
day = int(input('Enter the day: '))
year = int(input('Enter the year, only last twoo num: '))

month_day = month * day

if month_day == year:
    print('Data is magic')
else:
    print('Data is not magic')
