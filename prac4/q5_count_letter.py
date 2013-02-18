#Filename: q5_count_letter.py
#Author: Wu Chenmu
def count_letter(str, ch):
    if len(str) == 0:
        return 0
    elif str[0:1] == ch:
        return 1 + count_letter(str[1:], ch)
    else:
        return count_letter(str[1:], ch)
#main
print(count_letter("Welcome", "e"))
