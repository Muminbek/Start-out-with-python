''' Игра в подсчитывание монет. Создайте игру, которая просит пользователя ввести 
не­обходимое количество монет, чтобы получился ровно один рубль. Программа должна
предложить пользователю ввести количество монет достоинством 5, 10 и 50 копеек.
Если итоговое значение введенных монет равно одному рублю, то программа должна
поздравить пользователя с выигрышем. В противном случае программа должна вывести
сообщение, говорящее о том, была ли введенная сумма больше или меньше одного
рубля. Подумайте о варианте игры, где вместо рубля используется доллар и разменные
монеты: пенс, пятицентовик, десятицентовик и четвертак.'''

PENNY = 1
NICKEL = 5
DIME = 10
QUARTER = 25

pennies = int(input('Enter number of pennies = 1: '))
nickels = int(input('Enter number of nickels = 5: '))
dimes = int(input('Enter number of dimes = 10: '))
quarters = int(input('Enter number of quarters = 25: '))

pennies *= PENNY
nickels *= NICKEL
dimes *= DIME
quarters *= QUARTER

total = pennies + nickels + dimes + quarters

message = ''

if total == 100:
    message = 'You won! The amount entired equals 1 dollar'
else:
    message = 'You lost! '
    
    if total > 100:
        message += 'The amount entered is greater than 1 dollar'
    else:
        message += 'The amount entered is less than 1 dollar'

print(message)
