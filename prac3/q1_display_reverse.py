#Filename: q1_display_reverse.py
#Author: Wu Chenmu
def reverse_int(n):
    a = 0
    while n != 0:
        a = a * 10 + n % 10
        n = n // 10
    return a
#main
num = int(input("Enter an integer: "))
print(reverse_int(num))

