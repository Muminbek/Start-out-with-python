#Селектор ресторанов

message = ''

vegetarian_answer = input('Будет ли на ужине вегетарианец? \n(д/н) Введите "д" для да или "н" для нет\n')

if vegetarian_answer == 'д' or vegetarian_answer == 'н':
    vegan_answer = input('Будет ли на ужине веганец?\n')
    
    if vegan_answer =='д' or vegan_answer == 'н':
        gluten_answer = input('Будет ли на ужине приверженец безглютеновой диеты?\n')
        
        if gluten_answer == 'д' or gluten_answer == 'н':
            message = '\nВот ваши варианты ресторанов: \n'
            
            if vegetarian_answer == 'д':
                
                if vegan_answer == 'д':
                    
                    if gluten_answer == 'д' or gluten_answer == 'н':
                        message +=  'Кафе за углом\n' + \
                                    'Кухня шеф-повара'
                else: #vegan_answer == 'н'
                    if gluten_answer == 'д':
                        message +=  'Центральная пиццерия\n' + \
                                    'Кафе за углом\n' + \
                                    'Кухня шеф-повара'
                    else:
                        message +=  'Центральная пиццерия\n' + \
                                    'Кафе за углом\n' + \
                                    'Блюда от итальянской мамы\n' + \
                                    'Кухня шеф-повара'
            else: #vegetarian_answer == 'н'
                
                if vegan_answer == 'д':
                    
                    if gluten_answer == 'д' or gluten_answer == 'н':
                        message +=  'Кафе за углом\n' + \
                                    'Кухня шеф-повара'
                else:
                    if gluten_answer == 'д':
                        message +=  'Центральная пиццерия\n' + \
                                    'Кафе за углом\n' + \
                                    'Кухня шеф-повара'
                    else:
                        message +=  'Изысканые гамбургеры от джо\n' + \
                                    'Центральная пиццерия\n' + \
                                    'Кафе за углом\n' + \
                                    'Блюда от итальянской мамы\n' + \
                                    'Кухня шеф-повара'
        
        else:
            print('Пожалюста (д/н) Введите "д" для да или "н" для нет>> Перезапустите программу и попробуйте снова.')
    else:
        print('Пожалюста (д/н) Введите "д" для да или "н" для нет>> Перезапустите программу и попробуйте снова.')
else:
     print('Пожалюста (д/н) Введите "д" для да или "н" для нет>> Перезапустите программу и попробуйте снова.')                                           
                                    
                                    
                                    
print(message)
    