
sum = 0
number = 0

while number >= 0:
    
    sum += number
    number = int(input('Enter positive number to continue or negative number to end: '))
    
print()  
print('Sum of numbers: ', sum)