#Калькулятор сосисок для пикника

SAUSAGE_PACK = 10 #in one pack
BURGER_PACK = 8   #in one pack

hot_dog_amount = int(input('amount of hot-dogs per person: '))
people_amount = int(input('amount of people: '))

total_hot_dogs = hot_dog_amount * people_amount 

needed_pack_sas = total_hot_dogs // SAUSAGE_PACK
needed_pack_bur = total_hot_dogs // BURGER_PACK
sas_rem = total_hot_dogs % SAUSAGE_PACK
bur_rem = total_hot_dogs % BURGER_PACK
    
    
print('You need', needed_pack_sas,  'packages of sausage')

print('You need', needed_pack_bur, 'packages of burger')

if sas_rem > 0:
    print(sas_rem, 'sausages will left over')
if bur_rem > 0:
    print(bur_rem, 'burgers will left over')