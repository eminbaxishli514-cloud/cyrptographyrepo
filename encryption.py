#encryption 35-99
from random import randint
code=""
end=""
letter="abcdefjghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
countt=0
for i in letter:
    number=randint(35,99)
    code+=str(ord(i)+number)
    end+=str(number)
key = code+"898989"+end
print(key)