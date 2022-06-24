import question

def main():
    questions=["What is the capital of Turkey?\n(a) Istanbul\n(b) Ankara\n(c) Izmir\n(d) Antalya",
               "What is the capital of France?\n(a) London\n(b) Paris\n(c) Moscow\n(d) Washington",
               "Where is the Great Pyramids?\n(a) Israel\n(b) Morocco\n(c) Egypt\n(d) Iraq",
               "What is the world's longest river?\n(a) Nile\n(b) Amazon\n(c) Colorado\n(d) Mississippi",
               "What is the capital of Spain?\n(a) Lisbon\n(b) Paris\n(c) Madrid\n(d) Cordoba",
               "When did the Cold War end?\n(a) 1989\n(b) 1990\n(c) 1985\n(d) 1992"]
    
    # create a list of answers with the same index number with
    # associated question.
    answers = ["b", "b", "c", "b", "c", "a"]
    player1 = 0
    player2 = 0
    print("Player 1 questions:")
    print()
    for i in range(0, int(len(questions)/2)):
        print("Question: ", i + 1)
        print(questions[i])
        user_answer = input('Enter correct answer (a,b,c,d): ')
        quest = question.Question(questions[i], answers[i], user_answer)
        quest.test1()
        player1 += quest.get_test1()
    print("Player 2 questions:")
    print()
    for i in range(int(len(questions)/2), len(questions)):
        print("Question: ", i + 1)
        print(questions[i])
        user_answer = input('Enter correct answer (a,b,c,d): ')
        quest = question.Question(questions[i], answers[i], user_answer)
        quest.test2()
        player2 += quest.get_test2()
        
    
    if player1 > player2:
        print('Player 1 has won!')
    elif player2 > player1:
        print('Player 2 has won!')
    else:
        print('It is a draw!')
    print()
    print(f'Player 1 score: {player1}')
    print(f'Player 2 score: {player2}')

if __name__ == '__main__':
    main()