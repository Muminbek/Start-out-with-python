# total sales

def main():
    sales = get_sales()
    total = get_total_sales(sales)
    print("\nTotal sales is $", total, sep='')

def get_sales():
    index = 0
    sales = [0]*7
    while index < len(sales):
        print("Please enter the sales for day #", index+1, sep="", end='')
        sales[index] = float(input(': '))    # type: ignore
        index +=1

    return sales

def get_total_sales(sales):
    total = 0
    index = 0

    while index < len(sales):
        total += sales[index]
        index += 1
    return total

main()
