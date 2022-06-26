# Sales Tax

# get the amount of purchase
def main():
    
    purchase = float(input("Enter the amount of purchase: "))
    
    print("\nYour purchase amount is $", purchase, '\n', sep='')

    s_tax = state_tax(purchase)
    c_tax = county_tax(purchase) 
    t_tax = total_tax(s_tax, c_tax)
    total(purchase, t_tax)
    
# subtasks
def state_tax(arg):
    result = arg * 0.05
    print("Your state tax is $", format(result, ".2f"), sep='')
    return result
    
def county_tax(arg):
    result = arg * 0.025
    print("Your county tax is $", format(result, ".2f"), sep='')
    return result

def total_tax(arg, arg2):
    result = arg + arg2
    print("Your total tax is $", format(result, ".2f"), sep='')
    return result

def total(arg, arg2):
    result = arg + arg2
    print("\nYour total is $", result, sep='')
    
# call amin function
main()
    