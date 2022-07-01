def main():
    x = int(input("Enter a positive non-zero integer for X: "))
    y = int(input("Enter a positive non-zero integer for Y: "))

    result = multiply(x, y)
    
    # display the result
    print()
    print(f"The multiplication of {x} and {y} is {result}")

def multiply(x, y):
    if x == 1:
        return y
    else:
        return y + multiply(x-1, y)

if __name__ == '__main__':
    main()