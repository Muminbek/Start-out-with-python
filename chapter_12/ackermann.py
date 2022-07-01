# Ackermann’s Function is a recursive mathematical algorithm that can be used to test how
# well a system optimizes its performance of recursion.
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
    
if __name__ == '__main__':
    m = int(input('Enter first integer: '))
    n = int(input('Enter second integer: '))
    print(ackermann(m, n))
