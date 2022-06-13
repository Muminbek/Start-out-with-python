# word frequency

def main():
    frequency = {}

    with open('uniquewords.txt', 'r') as myfile:
        text = myfile.read().splitlines()
    
    freq_dict = Counter(frequency, text)
    print('Enter the word from below for counting')
    print(freq_dict)
    print()
        
    try:
        key = input("Enter a word to see its frequency in given text: ").lower()
        print(freq_dict[key])
    except KeyError as err:
        print(err)
        main()
def Counter(freq, text):
    for line in text:
        for word in line.split():
            if word not in freq:
                freq[word.lower()] = 1
            else:
                freq[word.lower()] += 1
    return freq

main()


