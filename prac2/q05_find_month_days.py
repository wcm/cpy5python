#Filename: q05_find_month_days.py
#Author: Wu Chenmu
m = int(input("Enter month: "))
y = int(input("Enter year: "))
month = ["January","Feburary","March","April","May","June","July","August","September","October","November","December"]
if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) and m == 2:
    print("February",y,"has 29 days")
else:
    if m == 2:
        print("February",y,"has 28 days")
    elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        print(month[m - 1],y,"has 31 days")
    elif m == 4 or m == 6 or m == 9 or m == 11:
        print(month[m - 1],y,"has 30 days")
    else:
        print("Invalid input!")
