from calendar import month
from functools import total_ordering


years = int(input('Enter years: '))
total_amount_rainfall_mm = 0
month_amount = years * 12
counter = 0

for x in range(years):
        
    for y in range(12):
        
        counter += 1
        
        rainfall_mm = int(input(f'Enter millimetrs of rainfall, month {counter}: '))
        
        total_amount_rainfall_mm += rainfall_mm
        
average_mm_rainfall = total_amount_rainfall_mm // month_amount
        

        
print('Amount of month: ', month_amount)
print('Total millimetrs of rainfall: ', total_amount_rainfall_mm)
print('Average rainfall per month: ', average_mm_rainfall)