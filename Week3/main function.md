

In Python, execution does NOT have to begin at main. The first line of "executable code" is executed first. 
 
 The Python approach to "main" is almost unique to the language(*).

The semantics are a bit subtle. The ______name____ identifier is bound to the name of any module as it's being imported. However, when a file is being executed then  ______name____ is set to "____main__" (the literal string: ____main__).

This is almost always used to separate the portion of code which should be executed from the portions of code which define functionality. 
 
 It's fairly common to def main(*args) and have if ______name____ == '____main__': simply call main(*sys.argv[1:]) if you want to define main in a manner that's similar to some other programming languages.

 It's important to understand that all of the code above the if ______name____line is being executed, evaluated, in both cases. It's evaluated by the interpreter when the file is imported or when it's executed. If you put a print statement before the if ______name____ line then it will print output every time any other code attempts to import that as a module.

 Summary: if __name__ == '__main__': has two primary use cases:

1. when a module is imported for the first time, the main block in that module is run. What if we want to run the block only if the program was used by itself and not when it was imported from another module? This can be achieved using the name attribute of the module. 

	Allow a module to provide functionality for import into other code while also providing useful semantics as a standalone script (a command line wrapper around the functionality)

1. Allow a module to define a suite of unit tests which are stored with (in the same file as) the code to be tested and which can be executed independently of the rest of the codebase.

[Reference](https://stackoverflow.com/questions/22492162/understanding-the-main-method-of-python)

