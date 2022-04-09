# color mixer

color1 = input('Enter one of these colors (red, blue, yellow): ')
color2 = input('Enter second  main color: ')

if color1 == 'red' and color2 == 'blue':
    print('color will be violet')
elif color1 == 'red' and color2 == 'yellow':
    print('color will be orange')
elif color1 == 'blue' and color2 == 'yellow':
    print('color will be green')
else:
    print('color is not defined')   