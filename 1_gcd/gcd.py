# find greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a, b):
    while(b != 0):
        t = a
        a = b
        b = t % b
    return a


# tests
print(gcd(60, 20)) # has to return 20
print(gcd(60, 21)) # has to return 3
