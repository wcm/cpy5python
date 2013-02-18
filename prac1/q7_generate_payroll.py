# Filename: q7_generate_payroll.py
# Author: Wu Chenmu

n = input("Emter name: ")
h = float(input("Enter number of hours worked weekly: "))
r = float(input("Enter hourly pay rate: "))
cpf = float(input("Enter CPF contribution rate(%): "))
gp = r * h
c = gp * cpf / 100
np = gp - c
print("Payroll statement for ", n)
print("Number of hours worked in week: {:.0f}".format(h))
print("Hourly pay rate: $", r)
print("Gross pay = $", gp)
print("CPF contribution at {:.0f}".format(cpf), "% = ${:.2f}".format(c),"\n")
print("Net pay = ${:.2f}".format(np))
