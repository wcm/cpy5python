#Filename: q02_display_pattern.py
#Author: Wu Chenmu
def display_pattern(n):
    for i in range (1, n+1):
        for j in range (n, 0, -1):
            if j <= i:
                print("{0:3.0f}".format(j),end = "")
            else:
                print("  ", end = " ")
        print()
#main
num = int(input("Enter n: "))
display_pattern(num)
