# average grade

def main():
    # ask user to enter test scores
    grade1=int(input("Enter the grade for test 1: "))
    grade2=int(input("Enter the grade for test 2: "))
    grade3=int(input("Enter the grade for test 3: "))
    grade4=int(input("Enter the grade for test 4: "))
    grade5=int(input("Enter the grade for test 5: "))

    print("\nScore\t\tLetter Grade")
    print("-------------------------")

    determine_grade(grade1, grade2, grade3, grade4, grade5)
    average = calc_average(grade1, grade2, grade3, grade4, grade5)
    print('\nYour average is', format(average, ",.2f"))
          
          
def calc_average(grade1, grade2, grade3, grade4, grade5):
    average = (grade1 + grade2 + grade3 + grade4 + grade5) / 5
    return average
    
def determine_grade(grade1, grade2, grade3, grade4, grade5):
    for grade in (grade1, grade2, grade3, grade4, grade5):
        if grade>=90 and grade<=100:
            print(grade, "\t\t", "A")
        elif grade>=80 and grade<=89:
            print(grade, "\t\t", "B")
        elif grade>=70 and grade<=79:
            print(grade, "\t\t", "C")
        elif grade>=60 and grade<=69:
            print(grade, "\t\t", "D")
        elif grade>=0 and grade<60:
            print(grade, "\t\t", "F")
        else:
            print("Error! You entered an invalid test score!")
    
main()