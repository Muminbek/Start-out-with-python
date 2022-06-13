# word index

def create_dict(text):
    infile = open(text, 'r')
    count = 0
    word_index = {}
    for line in infile:
        count +=1
        for word in line.rstrip('\n').split():
            if word not in word_index:
                word_index[word] = [str(count)]
            elif word in word_index:
                word_index[word].append(str(count))
    infile.close()
    return word_index

def create_index_file(dict):
    infile = open('word_index.txt', 'w')
    list = []
    index =0
    for key in dict.keys():
        list.append(key)
        for value in dict[key]:
            list[index] = list[index] + ' ' + value
        index += 1
    list.sort()
    for element in list:
        infile.write(element + '\n')
    infile.close()


def main():
    print('This program creates a word index of the file you request.')
    print('----------------------------------------------------------')
    print()
    infile = input('For which file would you like me to create a word index? ')
    dict = create_dict(infile)
    create_index_file(dict)
    print('Word index is created. File name is: word_index.txt')
 
    
main()
