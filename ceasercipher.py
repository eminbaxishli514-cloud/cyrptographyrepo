#Encryption
def finder(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return i

def encrypt(text,key):
    result = ""
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in text:
        if i in text:
            number = finder(letters,i)
            result = result + letters[(number+key)%26]
        else:
            result = result + i
    return result

#Decryption

def decyrpt(ciphertext,key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in ciphertext:
        if i in letters:
            number = finder(letters,i)
            result = result + letters[(number-key)%26]
        else:
            result = result + i
    return result

#Decryption
#ciphertext = input("Enter the ciphertext: ")
#key = int(input("Enter the key: "))
#print(decyrpt(ciphertext,key))

#Encryption
#cleartext = input("Enter your message: ")
#key = int(input("Enter the key: "))
#print(encrypt(cleartext,key))

