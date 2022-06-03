# average number of words

def main():

    with open('text.txt', 'r') as file:
        text = file.read().splitlines()
        
    line_count=0
    total_word_count=0
    
    for t in text:
        line_count += 1
        total_word_count += len(t.split())
    
    average = total_word_count/line_count
    
    print('The average number of words per sentence is', format(average, '.2f'))
    table = input("If you want to see the table of each line with a count of words enter y: ")
    print()
    if table.lower() == 'y':
        line_count=0
        total_word_count=0
        print("Line\t\tWord Count")
        print("------------------------")
        for line in text:
            line_count+=1
            print(line_count, end="\t\t")
            word_count=len(line.split())
            print(word_count)

    
main()