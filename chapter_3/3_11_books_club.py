 #Очки книжного клуба

from email import message


books_count = int(input('Enter amount of books per month: '))

if books_count < 0:
    message = "Error. Enter positive number. \n" + \
                "Re-run programm and try again." 
else:
    message = 'You are awared '
    
    if books_count == 0 and books_count <= 1:
        message += '0 '
    elif books_count >= 2 and books_count <= 3:
        message += '5 '
    elif books_count >= 4 and books_count <= 5:
        message += '15 '
    elif books_count >= 6 and books_count <= 7:
        message += '30 '
    elif books_count >= 8:
        message += '60 '
        
    message += 'points.'
    
print(message)