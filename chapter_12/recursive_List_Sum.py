#  Recursive List Sum

def  List_Sum(x):

    if len(x) == 0:
        return 0
    else:
        return x[0] + List_Sum(x[1:])

if __name__ == '__main__':
    x = [4, 5, 7, 6, 2]
    print(List_Sum(x))
    