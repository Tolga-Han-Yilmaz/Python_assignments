"""
Finding Fibonacci numbers from 1 to 55
"""

f_list = []
a = 1
b = 0
c = 0

while c<55:
    c = a + b
    a = b
    b = c
    f_list.append(b)
print("fibonacci ->",f_list)
