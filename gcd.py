########################################################
#Finding the GCD
#In this file, we are going to find the GCD with a lot of methods, the extended gcd can be found in the extendedecludian file in this repo.

#Slow version(Loop)
def gcd(a,b):
    result = 1
    for i in range(1,a+1):
        if a%i ==0 and b%i==0:
            result*=i
    return result

a = 5
b = 10
print(gcd(5,10))



#A bit faster version
def gcd(a,b):
    result = 1
    for i in range(1, min(a, b) + 1):
        if a%i ==0 and b%i==0:
            result*=i
    return result

a = 5
b = 10
print(gcd(5,10))


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = 5
b = 10
print(gcd(a,b))


#GCD(Built-in)
import math
a = 5
b = 10
print(math.gcd(a, b))


def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

a = 5
b = 10
print(gcd(a,b))










