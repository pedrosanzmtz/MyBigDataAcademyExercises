from __future__ import print_function

if __name__ == '__main__':

	'''
	
	Create a dictionary (in your file) of names and birthdays.


	When you run your program it should show you the available names to
	search for the birthday, ask the user to enter a name, and return the
	birthday of that person back to them.

	'''

	my_dict = {
		'pedro': '12-sept',
		'pamela': '11-oct',
		'gonzalo': '9-sept',
		'strange1': '29-feb',
		'strange2': '31-oct'
	}

	name = raw_input('Give a name: ')

	if name in my_dict.keys():
		print('The birthday of', name, 'is', my_dict[name])
	else:
		print('I dont have the birthday of:', name)