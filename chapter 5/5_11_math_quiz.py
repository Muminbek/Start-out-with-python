# math quiz
import random

def main():
    first_num = random.randint(1, 1000)
    second_num = random.randint(1, 1000)
    print("Please calculate the sum of two numbers. The numbers are below:")
    print(' ', first_num)
    print('+', second_num)
    result = total_num(first_num, second_num)
    user_answer = int(input("Please enter the total of these two numbers: "))
    user_answer_checker(result, user_answer)

def total_num(first_num, second_num):
    result = first_num + second_num
    return result

def user_answer_checker(result, user_answer):
    if result == user_answer:
         print("\nCongratulations! Your answer", result,"is correct.")
    else:
         print("\nSorry! The answer is", result)

main()
