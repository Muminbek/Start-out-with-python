import random


with open('8_ball_responses.txt', 'r') as my_file:
    responses = my_file.read().splitlines()


print('Hello World, I am the Magic 8 Ball, What is your name?')
name = input()
print('hello ' + name)

def main():
    print('Ask me a question.')
    input()
    print(responses[random.randint(0, len(responses) -1)])
    print('I hope that helped!')
    Replay()

def Replay():
    print ('Do you have another question? [y/n] ')
    reply = input()
    if reply == 'y':
        main()
    elif reply == 'n':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()

main()