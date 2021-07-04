a = input() # Explicitely converts input to string
print(type(a)) # always <class 'str'>

# raw_input() is renamed as input() in python3
# a = raw_input()
# print(type(b))
"""
You call input function to tell program to stop and wait for user to key in the data. The program will resume once the user presses the ENTER or RETURN key.
"""
"""
input() in python 2.0-
Not modifying type of input

Vulnerability in input()
1. Variable name as input - Direct access the variable value
2. Function name as input - direct access to function return value
"""