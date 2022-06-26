import PersonCustomer

def main():
    # get the data from the user.
    print("Please enter the following data.")
    name = input("Name: ")
    address = input("Address: ")
    phone_num = input("Phone number: ")
    cust_num = int(input("Customer number: "))
    mail_list = input("Do you want to be in our mailing list? (y/n): ")
    
    # create the object with these data attributes
    customer = PersonCustomer.Customer(name, address, phone_num, cust_num, mail_list)

    print()
    print("Here is the data you entered.")
    print("------------------------------")
    print(f"Name: {customer.get_name()}")
    print(f"Address: {customer.get_address()}")
    print(f"Phone number: {customer.get_tel_num()}")
    print(f"Customer number: {customer.get_cust_num()}")
    print(f"Mailing List: {'Yes' if customer.get_mail_list() else 'No'}")

if __name__ == '__main__':
    main()