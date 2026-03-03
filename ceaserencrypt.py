#The source code of ceaser encryption algorithm
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

cleartext = input("Enter your message: ")
key = int(input("Enter the key: "))
print(encrypt(cleartext,key))