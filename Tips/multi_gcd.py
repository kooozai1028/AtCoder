from functools import reduce

list = [4,6,8,10]

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

print(reduce(gcd,list))
