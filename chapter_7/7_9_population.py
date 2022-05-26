def main():
    with open('USPopulation.txt','r') as pop_file:
        population = list(map(int, pop_file.read().splitlines()))
        
    annual_change = AnnualChange(population)
    total = 0
    for x in annual_change:
        total += x
    
    average = total / len(annual_change)

    print(f"The average annual change in population between 1950 and 1990 is {average:.2f}")
    print('The greatest increase in population occured in the year of',\
        annual_change.index(max(annual_change))+1951, 'with an increase of', max(annual_change))
    print('The smallest increase in population occured in the year of', \
        annual_change.index(min(annual_change))+1951, 'with an increase of', min(annual_change))

    print()
    print("Years\t\tAnnual Change")
    print("-----------------------------")
    for i in range(40):
        print(f'{i+1950} - {i+1951}\t\t{annual_change[i]}')

def AnnualChange(pop):
    index = 0
    annual = [0] * (len(pop)-1)
    for _ in annual:
        annual[index] = pop[index+1] - pop[index]
        index += 1
    return annual
    
main()