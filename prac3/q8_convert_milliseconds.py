#Filename: q8_convert_milliseconds.py
#Author: Wu Chenmu
def convert_ms(n):
    h = n // 3600000
    m = n % 3600000 //60000
    s = n % 60000 // 1000
    return str(h)+':'+str(m)+':'+str(s)
#main
t = int(input("Enter the number of milliseconds:"))
print(convert_ms(t))
