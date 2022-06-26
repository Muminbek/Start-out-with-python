# ShiftSupervisor class
class Employee:
    def __init__(self, emp_name, emp_num) -> None:
        self.__emp_name = emp_name
        self.__number = emp_num

    def set_emp_name(self, emp_name):
        self.__emp_name = emp_name

    def set_emp_num(self, emp_num):
        self.__number = emp_num

    def get_emp_name(self):
        return self.__emp_name

    def get_emp_num(self):
        return self.__number

class ShiftSupervisor(Employee):
    def __init__(self, emp_name, emp_num, annual_salary, ann_bonus):
        super().__init__(emp_name, emp_num)
        self.__annual_salary = annual_salary
        self.__annual_bonus = ann_bonus
    
    def get_annual_salary(self):
        return self.__annual_salary
    
    def get_annual_bonus(self):
        return self.__annual_bonus
