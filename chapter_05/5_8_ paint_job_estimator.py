# paint job estimator
FOR_SQUARE_METER = 10       
PAINT_FOR_SQUARE_METER = 5  # 5 litres on 10 square metres
LABOR_FOR_SQUARE_METER = 8  # 8 hours labor on 10 square metres
CHARGE_FOR_HOUR = 20        # 20$ per hour of labor

def main():
    wall_space=float(input("Enter the square meter of wall to be painted: "))
    price_paint=float(input("Enter the price of the paint litres: \n"))
    num_litr = number_of_litres(wall_space)
    num_hour = number_of_hours(wall_space)
    cost_paint = cost_of_paint(num_litr, price_paint)
    cost_labor = Labor_charges(num_hour)
    Total_of_charges(cost_paint, cost_labor)

def number_of_litres(wall_space):
    num = wall_space / FOR_SQUARE_METER * PAINT_FOR_SQUARE_METER
    print('You will need', num, 'litres of paint.')
    return num

def number_of_hours(wall_space):
    num = wall_space / FOR_SQUARE_METER * LABOR_FOR_SQUARE_METER
    print('You will need', num, 'hours of labor')
    return num

def cost_of_paint(num_litr, price_paint):
    num = num_litr * price_paint
    print('The cost of paint is $', format(num, ",.2f"), sep='')
    return num

def Labor_charges(num_hour):
    num = num_hour * CHARGE_FOR_HOUR
    print("The cost of labor is $", format(num, ",.2f"), sep='')
    return num

def Total_of_charges(cost_paint, cost_labor):
    num = cost_paint + cost_labor
    print("Your total charges are $", format(num, ",.2f"), sep='')
    
main()
