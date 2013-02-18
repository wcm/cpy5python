# Filename: q4_sum_digits.py
# Author: Wu Chenmu

n = int(input("Enter an integer: "))
s = 0
while(n>0):
    s = s + n % 10
    n=n//10
print("The sum of its digits: ",s)
