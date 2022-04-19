
CAL_PER_MIN = 4.2
minutes = 5

for x in range(10, 31, 5):
    
    
    res = minutes * CAL_PER_MIN
    
    print('Burned caloreies in', minutes, 'minutes is', format(res, '.1f'))