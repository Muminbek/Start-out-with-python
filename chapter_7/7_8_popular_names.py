
def main():
    with open('GirlNames.txt','r') as girls_names:
        girl_list = girls_names.read().splitlines()
    with open('BoyNames.txt','r') as boys_names:
        boy_list = boys_names.read().splitlines()
    
    
    user_boy=input("Enter a boy's name (first letter capital): ")
    user_girl=input("Enter a girl's name (first letter capital): ")
    print()
    check_names(girl_list, boy_list, user_boy, user_girl)


def check_names(girls, boys, user_boy, user_girl):
    if user_boy in boys:
        print("The boy name <<", user_boy, ">> is in the list.", sep="")
    else:
        print("The boy name <<", user_boy, ">> is NOT in the list.", sep="")
        
    if user_girl in girls:
        print("The girl name <<", user_girl, ">> is in the list.", sep="")
    else:
        print("The girl name <<", user_girl, ">> is NOT in the list.", sep="")

main()       
