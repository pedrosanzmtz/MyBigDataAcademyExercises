from __future__ import print_function

if __name__ == '__main__':
	'''
	Exercise 1

	Use list slicing to print out every odd element of my_list from start to
	finish. Omit the start and end index.
	my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

	# Output 
	[9, 25, 49, 81]
	'''

	my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	output = [i for i in my_list[1:-1] if i % 2 != 0]
	print(output)