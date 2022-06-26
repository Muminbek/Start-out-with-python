# morse code converter

from turtle import position


def main():
    user_input = input("Enter a string to be converted into morse code: ")
    user_input = user_input.upper()
    user_input = list(user_input)

    print(user_input)
    converter(user_input)
    print()

def converter(a):
    
    character=[" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7",\
               "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", \
               "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", \
               "W", "X", "Y", "Z"]
    morse=[" ", "--..--", ".-.-.-", "..--..", "-----", ".----", "..---", "...--", \
           "....-", ".....", "-....", "--...", "---..", "----.", ".-", "-...", "-.-.", \
           "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", \
           ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.-", "--.."]

    for ch in a:
        position = character.index(ch)
        print(morse[position], end='')


main()