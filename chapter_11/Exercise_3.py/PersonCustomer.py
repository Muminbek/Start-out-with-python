#Person and Customer classes
class Person:
    def __init__(self, name, address, tel_num):
        self.__name = name
        self.__address = address
        self.__tel_num = tel_num

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_tel_num(self):
        return self.__tel_num

class Customer(Person):
    def __init__(self, name, address, tel_num, cust_num, mail_list):
        super().__init__(name, address, tel_num)      
        self.__cust_num = cust_num
        self.__mail_list = mail_list

    def get_cust_num(self):
        return self.__cust_num

    def get_mail_list(self):
        if self.__mail_list.lower() == 'y': 
            return True
        else:
            return False
    
