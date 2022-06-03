# alphabetic telephone number translator

def main():
    
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y''z']
    number =[2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]

    
    phone = input('Enter a phone number in the format xxx-xxx-xxxx: ')
    phone = phone.lower()

    for i in phone:
        if i.isalpha():
            print(number[alpha.index(i)], end='')
        else:
            print(i, end='')
    print()
main()
