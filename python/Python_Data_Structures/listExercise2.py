from __future__ import print_function

if __name__ == '__main__':
	'''

	Exercise 2

	zoo_animals = [
		'elephant', 'zebra', 'tiger', 'lion'
	]

	- Add the 5th element to the list: "cheetah". Display the number of list
	items and print the new list.

	- Write an assignment statement that will replace the item that currently
	holds the value "lion" in the zoo_animals list with another animal.

	- From the list remove "zebra"
	
	'''

	zoo_animals = [
		'elephant', 'zebra', 'tiger', 'lion'
	]

	# 1
	zoo_animals.append('cheetah')
	print('size:', len(zoo_animals), 'list:', zoo_animals)

	# 2
	zoo_animals[zoo_animals.index('lion')] = 'cat'
	print(zoo_animals)	

	# 3
	zoo_animals.remove('zebra')
	print(zoo_animals)