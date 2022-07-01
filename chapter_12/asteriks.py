def main():
    asteriks = int(input('How many end of asterisk: '))
    num = 1
    lines(num, asteriks)

def lines(num, n):
    if n > num:
        print(num * '*')
        num += 1
        return lines(num, n)

    elif n == num:
        print(num * '*')
main()
