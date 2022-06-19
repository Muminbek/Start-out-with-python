import pets

def main():
    name = input("Enter a animal name: ")
    animal_type = input("Enter the animal type: ")
    age = int(input("Enter the age: "))

    animal = pets.Pet(name, animal_type, age)


    print()
    print(f"Name: {animal.get_name()}")
    print(f"Animal Type: {animal.get_animal_type()}")
    print(f"Age: {animal.get_age()}")

main()

    
