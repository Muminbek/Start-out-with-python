# Recursive printing
def main():
    print("This program displays the numbers from \
1 up through the 'n' that you stated")

    begin = 1
    end = int(input('Please enter an integer: '))
    show_num(begin, end)
    
def show_num(b, e):
    if b < e:
        print(b)
        return show_num(b + 1, e)
    elif b == e:
        print(b)
        
if __name__ == '__main__':
    main()

