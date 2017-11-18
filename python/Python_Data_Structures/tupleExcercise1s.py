from __future__ import print_function

if __name__ == '__main__':
	'''
	Write a program to generate and print another tuple whose values are
	even numbers in the given tuple:
	(1, 2, 3, 4, 5, 6, 7, 8, 9, 10).
	Output:
	(2, 4, 6, 8, 10)
	'''

	my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

	output = tuple([i for i in my_tuple if i % 2 == 0])
	print(output)