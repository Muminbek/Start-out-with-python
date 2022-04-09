#Time calculator

total_second = int(input('Enter number of seconds: '))
message = ''

if total_second < 0:
    message = "Enter a number above 0.\n" \
              "Rerun program and try again."
else:
    if total_second >= 0 and total_second < 60:
        seconds = format(total_second % 60)
        message += 'Seconds = ' + seconds
    elif total_second >= 60 and total_second <3600:
        minutes = format(total_second // 60)
        seconds = format(total_second  % 60)
        message += 'Minutes =' + minutes + '\n'\
                   'Seconds = ' + seconds
    elif total_second >= 3600 and total_second < 86400:
        hours = format(total_second // 3600)
        minutes = format((total_second % 3600) // 60)
        seconds = format((total_second % 3600) % 60)
        message += 'Hours = ' + hours + '\n'\
                   'Minutes = ' + minutes + '\n'\
                   'Seconds = ' + seconds
    elif total_second >= 86400:
        days = format(total_second // 86400)
        hours = format((total_second % 86400) // 3600)
        minutes = format(((total_second % 86400) % 3600) // 60)
        seconds = format(((total_second % 86400) % 3600) % 60)
        message += 'Day = ' + days + '\n'\
                   'Hours = ' + hours + '\n'\
                   'Minutes = ' + minutes + '\n'\
                   'Seconds = ' + seconds
                   
print(message)