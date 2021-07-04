1. ### module

	An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

1. The Python style (unlike Perl) is to halt if it can't tell what to do, rather than just make up a default value.

1. Python newbie gotcha: don't use "len" as a variable name to avoid blocking out the len() function.

1. we can’t create a raw string of single backslash. Also, a raw string can’t have an odd number of backslashes at the end.

1. by default Python treats each line as a separate statement (on the plus side, this is why we don't need to type semi-colons on each line).

1. command-line arguments include the script name but not the interpreter name. In this sense, Python treats the script as the executable. If you need to know the name of the executable (python in this case), you can use sys.executable

1. It's fairly common to def main(*args) and have if ______name____ == '____main__': simply call main(*sys.argv[1:]) if you want to define main in a manner that's similar to some other programming languages.

