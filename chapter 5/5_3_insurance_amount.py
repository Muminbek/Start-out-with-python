# Insurance amount

MINIMAL_INSURANCE = 80

def main():
    building_cost = float(input('Enter your building amount: '))
    m_insurance(building_cost)
    
    
def m_insurance(insurance_amount):
    insurance_amount *= (MINIMAL_INSURANCE / 100)
    print('Your insurance amount is $', format(insurance_amount, ',.2f'), sep='')

main()
