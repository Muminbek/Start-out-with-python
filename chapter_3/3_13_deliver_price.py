#Стоимость доставки

from email import message
from multiprocessing.connection import deliver_challenge


mass_package = float(input('Enter the mass of the package in gramms: '))

if mass_package <= 0:
    print('Error, mass is incorrect!')
elif mass_package > 0 and mass_package <= 200:
    deliver_price = 150
elif mass_package > 200 and mass_package <= 600:
    deliver_price = 300
elif mass_package > 600 and mass_package <= 1000:
    deliver_price = 400
else:  
    deliver_price = 475
    
total_price = mass_package / 100 * deliver_price

print('Your delivr price will be', format(total_price, ',.1f'), 'Rub')

    