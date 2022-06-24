#class Question

class Question:
    player1 = 0
    player2 = 0

    def __init__(self, question, answer, user_answer):
        self.question = question
        self.answer = answer
        self.user_answer = user_answer

    def test1(self):
        if self.answer == self.user_answer:
            print('Correct')
            print()
            Question.player1 += 1
        else:
            print(f'Wrong! The correct answer is {self.answer}')
            print()
    
    def get_test1(self):
        return Question.player1
    
    def test2(self):
        if self.answer == self.user_answer:
            print('Correct')
            print()
            Question.player2 += 1
        else:
            print(f'Wrong! The correct answer is {self.answer}')
            print()

    def get_test2(self):
        return Question.player2

