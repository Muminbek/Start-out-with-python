#charge account validation

def main():
    with open('charge_accounts.txt', 'r') as account_file:
        file_numbers = list(map(int, account_file.read().splitlines()))
    
    user_number = get_user_number()
    print()
    CheckFile(file_numbers, user_number)
    
    
def get_user_number():
    print("Please enter the charge account number", end="")
    get_user = int(input(": "))
    return get_user

def CheckFile(a, b):
    if b in a:
        print("The number",b,"is valid. It is in the file.")
    else:
        print("***ERROR***:The number", b,"is NOT valid. It is not found in the file.")
main()
    