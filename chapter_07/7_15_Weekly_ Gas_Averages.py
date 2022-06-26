import matplotlib.pyplot as plt

with open('1994_Weekly_Gas_Averages.txt', 'r') as my_file:
    prices = list(map(float, my_file.read().splitlines()))

def main():
    x_cords = range(1, len(prices) + 1)
    y_cords = prices

    plt.plot(x_cords, y_cords)

    plt.title('1994_ Weekly_Gas_Averages')
    plt.xlabel('Weeks')
    plt.ylabel('Average price')
    
    
    plt.grid(True)
    plt.show()

main()