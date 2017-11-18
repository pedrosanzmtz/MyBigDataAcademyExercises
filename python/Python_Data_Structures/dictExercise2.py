from __future__ import print_function
from collections import Counter
from pprint import pprint

if __name__ == '__main__':
	'''
	
	Write a program which count and print the numbers of each character in
	a string input by console.

	Example: If the following string is given as input to the program:
	
	'abcdefgabc'

	Then, the output of the program should be:
	
	a,2
	c,2
	b,2
	e,1
	d,1
	g,1
	f,1

	'''

	string = 'abcdefgabc'

	counts1 = dict()

	for i in string:
		if i in counts1:
			counts1[i] += 1
		else:
			counts1[i] = 1
	print('Solution1')
	pprint(counts1, width=1)

	print('Solution2')
	counts2 = dict(Counter(string))
	pprint(counts2, width=1)