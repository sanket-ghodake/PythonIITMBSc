# Operators
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

	Operator	Description	  Associativity


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