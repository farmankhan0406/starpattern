#pattern printing
#input=integer n
#Boolean =true or false
#true n=5
# *
# **
# ***
# ****
# *****
# #false
# *****
# ****
# ***
# **
# *
i=0
n = int(input("Enter a num you want to print star lines: "))
pattern = bool(int(input("Enter 0 or 1 to print pattern: ")))
if pattern == True:
    for i in range(0, n+1, 1):
        print("*" * i)
else:
    for i in range(n, 0, -1):
        print("*" * i)
i=0
#
#
#
# print("*"*i)