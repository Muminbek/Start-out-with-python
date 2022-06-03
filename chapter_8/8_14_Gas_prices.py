# Gas Prices

def main():
    with open('GasPrices.txt', 'r') as infile:
        infile_list = infile.read().splitlines()
        date_list = []
        price_lists = []
        for line in infile_list:
            date_list.append(line[0:10])
            price_lists.append(line[11:])
        
        
    average_price_per_year(date_list, price_lists)
    average_price_per_month(date_list,price_lists)
    highest_lowest_price_per_year(date_list,price_lists)
    list_of_prices_lowest_to_highest(date_list,price_lists)
    list_of_prices_highest_to_lowest(date_list,price_lists)


def average_price_per_year(dates, prices):
    counter = 0
    year = ''
    accumulator = 0
    average_year_years = []
    average_year_prices = []

    for index in range(len(dates)):
        if year == '':
            year = dates[index][6:]
            accumulator += float(prices[index])
            counter += 1
        elif year == dates[index][6:]:
            accumulator += float(prices[index])
            counter += 1
        else:
            average = accumulator / counter
            average_year_years.append(year)
            average_year_prices.append(average)
            year = dates[index][6:]
            counter = 1
            accumulator = float(prices[index])
    print('Average Price Per Year')
    print('----------------------')
    print('Year\t\tPrice')
    print('----\t\t-----')
    for index in range(len(average_year_years)):
        print(f'{average_year_years[index]}\t--->\t{average_year_prices[index]: ,.3f}')
    print()
    
def average_price_per_month(date,price):
    counter = 0
    month = ''
    year = ''
    accumulator = 0
    average_month = []
    average_price = []
    
    for index in range(len(date)):
        if month == '':
            month = date[index][:2]
        elif year == '':
            year = date[index][6:]
        elif month == date[index][:2] and year == date[index][6:]:
            accumulator += float(price[index])
            counter +=1
            
        else:
            average = accumulator / counter
            average_month.append(f'{year}-{month}')
            average_price.append(average)
            month = date[index][:2]
            year = date[index][6:]
            counter = 1
            accumulator = float(price[index])
    print('Average Price Per Month')
    print('----------------------')
    
    print('Month\t\tPrice')
    print('----\t\t-----')
    for index in range(len(average_month)):
        print(f'{average_month[index]}\t----->\t{average_price[index]: ,.3f}')
    print()

def highest_lowest_price_per_year(dates, prices):
    year = ''
    year_list = []
    highest_per_year = []
    lowest_per_year = []
    find_max_min_price = []

    for index in range(len(prices)):
        prices[index] = float(prices[index])
    for index in range(len(dates)):
        if year == '':
            year = dates[index][6:]
            find_max_min_price.append(prices[index])
            year_list.append(year)
        elif year == dates[index][6:]:
            find_max_min_price.append(prices[index])
        else:
            highest_per_year.append(max(find_max_min_price))
            lowest_per_year.append(min(find_max_min_price))
            year = dates[index][6:10]
            year_list.append(year)
            find_max_min_price = [prices[index]]
            
    highest_per_year.append(max(find_max_min_price))
    lowest_per_year.append(min(find_max_min_price))

    print('Highest and Lowest Prices Per Year')
    print('----------------------------------')
    print('Year\tHigh\tLow')
    print('----\t----\t---')
    for index in range(len(highest_per_year)):
        print(f'{year_list[index]}\t{highest_per_year[index]: ,.3f}\t{lowest_per_year[index]: ,.3f}')  
    print()

def list_of_prices_lowest_to_highest(dates, prices):
    min_to_max_prices = []
    min_to_max_dates = []
    price_list = prices[:]
    date_list = dates[:]
    for _ in range(len(price_list)):
        min_to_max_prices.append(min(price_list))
        index = price_list.index(min(price_list))
        min_to_max_dates.append(date_list[index])
        del date_list[index]
        del price_list[index]
        
    print('List of Prices, Lowest to Highest')
    print('---------------------------------')
    print('Date\t\tPrice')
    print('----\t\t-----')
    outfile = open('LowToHigh.txt','w')
    for index in range(len(min_to_max_prices)):
        print(min_to_max_dates[index],'\t',min_to_max_prices[index])
        outfile.write(f'{min_to_max_dates[index]}:{min_to_max_prices[index]}\n')
    outfile.close()

def list_of_prices_highest_to_lowest(dates, prices):
    max_to_min_prices = []
    max_to_min_dates = []
    price_list = prices[:]
    date_list = dates[:]
    for index in range(len(price_list)):
        max_to_min_prices.append(max(price_list))
        index = price_list.index(max(price_list)) 
        max_to_min_dates.append(date_list[index])
        del date_list[index]
        del price_list[index]
    print('List of Prices, Highest to Lowest')
    print('---------------------------------')
    print('Date\t\tPrice')
    print('----\t\t-----')
    outfile = open('HighToLow.txt','w')
    for index in range(len(max_to_min_prices)):
        print(max_to_min_dates[index],'\t',max_to_min_prices[index])
        outfile.write(f'{max_to_min_dates[index]}:{max_to_min_prices[index]}\n')
    outfile.close()

main()
