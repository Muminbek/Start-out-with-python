#future value
def main():
    present_value = float(input("Enter the account's present value: "))
    interest_rate = float(input("Please enter the monthly interest rate: "))
    months = int(input("Please enter the months that the money will be left in the account: "))
    future_value = FutureValueCalculator(present_value,interest_rate,months)
    print("\nYour future value after", months, "months", end='')
    print(" is $", format(future_value, ",.2f"), sep='')
    
def FutureValueCalculator(a, b, c):
    future_value=c*(a*(b/100)) + a
    return future_value

main()
