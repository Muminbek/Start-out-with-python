#Thе Кilometer Coпverter


def main():
    km = float(input("enter kilometers to convert in km: "))
    convert(km)
    
def convert(km):
    print(km, 'kilometers will be', format(km * 0.6214, '.2f'), 'km')
    
main()