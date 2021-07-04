| Escape Sequence 	| Description                    	| Example                                                                         	|
|-----------------	|--------------------------------	|---------------------------------------------------------------------------------	|
| \        	| Backslash and newline ignored  	| print("""line1 \  line2 \ line3""") Multiline print statement  RESULT line1 line2 line3 Output on single line                  	|
| \\              	| Backslash (\)                  	| print("\\")   RESULT \                                                          	|
| \'              	| Single quote (')               	| print('\'')   RESULT '                                                          	|
| \"              	| Double quote (")               	| print("\"")   RESULT "                                                          	|
| \a              	| ASCII Bell (BEL)               	| print("\a")  NO KNOWLEDGE. Some beep sounds on laptop                           	|
| \b              	| ASCII Backspace (BS)           	| print("Hello\bWorld!")   RESULT HelloWorld!                                     	|
| \f              	| ASCII Formfeed (FF)            	| print("Hello \f World!")  RESULT Hello     (this will print on new page)World!  	|
| \n              	| ASCII Linefeed (LF)            	| print("Hello \n World!")   RESULT Hello   World!                                	|
| \r              	| ASCII Carriage Return (CR)     	| print("Hello \r World!")   RESULT  World!                                       	|
| \t              	| ASCII Horizontal Tab (TAB)     	| print("Hello \t World!")  RESULT  Hello      World!                             	|
| \v              	| ASCII Vertical Tab (VT)        	| print("Hello \v World!")  RESULT  Hello        World!                           	|
| \ooo            	| Character with octal value ooo 	| print("\110\145\154\154\157\40\127\157\162\154\144\41")   RESULT Hello World!   	|
| \xhh            	| Character with hex value hh    	| print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")   RESULT Hello World! 	|

Some escape sequences are only recognized in string literals. These are:

| Escape Sequence 	| Description                                                                              	|
|-----------------	|------------------------------------------------------------------------------------------	|
| \N{name}        	| Character named name in the Unicode database                                             	|
| \uxxxx          	| Character with 16-bit hex value xxxx. Exactly four hexadecimal digits are required.      	|
| \Uxxxxxxxx      	| Character with 32-bit hex value xxxxxxxx. Exactly eight hexadecimal digits are required. 	|

Carriage Return - Make cursor to left side and overrites if the text is written there 
		
	print("Hello\rWorld!")

Output

	World!

Form feed - Jump to new page

	Form feed is a page-breaking ASCII control character. It forces the printer to eject the current page and to continue printing at the top of another. Often, it will also cause a carriage return. The form feed character code is defined as 12 (0xC in hexadecimal) (..) In the C programming language (and other languages derived from C), the form feed character is represented as '\f'.

'\a' - control character BEL (a for alert) - https://en.wikipedia.org/wiki/Bell_character

[Reference](https://www.python-ds.com/python-3-escape-sequences)