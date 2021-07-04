# Operators

1. UNARY OPERATORS
The unary operators operate on a single operand. The addition, subtraction and multiplication operators are used as unary operator in python.

2. BINARY OPERATORS
A binary operator is an operator that operates on two operands.

	Arithmetic Operators
	Assignment Operators
	Relational Operators
	Logical Operators
	Membership operators
	Identity operators
	Bitwise operators

3. TERNARY OPERATORS
The ternary operator is an operator that operates on three operands. The first argument is an expression, If expression is true then second argument will execute else third argument will execute.

##
1. Arithmetic

		+ - * / // % **

2. Relational 
	
	Either return True or False
		> < == != >= <= >= 

3. Logical 
		
		and, or, not

4. Bitwise 

		& | ~ ^ >> <<

5. Assignment 

		= += -= *= /= %= //= &= |= ^= >>= <<=

6. Special operators

	identity operator
	
		is, is not

	membership operator

		in, not in

7. Precedence and Associativity 

	Operator Precedence: This is used in an expression with more than one operator with different precedence to determine which operation to perform first.

	Operator Associativity: If an expression contains two or more operators with the same precedence then Operator Associativity is used to determine. It can either be Left to Right or from Right to Left

	**Non associative operators**

	Some operators like assignment operators and comparison operators do not have associativity in Python. There are separate rules for sequences of this kind of operator and cannot be expressed as associativity.

	For example, x < y < z neither means (x < y) < z nor x < (y < z). x < y < z is equivalent to x < y and y < z, and is evaluated from left-to-right.

	Furthermore, while chaining of assignments like x = y = z = 1 is perfectly valid, x = y = z+= 2 will result in error.

The following table summarizes the operator precedence in Python, from highest precedence (most binding) to lowest precedence (least binding). Operators in the same box have the same precedence. Unless the syntax is explicitly given, operators are binary. Operators in the same box group left to right (except for exponentiation(**), assignment(=) which groups from right to left).


| Operator                                                              	| Description                                                                        	|
|-----------------------------------------------------------------------	|------------------------------------------------------------------------------------	|
| (expressions...), [expressions...], {key: value...}, {expressions...} 	| Binding or parenthesized expression, list display, dictionary display, set display 	|
| x[index], x[index:index], x(arguments...), x.attribute                	| Subscription, slicing, call, attribute reference                                   	|
| await x                                                               	| Await expression                                                                   	|
| **                                                                    	| Exponentiation 5                                                                   	|
| +x, -x, ~x                                                            	| Positive, negative, bitwise NOT                                                    	|
| *, @, /, //, %                                                        	| Multiplication, matrix multiplication, division, floor division, remainder 6       	|
| +, -                                                                  	| Addition and subtraction                                                           	|
| <<, >>                                                                	| Shifts                                                                             	|
| &                                                                     	| Bitwise AND                                                                        	|
| ^                                                                     	| Bitwise XOR                                                                        	|
| \|                                                                    	| Bitwise OR                                                                         	|
| in, not in, is, is not, <, <=, >, >=, !=, ==                          	| Comparisons, including membership tests and identity tests                         	|
| not x                                                                 	| Boolean NOT                                                                        	|
| and                                                                   	| Boolean AND                                                                        	|
| or                                                                    	| Boolean OR                                                                         	|
| if – else                                                             	| Conditional expression                                                             	|
| lambda                                                                	| Lambda expression                                                                  	|
| :=                                                                    	| Assignment expression                                                              	|
[Reference](https://docs.python.org/3/reference/expressions.html#operator-precedence)