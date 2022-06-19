import car

def main():
    auto = car.Car('2022', 'Cobalt')

    for _ in range(5):
        auto.accelerate()
        print(f'Current speed is: {auto.get_speed()}')
    
    for _ in range(5):
        auto.brake()
        print(f'Current speed is: {auto.get_speed()}')
main()
