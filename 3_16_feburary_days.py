#Дни в феврале
year = int(input('Input a year: '))

if year > 0:
    message = 'In ' + format(year) + ' February has ' 
    if year % 100 == 0:
        if year % 400 == 0:
            message += '29'
        else:
            message += '28'
    else:
        if year % 4 == 0:
            message += '29'
        else:
            message += '28'
            
    message += ' days.'
    
else:
    message = 'Enter a year greater than 0\n' + \
              'Rerun the program and try again.'
              
print(message) 