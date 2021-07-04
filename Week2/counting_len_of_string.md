There is no end-of-string character in Python, at least not one that is exposed and it would be implementation dependent. String objects maintain their own length and it is not something that you need to be concerned with. There are several ways to get the string's length without using len().

	str = 'man bites dog'
	unistr = u'abcd\u3030\u3333'

	# count characters in a loop
	count = 0
	for character in str:
			count += 1
	>>> count
	13

	# works for unicode strings too
	count = 0
	for character in unistr:
			count += 1
	>>> count
	6

	# use `string.count()`
	>>> str.count('') - 1
	13
	>>> unistr.count(u'') - 1
	6

	# weird ways work too
	>>> max(enumerate(str, 1))[0]
	13
	>>> max(enumerate(unistr, 1))[0]
	6
	>>> str.rindex(str[-1]) + 1
	13
	>>> unistr.rindex(unistr[-1]) + 1
	6

	# even weirder ways to do it
	import re
	pattern = re.compile(r'$')
	match = pattern.search(str)
	>>> match.endpos
	13
	match = pattern.search(unistr)
	>>> match.endpos
	6

[Reference](https://stackoverflow.com/questions/24409581/do-python-strings-end-in-a-terminating-null)