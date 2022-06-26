def main():
    with open('uniquewords.txt', 'r') as infile:
        lines = infile.read().splitlines()

    unique_words = set()

    for line in lines:
        unique_words.add(line)

    print("Unique words are below: ")
    print(unique_words)
    
main()