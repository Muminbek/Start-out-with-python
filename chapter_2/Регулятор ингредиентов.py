#Регулятор ингредиентов
sugar = 1.5 /48
oil = 1 / 48
flour = 2.75 / 48

amount = float(input('количества булочек'))
print(format(sugar * amount, '.2f'), 'стакана сахара')
print(format(oil * amount, '.2f'), 'стакан масла')
print(format(flour * amount, '.2f'), 'стакана муки')
