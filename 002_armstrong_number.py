n = float(input("number : "))
b = int(n)
a = str(b)
arm_num = 0
if 0 < n and n == b :
    for i in a:
        arm_num += int(i)**(len(a))
    if arm_num == b :
        print(b ,"is an Armstrong number")
    elif arm_num != b :
        print(b ,"is not an Armstrong number")
else:
    print("It is an invalid entry.Don't use non-numeric,float or negative values!")
    
