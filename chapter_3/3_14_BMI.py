#Индекс массы тела

body_weight = float(input('Enter your body weight: '))
body_height = float(input('Enter your body height: '))

body_mass_index = body_weight / body_height ** 2
missing_weight = 18.5 - body_mass_index
excess_weight = body_mass_index - 25

if body_mass_index >= 18.5 and body_mass_index <= 25:
    print('You have a optimal weight!')
    print('Your bmi is', format(body_mass_index, '.2f'))
elif body_mass_index < 18.5:
    print('You are underwieght! You have to get more minimum',\
        format(missing_weight, '.2f'), 'kg.')
    print('Your bmi is', format(body_mass_index, '.2f'))
else:
    print('You are overweight! Yoy must lose minimum',\
        format(excess_weight, '.2f'), 'kg.')
    print('Your bmi is', format(body_mass_index, '.2f'))
    