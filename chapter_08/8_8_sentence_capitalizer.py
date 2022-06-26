# sentence capitalizer
def main():
    sentence = input('Enter a sentence: ')
    sentence = sentence.split('.')
    capitalizer(sentence)

def capitalizer(s):
    
    for i in s:
        print(f'{i.strip().capitalize()}. ',  end='')

    print()

main()