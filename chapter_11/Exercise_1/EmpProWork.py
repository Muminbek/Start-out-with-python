#  Employee and ProductionWorker classes
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

class ProductionWorker(Employee):
    def __init__(self, emp_name, emp_num, shift_num, pay_rate):
        super().__init__(emp_name, emp_num)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

    def set_shift_num(self, shift_num):
        self.__shift_num = shift_num

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    
    def get_shift_num(self):
        if self.__shift_num==1:
            return "Day"
        if self.__shift_num==2:
            return "Night"

    def get_pay_rate(self):
        return self.__pay_rate

    