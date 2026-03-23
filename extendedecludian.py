def extended_gcd(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    
    while b != 0:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    
    return a, x0, y0

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(extended_gcd(a,b))