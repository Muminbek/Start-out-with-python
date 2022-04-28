#calories from fat and carbohydrates

def main():
    fats = float(input('Please enter grams of fats you consumed in a day: '))
    carbohydrates = float(input('Plesae enter the grams of carbohydrates you consumed in a day: '))
    fat_c = fat_calories(fats)
    carb_c = carbohydrate_calories(carbohydrates)
    total_calories(fat_c, carb_c)
    
def fat_calories(fats):
    return fats * 9
    
def carbohydrate_calories(carbohydrates):
    return carbohydrates * 4

def total_calories(fat_c, carb_c):
    print("The calories from fats and carbohydrates are", fat_c + carb_c, "calories.")

main()