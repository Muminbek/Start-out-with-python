import Supervisor
def main():
    
    # get the data from the user.
    print("Please enter the following data.")
    
    emp_name = input("Supervisor Name: ")
    emp_num = int(input("Supervisor Number: "))
    annual_salary = float(input("Please enter annual salary: "))
    annual_bonus = float(input("Please enter your annual bonus: "))
    print()

    supervisor = Supervisor.ShiftSupervisor(emp_name, emp_num, annual_salary, annual_bonus)

    print("Here is the data that you entered for supervisor.")
    print("---------------------------------------------")
    print(f'Name: {supervisor.get_emp_name()}')
    print(f'Employee Number: {supervisor.get_emp_num()}')
    print(f'Annual Salary: ${supervisor.get_annual_salary(): ,.2f}')
    print(f'Annual Bonus: ${supervisor.get_annual_bonus(): ,.2f}')

if __name__ == '__main__':
    main()