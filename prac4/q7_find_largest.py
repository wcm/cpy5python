#Filename: q7_find_largest.py
#Author: Wu Chenmu
def find_largest(alist):
    if len(alist)  == 0:
        return 0
    else:
        return max(alist[0], find_largest(alist[1:]))
#main
list = [5, 1, 8, 7, 2]
print(find_largest(list))
