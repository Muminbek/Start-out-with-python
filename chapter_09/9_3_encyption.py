# file encryption and decryption

def main():
    # create a dictionary for
    # it is too long copy paste from web
    encrypt={'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
             'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
             'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
             'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
             'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
             't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q', ' ':' ', ',': '/',
             '.': '--'}
            
    print("Welcome to File Encryption and Decryption Program")
    print("1. Encrypt a file.")
    print("2. Decrypt a file.")
    
    choice=int(input("Please enter your choice from above (1 or 2): "))
    print()
    
    if choice==1:
        encryptor(encrypt)
    if choice==2:
        decryptor(encrypt)
    
def encryptor(encrypt):

    text = input('Enter the text for encrypting: ')

    encrypted = open('coded.txt', 'w')
    
    for ch in text:    # this is each character in that element
        if ch in encrypt:
            encrypted.write(encrypt[ch])
        else:
            encrypted.write(ch)
    print("Your file has been encrypted.")     
    print()       
    # close the file.
    encrypted.close()

def decryptor(encrypt):
    textfile = open("coded.txt", "r")
    
    # read the file's contents and close it
    text = textfile.readlines()
    textfile.close()
    
    # open a file to write decrypted text
    decrypted = open("uncoded.txt", "w")

    listofpairs = encrypt.items()

    
    for item in text:
        for ch in item:
            
            for keyvalue in listofpairs:
                if ch == keyvalue[1]:
                    decrypted.write(keyvalue[0])

    print("Your file has been decrypted.")            
    decrypted.close()
main()