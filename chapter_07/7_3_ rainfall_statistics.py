# rainfall statistics

def main():
    rainfall_monthly = get_rainfall()

    index = 0
    total = 0.0
    while index <len(rainfall_monthly):
        total += rainfall_monthly[index]
        index += 1

    print()
    print("The total rainfall is", total)
    print("The average monthly rainfall is", total/12)

    print("The minimum rainfall was", min(rainfall_monthly), "in the month #", end="")
    print(rainfall_monthly.index(min(rainfall_monthly))+1)

    print('The maximum rainfall was', max(rainfall_monthly), 'in tne month #', end='')
    print(rainfall_monthly.index(max(rainfall_monthly))+1)


def get_rainfall():
    index = 0
    rainfall = []
    while index < 12:
        print("Enter the total rainfall for month #", index+1, end="")
        rainfall.append(float(input(': ')))
        index += 1

    return rainfall

main()
