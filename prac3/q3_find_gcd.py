#Filename: q03_find_gcd.py
#Author: Wu Chenmu
def gcd(m, n):
    d = min(m, n)
    while m % d != 0 or n % d != 0:
        d -= 1
    return d
print(gcd(24,16), gcd(255, 25))
