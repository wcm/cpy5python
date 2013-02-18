#Filename: q7_display_matrix.py
#Author: Wu Chenmu
import random
def print_matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print (random.randint(0,1), end = " ")
        print()
#main
num = int(input("Enter an integer: "))
print_matrix(num)
