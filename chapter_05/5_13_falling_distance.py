# falling distance

G = 9.8

def main():
    
    print("Seconds\t\tDistance in Meters")
    print("----------------------------------")
    
    for i in range(1, 11, 1):
        distance = falling_distance(i)
        print(i, '\t\t', format(distance, ',.2f'))
        
def falling_distance(time):
    distance = (1/2) * G * time**2
    return distance

main()