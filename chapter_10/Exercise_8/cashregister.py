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
    
    def __str__(self):
        return f'Description: {self.__description}'\
               f'\nUnits in Inventory: {self.__units}'\
               f'\nPrice: ${self.__price}'     

# Cash Register class
class CashRegister:
    def __init__(self):
        self.__cart = []

    def purchase_item(self, item):
        descr_list = []
        for i in self.__cart:
            descr_list.append(i.get_description())

        if item.get_description() not in descr_list:
                self.__cart.append(item)
        else:
            for i in range(len(self.__cart)):
                if self.__cart[i].get_description() == item.get_description():
                    self.__cart[i].set_units(self.__cart[i].get_units() + self.__cart[i].get_units())
                    self.__cart[i].set_price(self.__cart[i].get_price() + self.__cart[i].get_price())            
        
    def get_total(self):
        total = 0
        for item in self.__cart:
            total += item.get_price()
        return f'{total:,.2f}'

    def show_items(self):
        print("Your cart")
        for item in self.__cart:
            print(item)
            print("---------------")
    
    def clear(self):
        return self.__cart.clear()
        
    def __len__(self):
        return len(self.__cart)

