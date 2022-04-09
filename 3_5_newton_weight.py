#newton weight
mass = int(input('Enter mass: '))

weight = mass * 9.8 #newton formula of weight

if weight > 500:
    print('weight is too heavy')
elif weight < 100:
    print('weight is too light')
else:
    print(format(weight, '.1f'))