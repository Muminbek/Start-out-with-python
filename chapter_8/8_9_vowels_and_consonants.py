# vowels and consonants
def main():


    user_string = input("Enter a string to count vowels and consonants: ").lower()    # lowercase it.
    vowel, consonant = VowelConsonantCounter(user_string)
    print()
    print("Number of vowels:", vowel, "and number of consonants is", consonant)

def VowelConsonantCounter(a):
    vowel_list=["a", "e", "i", "o", "u"]
    vowel=0
    consonant=0

    for ch in a:
        if ch.isalpha():
            if ch in vowel_list:
                vowel += 1
            else:
                consonant +=1
    return vowel, consonant

main()