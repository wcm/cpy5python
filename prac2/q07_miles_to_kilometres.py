#Filename: q07_miles_to_kilometres.py
#Author: Wu Chenmu
print("{0:<6s}{1:<11s}{2:<11s}{3:<6s}".format("Miles","Kilometres","Kilometres","Miles"))
for i in range(1,11):
    print("{0:<6.0f}{1:<11.3f}{2:<11.0f}{3:<6.3f}".format(i,i * 1.609,15 + 5*i,(15 + 5*i)/1.609))
