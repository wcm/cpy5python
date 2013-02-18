#Filename: q04_sum_series.py
#Author: Wu Chenmu
def m_series(i):
    s = 0
    for a in range (1, i + 1):
        s = s + a / (a + 1)
    return s
#main
print("i         m(i)")
for j in range(1, 21):
    print("%-10d%-.4f"%(j, m_series(j)))
