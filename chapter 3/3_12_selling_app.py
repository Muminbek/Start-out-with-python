#Реализация программного обеспечения


amount_packages = int(input("Enter how many packages you have bought: "))
packages = 99 #price of packages
total_summ = amount_packages * packages
if amount_packages > 0 and amount_packages < 10:
    message = 'You did not bought enaugh packages for discount!'
else:
    message = 'You bought pakcages for $'
    
    if amount_packages >= 10 and amount_packages >= 19:
        discount = total_summ * 0.1
        final_summ = total_summ - discount
        message += f'{final_summ} with ${discount} discount'
    elif amount_packages >= 20 and amount_packages >= 49:
        discount = total_summ * 0.2
        final_summ = total_summ - discount
        message += f'{final_summ} dollars with ${discount} discount'
    elif amount_packages >= 50 and amount_packages >= 99:
        discount = total_summ * 0.3
        final_summ = total_summ - discount
        message += f'{final_summ} dollars with ${discount} discount'
    elif amount_packages >= 100:
        discount = total_summ * 0.4
        final_summ = total_summ - discount
        message += f'{final_summ} dollars with ${discount} discount'    
    
print(format(message))
