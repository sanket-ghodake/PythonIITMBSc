## [In C language (click to link)](http://www.crasseux.com/books/ctutorial/argc-and-argv.html)

The name of the variable argc stands for "argument count"; argc contains the number of arguments passed to the program. The name of the variable argv stands for "argument vector". A vector is a one-dimensional array, and argv is a one-dimensional array of strings. Each string is one of the arguments that was passed to the program.

For example, the command line

gcc -o myprog myprog.c

would result in the following values internal to GCC:


argc

4

argv[0]

gcc

argv[1]

-o

argv[2]

myprog

argv[3]

myprog.c

## sys.argv in python

For every invocation of Python, sys.argv is automatically a list of strings representing the arguments (as separated by spaces) on the command-line. The name comes from the C programming convention in which argv and argc represent the command line arguments.

	import sys
	print(sys.argv, len(sys.argv))

	> python print_args.py
	['print_args.py'] 1

	> python print_args.py foo and bar
	['print_args.py', 'foo', 'and', 'bar'] 4

	> python print_args.py "foo and bar"
	['print_args.py', 'foo and bar'] 2

	> python print_args.py "foo and bar" and baz
	['print_args.py', 'foo and bar', 'and', 'baz'] 4

As you can see, the command-line arguments include the script name but not the interpreter name. In this sense, Python treats the script as the executable. If you need to know the name of the executable (python in this case), you can use sys.executable.

You can see from the examples that it is possible to receive arguments that do contain spaces if the user invoked the script with arguments encapsulated in quotes, so what you get is the list of arguments as supplied by the user.