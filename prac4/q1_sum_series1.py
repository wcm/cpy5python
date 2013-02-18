#Filename: q1_sum_series1.py
#Author: Wu Chenmu
def sum_series1(i):
    if i == 1:
        return 1
    else:
        return 1/i + sum_series1(i-1)
#main
n = int(input("Enter an integer: "))
print(sum_series1(n))
