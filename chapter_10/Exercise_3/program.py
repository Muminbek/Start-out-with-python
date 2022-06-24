import personal

def main():
    info = []


    for i in range(3):
        name = input(f"Name {i+1}: ")
        address = input(f"Address {i+1}: ")
        age = int(input(f"Age {i+1}: "))
        phone_number = int(input(f"Phone number {i+1}: "))
        print()
        person = personal.Personal_information(name, address, age, phone_number)
        info.append(person)
    print("The data has been saved.\n")   

    print("Here is the information you entered.")

    for item in info:
        print(f'Name: {item.get_name()}')
        print(f'Address: {item.get_address()}')
        print(f'Age: {item.get_age()}')
        print(f'Phone Number: {item.get_phone_number()}')
        print()

if __name__ == '__main__':
    main()