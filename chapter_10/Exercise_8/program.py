# cash register app menu

import cashregister

# create your CashRegister object to store retail items
cart = cashregister.CashRegister()
PURCHASE = 1
SHOW = 2
CLEAR = 3
QUIT = 4
# prompt user for the description of an item
def main():
    
    choice = 0
    # keep prompting the user for more items until they're done
    while choice!= QUIT:
        choice = display()
        if choice == 1:
            # get the rest of the info for the item being purchased
            name = input("Enter the description of the item: ")   
            quantity = int(input("Enter the quantity you'd like to buy: "))
            price_per_unit = float(input("Enter the price for 1 of the item: "))
            price = quantity * price_per_unit
            
            # create a RetailItem object from this info and place in the cart.
            item = cashregister.RetailItem(name, quantity, price)
            cart.purchase_item(item)
            print('Item has been purchased!')
        elif choice == 2:
            cart.show_items()
            if len(cart) == 0:
                print('Empty') 
            # print out items in the cart as well as total
            print(f'Your total: ${cart.get_total()}')
            print()
        elif choice == 3:
            cart.clear()
            print('Your cart has been cleared!')
            print()
            

def display():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Purchase an item')
    print('2. Show item list')
    print('3. Clear item list')
    print('4. Quit the program')
    print()
    # Get the user's choice.
    try:
        choice = int(input('Enter your choice: '))
        print()
        while choice < PURCHASE or choice > QUIT:
            choice = int(input('Enter a valid choice: '))
        return choice
    except ValueError:
        choice = int(input('Enter a valid choice: '))


if __name__ == '__main__':
    main()
