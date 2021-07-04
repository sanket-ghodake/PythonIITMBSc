1. 
		print(print())

	>None
2. 
		print(int(str(1.23)))

	>Error
3. 
		print(1,2,3,4,5)

	>1 2 3 4 5
4. ***DOUBT***

		print(1 and 10)

	>10
5. 
		a = 1.
		print(type(a))

	> float
1. 
		x, y = 1, 2
		print(x, y)
		x, y = y, x
		print(x, y)

	>swap

1. 
		import math
		print(2 ** 5)
		print(math.pow(2, 5))

	>1. The ** operator returns an int while the math.pow function returns a float.
	>2. ** operator is generally faster than the math.pow function.

1. 
		lines = '''one
		two
		three'''
		print('\n' in lines)
		print(lines.count('\n'))

	>True

	>2

1. ***DOUBT***

		x = y = z+= 2

	>Syntax error

1. 
		a = 10
		print(-a)

	>-10

1. ***DOUBT***

		a, b, c, d = input()

		>>>1234

	>a=1, b=2, c=3, d=4

1.  
		pi = 3.14
		##text = 'The value of pi is ' + pi      ## NO, does not work
		text = 'The value of pi is '  + str(pi)  ## yes

	Unlike Java, the '+' does not automatically convert numbers or other types to string form. The str() function converts values to a string form so they can be combined with other strings.

1. 
		print("\\")
	
	>\

	print single backslash

1. 
		a='Hello'
		print(a[:500])

	>Hello



