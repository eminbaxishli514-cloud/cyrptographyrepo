#The script to brute force the cipher
cipher_text = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"
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

key_space = []
for i in range(1,26):
    key_space.append(i)

for i in key_space:
    print(f"{decyrpt(cipher_text,i)}\n")


#And we got the cleartext ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood
#Now we can write a simple loop to find the key

for i in key_space:
    if decyrpt(cipher_text,i) == "ifweallunitewewillcausetheriverstostainthegreatwaterswiththeirblood":
        print(i)
#The loop to find the key
