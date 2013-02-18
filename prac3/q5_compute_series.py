#Filename: q5_compute_series.py
#Author: Wu Chenmu
def m(n):
    s = 1
    for i in range (1, n+1):
        s = s + (1-i%2*2)* (1/(2*i+1))
    s *= 4
    return s
#main
print("i    m(i)")
for i in range (1, 20, 2):
    print("%-5d%1.11f"%(i, m(i)))
