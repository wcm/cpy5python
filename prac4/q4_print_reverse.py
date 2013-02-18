#Filename: q4_print_reverse.py
#Author: Wu Chenmu
def reverse_int(n):
    if n//10 == 0:
        return n
    else:
        return (n%10)*10**(len(str(n))-1)+ reverse_int(n//10)
#main
num = int(input("Enter an integer: "))
print(reverse_int(num))
