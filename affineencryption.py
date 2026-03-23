#Encryption
def finder(a, b):
    for i in range(len(a)):
        if a[i] == b:
            return i

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(plaintext, multiplier, shifter):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    if gcd(multiplier, 26) == 1:
        for char in plaintext.lower():
            if char in letters:
                x = finder(letters, char)
                y = (multiplier * x + shifter) % 26
                result = result + letters[y]
            else:
                result = result + char
    else:
        return "For the inverse to exist, the number must be coprime to 26."
    return result


#Decryption

def inverse(a,m = 26):
    for i in range(1,m):
        if (i*a)%m ==1:
            return i
    return None

def decrypt(ciphertext,multiplier,shifter,inverse_of_multiplier):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    if gcd(multiplier,26) == 1:
        for i in ciphertext:
            if i in letters:
                y = finder(letters,i)
                x = (inverse_of_multiplier*(y-shifter))%26
                result = result + letters[x]
            
            else:
                result = result + i
    
    return result

#Usage
plaintext = "hello world"
multiplier = 5
shifter = 8

#Encryption
ciphertext = encrypt(plaintext, multiplier, shifter)
print("Encrypted text:", ciphertext)
#Inverse
inv = inverse(multiplier)

#Decryption
decrypted = decrypt(ciphertext, multiplier, shifter, inv)
print("Decrypted text:", decrypted)
