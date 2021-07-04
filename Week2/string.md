Python strings are "immutable" which means they cannot be changed after they are created

### Difference between index() and find() method

string.index(x) and string.find(x) return the index of the leftmost occurence of the
substring x if it is present in the string. If the substring is not present in the string, then index
throws a ValueError while find returns the value -1 .

## String Methods

1. s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
1. s.strip() -- returns a string with whitespace removed from the start and end
1. s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
1. s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
1. s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
1. s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
1. s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
1. s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc

[More string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## String Slices

The "slice" syntax is a handy way to refer to sub-parts of sequences -- typically strings and lists. The slice s[start:end] is the elements beginning at start and extending up to but not including end. Suppose we have s = "Hello"

s[1:4] is 'ell' -- chars starting at index 1 and extending up to but not including index 4

s[1:] is 'ello' -- omitting either index defaults to the start or end of the string

s[:] is 'Hello' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy a sequence like a string or list)

s[1:100] is 'ello' -- an index that is too big is truncated down to the string length

s[-1] is 'o' -- last char (1st from the end)

s[-4] is 'e' -- 4th from the end

s[:-3] is 'He' -- going up to but not including the last 3 chars.

s[-3:] is 'llo' -- starting with the 3rd char from the end and extending to the end of the string.

It is a neat truism of slices that for any index n, s[:n] + s[n:] == s. This works even for n negative or out of bounds. Or put another way s[:n] and s[n:] always partition the string into two string parts, conserving all the characters. As we'll see in the list section later, slices work with lists too.

## String %

Python has a printf()-like facility to put together a string. The % operator takes a printf-type format string on the left (%d int, %s string, %f/%g floating point), and the matching values in a tuple on the right (a tuple is made of values separated by commas, typically grouped inside parentheses):

	# % operator
	text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')

