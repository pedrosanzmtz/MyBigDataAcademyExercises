from __future__ import print_function

if __name__ == '__main__':
	'''

	With two given lists [1, 3, 6, 24, 78, 35, 55] and [12, 24, 35, 24, 88,120,
	155], write a program to make a list with only the elements that are in
	both lists.

	'''

	list1 = [1, 3, 6, 24, 78, 35, 55]
	list2 = [12, 24, 35, 24, 88, 120, 155]

	in_both = list(set(list1).intersection(list2))
	in_both2 = list(set(list1) & set(list2))
	print('Solution 1:', in_both)
	print('Solution 2:', in_both2)