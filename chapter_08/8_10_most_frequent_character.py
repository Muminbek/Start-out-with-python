# most frequent character
def main():


    user_string = input('Enter string: ')
    char_list = []
    occurences = []

    for ch in user_string.lower():
        if ch.isalnum():
            if ch not in char_list:
                char_list.append(ch)
                occurences.append(1)
            elif ch in char_list:
                index = char_list.index(ch)
                occurences[index] +=1
    
    winner = char_list[occurences.index(max(occurences))]

    print(f'\nThe most frequently occuring letter is "{winner}" with {max(occurences)} occurences.')

main()
