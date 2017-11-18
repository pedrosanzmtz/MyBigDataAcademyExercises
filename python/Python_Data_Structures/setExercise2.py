from __future__ import print_function

if __name__ == '__main__':
	'''

	Delete the 'Sloth' and 'Bengal Tiger items from zoo_animals using
	del.


	Set the value associated with 'Rockhopper Penguin' to anything other
	than 'Arctic Exhibit'.

	'''

	zoo_animals = {
		'Unicorn': 'Cotton Candy House',
		'Sloth': 'Rainforest Exhibit',
		'Bengal Tiger': 'Jungle House',
		'Atlantic Puffin': 'Arctic Exhibit',
		'Rockhopper Penguin': 'Arctic Exhibit'
	}

	# 1

	del zoo_animals['Sloth']
	del zoo_animals['Bengal Tiger']

	print(zoo_animals)

	# 2
	zoo_animals['Rockhopper Penguin'] = 'Cotton Candy House'
	print(zoo_animals)