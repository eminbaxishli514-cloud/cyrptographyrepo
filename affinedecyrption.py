#The source code of affine decryption
def finder(a,b):
    for i in range(len(a)):
        if a[i] == b:
            return i

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

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