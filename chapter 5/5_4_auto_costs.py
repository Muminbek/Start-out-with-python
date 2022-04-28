# auto costs

def main():
    
    loan = loan_payment()
    insurance = insurance_cost()
    gas = gas_cost()
    oil = oil_cost()
    tires = tires_cost()
    maintenance = maintenance_cost()
    monthly_total = total_expenses_monthly(loan, insurance, gas, oil, tires, maintenance)
    yearly_total = total_expenses_yearly(loan, insurance, gas, oil, tires, maintenance)
    
    print("\nYour monthly total cost is $", format(monthly_total, ',.2f'), sep='')
    print("Your yearly total cost is $", format(yearly_total, ',.2f'), sep='')
    
def loan_payment():
    return float(input('Please enter the cost of loan: '))


def insurance_cost():
    return float(input('Please enter the cost of insurance: '))

def gas_cost():
    return float(input('Please enter cost of gas: '))

def oil_cost():
    return float(input('Please enter the cost of oil: '))
    

def tires_cost():
    return float(input('Please enter the cost of tires: '))

def maintenance_cost():
    return float(input('Please enter the cost of maintenance: '))

def total_expenses_monthly(loan, insurance, gas, oil, tires, maintenance):
    return loan + insurance + gas + oil + tires + maintenance

def total_expenses_yearly(loan, insurance, gas, oil, tires, maintenance):
    return (loan + insurance + gas + oil + tires + maintenance) * 12

main()