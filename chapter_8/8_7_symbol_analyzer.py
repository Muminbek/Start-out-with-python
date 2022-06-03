def main():
    with open('text.txt', 'r') as file:
        text = file.read()

    uppercase = 0
    lowercase = 0
    digits = 0
    whitespace = 0
    
    for s in text:
        if s.isupper():
            uppercase += 1
        elif s.islower():
            lowercase += 1
        elif s.isdigit():
            digits += 1
        elif s.isspace():
            whitespace += 1

    print("The number of uppercase letters in the file is", uppercase)
    print("The number of lowercase letters in the file is", lowercase)
    print("The number of digits in the file is", digits)
    print("The number of whitespace characters in the file is", whitespace)


    
main()