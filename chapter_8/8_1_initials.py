from os import sep


def main():
    initials = input('Enter your full name: ')

    init = initials.split()
    print('Your initials')
    for ch in init:
        print(f'{ch[0]}.',sep='', end='')
    print()


main()
