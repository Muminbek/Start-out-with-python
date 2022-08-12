import sqlite3

def main():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    choice = 0
    while choice != 8:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            # Display a list of cities sorted by population, in ascending order.
            disp_sort_asc(cur)
        elif choice == 2:
            # Display a list of cities sorted by population, in descending order.
            disp_sort_desc(cur)
        elif choice == 3:
            # Display a list of cities sorted by name.
            disp_sort_name(cur)
        elif choice == 4:
            # Display the total population of all the cities.
            disp_tot_pop(cur)
        elif choice == 5:
            # Display the average population of all the cities.
            disp_avg_pop(cur)
        elif choice == 6:
            # Display the city with the highest population.
            disp_high_pop(cur)
        elif choice == 7:
            # Display the city with the lowest population.
            disp_low_pop(cur)

    conn.close()    

def display_menu():
    print()
    print('---------Display menu--------')
    print('1. Display a list of cities sorted by population, in ascending order.')
    print('2. Display a list of cities sorted by population, in descending order.')
    print('3. Display a list of cities sorted by name.')
    print('4. Display the total population of all the cities.')
    print('5. Display the average population of all the cities.')
    print('6. Display the city with the highest population.')
    print('7. Display the city with the lowest population.')
    print('8. Exit the program')

def get_menu_choice():
    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the input.
    while choice < 1 or choice > 8:
        print(f'Valid choices are 1 through 8.')
        choice = int(input('Enter your choice: '))
    print()
    return choice

def disp_sort_asc(cur):
    cur.execute('''SELECT * FROM Cities
                ORDER BY Population''')
    results = cur.fetchall()
    print('List of cities sorted by population, in ascending order.\n')
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

def disp_sort_desc(cur):
    cur.execute('''SELECT * FROM Cities
                ORDER BY Population''')
    results = cur.fetchall()
    print('List of cities sorted by population, in descending order.\n')
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

def disp_sort_name(cur):
    cur.execute('''SELECT * FROM Cities
                ORDER BY CityName''')
    results = cur.fetchall()
    print('List of cities sorted by name.\n')
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

def disp_tot_pop(cur):
    cur.execute('''SELECT SUM(Population)
                    FROM Cities''')
    
    print('Total population of all the cities.')
    result = cur.fetchone()
    print(f'{result[0]:,.0f}')

def disp_avg_pop(cur):
    cur.execute('''SELECT AVG(Population)
                    FROM Cities''')
    
    print('Average population of all the cities.')
    result = cur.fetchone()
    print(f'{result[0]:,.0f}')

def disp_high_pop(cur):
    cur.execute('''SELECT CityName, MAX(Population)
                    FROM Cities''')
    
    print('City with the highest population.')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:10}{row[1]:,.0f}')

def disp_low_pop(cur):
    cur.execute('''SELECT CityName, MIN(Population)
                    FROM Cities''')
    
    print('City with the lowest population.')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:10}{row[1]:,.0f}')

if __name__ == '__main__':
    main()