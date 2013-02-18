#Filename: q02_triangle.py
#Author: Wu Chenmu
a1 = float(input("Enter side 1: "))
a2 = float(input("Enter side 2: "))
a3 = float(input("Enter side 3: "))
if a1 + a2 <= a3 or a1 + a3 <= a2 or a2 + a3 == a1:
    print("Invalid triangle!")
else:
    print("Perimeter = {0:.0f}".format(a1 + a2 + a3))
