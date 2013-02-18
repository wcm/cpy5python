#Filename: q6_compute_sum.py
#Author: Wu Chenmu
def sum_digits(n):
    if n // 10 == 0:
        return n
    else:
        return n%10 + sum_digits(n//10)
#main
print(sum_digits(234))
