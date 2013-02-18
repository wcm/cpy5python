#Filename: q2_sum_series2.py
#Author: Wu Chenmu
def sum_series2(i):
    if i == 1:
        return 1/3
    else:
        return i/(2*i+1) + sum_series2(i-1)
#main
n = int(input("Enter an integer: "))
print(sum_series2(n))
