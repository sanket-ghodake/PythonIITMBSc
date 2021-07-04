# difference between / and // operator and ** and pow(a,b)
# // is accurate when it comes to large integers - https://www.geeksforgeeks.org/benefits-of-double-division-operator-over-single-division-operator-in-python/ 

x = 10000000000000000000006
print(x//2)
print(x/2)
from math import e # import euler number
from math import exp # exp(x) function e^x

print(str(int(x/2))) # printing x/2 = 5e+21 = 5* (10^21)
if int(x / 2) == x // 2:
    print("Hello")
else:
    print("World")


# // is the floored-division operator in Python. The difference is visible when dividing floating point values.

# In Python2, dividing two ints uses integer division, which ends up getting you the same thing as floored division. However, you can still use // to get a floored result of floating point division

# However, in Python3, dividing two ints results in a float, but using // acts as integer division

# Floored division means round towards negative infinity. This is the same as truncation for positive values, but not for negative. 3.3 rounds down to 3, but -3.3 rounds down to -4.
# reference https://stackoverflow.com/questions/37082597/difference-between-and-in-python-2 
print(-10//3) 


"""
1. The ** operator returns an int while the math.pow function returns a float.
2. ** operator is generally faster than the math.pow function.
"""
import math
print(2 ** 5)
print(math.pow(2, 5))