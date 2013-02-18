#Filename: q6_determine_prime.py
#Author: Wu Chenmu
def is_prime(n):
    for i in range (2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
#main
import math
num = 2
for i in range(1, 101):
    for j in range(1, 11):
        while is_prime(num) == False:
            num += 1
        print("%5d"%num, end = "")
        num += 1
    print()
