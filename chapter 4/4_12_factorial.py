#factorial

user_number = int(input('Enter above 0 number: '))

while user_number <= 0:
    user_number = int(input('Can only enter number > 0: '))

factorial = 1

for n in range(1, user_number + 1):
    
    factorial *= n
    
print("Factorial of", user_number, "is", factorial)