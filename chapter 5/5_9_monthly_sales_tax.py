# monthly sales tax

STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

def main():
    total_sales=float(input("Enter the total sales for the month: "))
    c_tax_total=County_Tax_Calculator(total_sales)
    s_tax_total=State_Tax_Calculator(total_sales)
    Total_Tax_Calculator(c_tax_total,s_tax_total)
    
def County_Tax_Calculator(total_sales):
    county_tax = total_sales * COUNTY_TAX_RATE
    print("\nYour county sales tax is $", format(county_tax, ",.2f"), sep='')
    return county_tax

def State_Tax_Calculator(total_sales):
    state_tax=total_sales * STATE_TAX_RATE
    print("Your state sales tax is $", format(state_tax, ",.2f"), sep='')
    return state_tax

def Total_Tax_Calculator(a,b):
    total = a + b
    print("Your total sales tax is $", format(total, ",.2f"), sep='')
    
main()