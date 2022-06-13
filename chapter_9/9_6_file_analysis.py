

def main():
    with open('fileanalysis_1.txt', 'r') as myfile:
        lines1= myfile.readlines()
    with open('fileanalysis_2.txt', 'r') as myfile:
        lines2= myfile.readlines()

    unique_words1 = UniqueWords(lines1)
    unique_words2 = UniqueWords(lines2)

    print("Unique words for <<<fileanalysis_1.txt>>> are listed below.")
    print(unique_words1)
    print()
    print("Unique words for <<<fileanalysis_2.txt>>> are listed below.")
    print(unique_words2)

    print()
    print("List of words that appear in both files:")
    print(unique_words1.intersection(unique_words2))

    print()
    print("List of words that appear in the first file but not the second:")
    print(unique_words1.difference(unique_words2))

    print()
    print("List of words that appear in the second file but not the first:")
    print(unique_words2.difference(unique_words1))

    print()
    print("List of words that appear in either the first or second file but not both:")
    print(unique_words1.symmetric_difference(unique_words2))


def UniqueWords(lines):
    unique_words = set()
    for line in lines:
        for word in line.split():
            unique_words.add(word)

    return unique_words
main()