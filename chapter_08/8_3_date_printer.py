# date printer
def main():
    date = input("Enter the date as dd/mm/yyyy: ")

    print("The date is below.")

    literal_date = convert(date)
    
    print(literal_date)

def convert(date):
    date_list = date.split('/')
    
    months=["January", "February", "March", "April", "May", \
            "June", "July", "August", "September", "October", \
            "November", "December"]
    new_date = f'{date_list[0]} {months[int(date_list[1])-1]} {date_list[2]}'
    return new_date
    
main()
