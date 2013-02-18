#Filename: q04_determine_leap_year.py
#Author: Wu Chenmu
n = int(input("Enter year: "))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print("Leap")
else:
    print("Non-leap")
