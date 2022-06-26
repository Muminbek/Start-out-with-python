# PowerBall lottery

# 5 numbers 1-69
# 1 powerball number 1-26
## import random

## def lottery():
##     numbers = []
##     powerballs = []
##     for i in range(5):
##         number = str(random.randint(1,69))
##         if len(number) == 1:
##             number = '0'+ number
##         numbers.append(number)
##     powerball = str(random.randint(1,26))
##     if powerball == 1:
##         powerball = '0' + powerball
##     powerballs.append(powerball)
##     winning_numbers_list = numbers + powerballs
##     winning_numbers = ''
##     for number in winning_numbers_list:
##         winning_numbers += number + ' '
##     winning_numbers = winning_numbers.rstrip()
    
##     return winning_numbers

## def main():
##     outfile = open('pnumbers.txt', 'w')
##     for i in range(1,655):
##         line = lottery()
##         print(line)
##        outfile.write(line + '/n')
##     outfile.close()
## main() 


from typing import overload


def main():
    infile = open('pbnumbers.txt', 'r')
    
    # Read the file and create a list.
    contents = infile.read().splitlines()

    master_list= unified_list(contents)

    numbers, times = times_each_appears(master_list)
    
    top10common(times, numbers)
    bottom10common(times,numbers)
    top10overdue(numbers)
    seperate_frequency(contents)
    infile.close()


def unified_list(numbers):
    master_list = []
    for draw in numbers:
        draw_list = draw.split()
        master_list += draw_list
    return master_list

def times_each_appears(a_list):
    counter = 0
    times_found = []
    numbers_found = []
    for number in a_list:
        if number not in numbers_found:
            counter = 0
            for searchnumber in a_list:
                if number == searchnumber:
                    counter += 1
        if number not in numbers_found:
            numbers_found.append(number)
            times_found.append(counter)
    return numbers_found, times_found

def top10common(times, numbers):
    top10times = []
    top10numbers = []
    for _ in range(10):
        draw = (times.index(max(times)))
        top10numbers.append(numbers[draw])
        top10times.append(times[draw])
        del numbers[draw]
        del times[draw]
    
    print('Most Common Numbers')
    print('-------------------\n')
    print('Number\t\tTimes')
    print('------\t\t-----')
    for i in range(len(top10numbers)):
        print(top10numbers[i],'\t--->\t', top10times[i])
    print()

def bottom10common(times, numbers):
    top10times = []
    top10numbers = []
    for _ in range(10):
        draw = (times.index(min(times)))
        top10numbers.append(numbers[draw])
        top10times.append(times[draw])
        del numbers[draw]
        del times[draw]
    
    print('Least Common Numbers')
    print('-------------------\n')
    print('Number\t\tTimes')
    print('------\t\t-----')
    for i in range(len(top10numbers)):
        print(top10numbers[i],'\t--->\t', top10times[i])
    print()

def top10overdue(numbers):
    count = 0
    overdue_list = []
    not_seen_list = []
    placeholder = ''

    for number in numbers:
        placeholder = number
        for specific_number in numbers:
            if placeholder == specific_number:
                count = 0
            else:
                count +=1
        overdue_list.append(number)
        not_seen_list.append(count)
    top10overdue =[]
    top10notseenfor =[]
    for count in range(10):
        index = not_seen_list.index(max(not_seen_list))
        top10notseenfor.append(not_seen_list[index])
        top10overdue.append(overdue_list[index])
        del not_seen_list[index]
        del overdue_list[index]
    print("Overdue List")
    print("------------")
    print()
    print('Number\t\tOverdue')
    print('------\t\t-------')
    for index in range(len(top10overdue)):
        print(top10overdue[index] + '\t--->\t' + str(top10notseenfor[index]))
    print()

def seperate_frequency(contents):
    powerballs = []
    powerballs_count = []
    non_powerballs = []
    non_powerballs_count = []
    counter = 0

    for i in range(1,27):
        for draw in contents:
            draw_list = draw.split()
            if int(draw_list[5]) == i:
                counter += 1
        powerballs.append(i)
        powerballs_count.append(counter)
        counter = 0

    for i in range(1,70):
        for draw in contents:
            draw_list = draw.split()
            del draw_list[5]
            for search_number in draw_list:
                if int(search_number) == i:
                    counter += 1
        non_powerballs.append(i)
        non_powerballs_count.append(counter)
        counter = 0

    print('Powerballs Frequency')
    print('--------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(powerballs)):
        print(str(powerballs[index]) + '\t--->\t' + str(powerballs_count[index]))
    print()
    print('Regulars Frequency')
    print('------------------')
    print()
    print('Number\t\tTimes')
    print('------\t\t-----')
    for index in range(len(non_powerballs)):
        print(str(non_powerballs[index]) + '\t--->\t' + str(non_powerballs_count[index]))


main()
