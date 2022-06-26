import  EmpProWork

def main():
    print("Please enter the following data.")
    emp_name = input('Employee Name: ')
    emp_num  = int(input('Employee Number: '))
    shift_num = int(input('Shift Number (1 for day 2 for night): '))
    pay_rate = float(input('Enter hourly pay rate: '))

    emp_info = EmpProWork.ProductionWorker(emp_name, emp_num, shift_num, pay_rate)

    print("Here is the data that you entered.")
    print("------------------------------------")
    print(f"Name: {emp_info.get_emp_name()}\n"\
        f"Employee Number: {emp_info.get_emp_num()}\n"\
        f"Shift time: {emp_info.get_shift_num()}\n"\
        f"Hourly pay rate: ${emp_info.get_pay_rate(): ,.2f}")
        
if __name__ == '__main__':
    main()
    