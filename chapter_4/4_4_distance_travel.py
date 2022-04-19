
average_speed = int(input('What is the speed of the vehicle in km/h? '))
time = int(input('How many hours did it move? '))


print("\nHour \t Distance traveled")
print("--------------------------")

for hour in range(1, time + 1):
    distance_traveled = hour * average_speed
    
    print(hour, '\t', distance_traveled)
    