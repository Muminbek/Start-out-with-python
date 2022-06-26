#driver's license exam

def main():
    correct_answers=["A", "C", "A", "A", "D",
                     "B", "C", "A", "C", "B",
                     "A", "D", "C", "A", "D",
                     "C", "B", "B", "D", "A"]

    my_file = open('answers.txt', 'r')
    my_answers = my_file.read().splitlines()
    my_file.close()
    total_correct = answers_comparing(correct_answers, my_answers)
    if total_correct >= 15:
        print("Congratulations! You passed the exam. You have", total_correct, " answers.")
    else:
        print("You failed the exam. You have", total_correct, " answers.")

def answers_comparing(cor, my):
    index = 0
    total = 0
    while index < len(cor):
        if cor[index] == my[index]:
            total += 1
        else:
            print(f'The question #{index+1} is wrong!', sep="")
        index += 1
    return total


main()