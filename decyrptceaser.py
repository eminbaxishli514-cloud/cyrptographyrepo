#The source code of ceaser decryption algorithm
def finder(a,b):
    for i in range(len(a)):
        if a[i] == b:
            return i

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

ciphertext = input("Enter the ciphertext: ")
key = int(input("Enter the key: "))
print(decyrpt(ciphertext,key))

