#Цвета колеса рулетки

roll_pocket_color = int(input('Enter number of roullete 0 - 36: '))

if roll_pocket_color == 0:
    print('Color of roll pocket is green')
elif roll_pocket_color > 0 and roll_pocket_color <= 10 or roll_pocket_color > 18 and roll_pocket_color <= 28:
    print('Color of roll pocket is black')
elif roll_pocket_color > 10 and roll_pocket_color <= 18 or roll_pocket_color > 29 and roll_pocket_color <= 36:
    print('Color of roll pocket is red')
else:
    print('There is no such a number in the roll')
