# pig latin

def main():
    user_sentence = input('Enter sentence: ').upper()

    word_list = user_sentence.split()

    for word in word_list:
        print(word[1:], word[0], 'AY', sep='', end='')
    print()
main()

