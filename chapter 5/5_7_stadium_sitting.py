#stadium sitting

CLASS_A_PRICE = 20
CLASS_B_PRICE = 15
CLASS_C_PRICE = 10

def main():
    class_a_numbers=int(input("How many Class A tickets are sold?: "))
    class_b_numbers=int(input("How many Class B tickets are sold?: "))
    class_c_numbers=int(input("How many Class C tickets are sold?: "))
    a = class_a_solded(class_a_numbers)
    b = class_b_solded(class_b_numbers)
    c = class_c_solded(class_c_numbers)
    total(a, b, c)

def class_a_solded(class_a_numbers):
    a_class = class_a_numbers * CLASS_A_PRICE
    print('\nA class sittings income: $', format(a_class, ",.2f"), sep='')
    return a_class

def class_b_solded(class_b_numbers):
    b_class = class_b_numbers * CLASS_B_PRICE
    print('B class sittings income: $', format(b_class, ",.2f"), sep='')
    return b_class 
   
def class_c_solded(class_c_numbers):
    c_class = class_c_numbers * CLASS_C_PRICE
    print('C class sittings income: $', format(c_class, ",.2f"), sep='')
    return c_class

def total(a, b, c):
    total = a + b + c
    print("\nThe total income generated from tickets are $", format(total, ",.2f"), sep='')

main()