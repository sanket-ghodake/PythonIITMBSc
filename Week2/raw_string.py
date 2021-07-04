'''
Python raw string is created by prefixing a string literal with ‘r’ or ‘R’. Python raw string treats backslash (\) as a literal character. This is useful when we want to have a string that contains backslash and don’t want it to be treated as an escape character
'''
'''
When a backslash is followed by a quote in a raw string, it’s escaped. However, the backslash also remains in the result. Because of this feature, we can’t create a raw string of single backslash. Also, a raw string can’t have an odd number of backslashes at the end.

r'\'  # missing end quote because the end quote is being escaped
r'ab\\\'  # first two backslashes will escape each other, the third one will try to escape the end quote.
'''
raw_s = r'\''
print(raw_s)

raw_s = r'ab\\'
print(raw_s)

raw_s = R'\\\"'  # prefix can be 'R' or 'r'
print(raw_s)