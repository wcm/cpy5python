# Filename: q2_calc_cylinder_volume.py
# Author: Wu Chenmu
import math
r = float(input("Enter the radius of the cylinder in cm: "))
l = float(input("Enter the length of the cylinder in cm: "))
v = r*r*math.pi*l
print("The volume of the cylinder: {0:.1f}".format(v),"cm^3")

