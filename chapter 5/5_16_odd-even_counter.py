#odd/even counter
import random

def main():
    #counters:
    total_odd = 0
    total_even = 0
    
    for i in range(100):
        r_int = get_r_integer()
        if r_int % 2 == 0:
            total_even += 1
        elif r_int % 2 == 1:
            total_odd += 1
    print('There are', total_even, "even numbers and", total_odd, "total_odd in the list.")
    
    
def get_r_integer():
    r_int = random.randrange(10000)
    return r_int

main()