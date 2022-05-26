# magic square lo shu  

ROWS = 3
COL = 3

def main():
    
    index = 0
    user_number = []

    while index < 9:
        try:
            inp = int(input('Enter numbers between 1-9: '))
            if 1<= inp <=9 and inp not in user_number: 
                user_number.append(inp)
                print('Added')
                index +=1
            else:
                print("Your number is already entered or isn't in range 1-9. Please enter again ")
        except ValueError:
            print('Type Error, please enter only numbers 1-9')

    

    square = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    index2 = 0
    for r in range(ROWS):
        for c in range(COL):
            square[r][c] = user_number[index2]
            index2 +=1

    print("\n\nYour square is below")
    for r in range(ROWS):
        for c in range(COL):
            print(square[r][c], end="\t")
        print()

    row1, row2, row3 = Sum_Rows(square)
    col1, col2,col3 = Sum_Cols(square)
    dig1, dig2 = Sum_Digs(square)


    if row1==row2==row3==col1==col2==col3==dig1==dig2:
        print("\nIt is a Lo Shu Magic Square.")
    else:
        print("\nIt is not a Lo Shu Magic Square.\n")


def Sum_Rows(square):
    total_row1 = 0
    for r in range(ROWS):
        total_row1 += square[0][r-1]
    total_row2 = 0
    for r in range(ROWS):
        total_row2 += square[0][r-1]
    total_row3 = 0
    for r in range(ROWS):
        total_row3 += square[0][r-1]
    return total_row1, total_row2, total_row3

def Sum_Cols(square):
    total_col1 = 0
    for r in range(ROWS):
        total_col1 += square[0][r-1]
    total_col2 = 0
    for r in range(ROWS):
        total_col2 += square[0][r-1]
    total_col3 = 0
    for r in range(ROWS):
        total_col3 += square[0][r-1]
    return total_col1, total_col2, total_col3

def Sum_Digs(square):
    total_dig1 = square[0][0] + square[1][1] + square[2][2]
    total_dig2 = square[0][2] + square[1][1] + square[2][0]
    return total_dig1, total_dig2

main()  
    