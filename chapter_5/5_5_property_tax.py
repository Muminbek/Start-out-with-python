# property tax

ASSESSMENT_RATE = 0.60
HUNDRED_DOLLARS = 100
TAX_PER_HUNDRED_DOLLARS = 0.72

def main():
    property_value = float(input("Please enter the property's actual value: "))
    assessment_amount = assessment_value(property_value)
    tax_value(assessment_amount)
    
def assessment_value(property_value):
    assess_value = property_value * ASSESSMENT_RATE
    print("Your property's assessment value is $", format(assess_value, ",.2f"))
    return assess_value

def tax_value(property_value):
    total_property_tax = property_value / HUNDRED_DOLLARS * TAX_PER_HUNDRED_DOLLARS
    print("Your total tax is $", format(total_property_tax, ",.2f"))
    return total_property_tax

    
main()