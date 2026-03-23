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