# Retail item class 

class RetailItem:
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price
    
    def set_descripition(self, description):
        self.__description = description
    
    def set_units(self, units):
        self.__units = units
    
    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description
    
    def get_units(self):
        return self.__units
    
    def get_price(self):
        return self.__price
    

