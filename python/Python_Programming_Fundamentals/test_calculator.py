from __future__ import print_function
from calculator import Calculator

if __name__ == '__main__':
	c = Calculator()
	options = ['add', 'sub', 'mul', 'div']
	for i, j in enumerate(options):
		print(i, ':', j)
	op = int(raw_input('what opcion do you want?: '))
	value2 = float(raw_input('Value to use in operation: '))
	indexes = list(range(len(options)))
	if op in indexes:
		print(options[op], value2, 'to 15')
		if op == 0:
			print(c.add(value2))
		elif op == 1:
			print(c.sub(value2))
		elif op == 2:
			print(c.mul(value2))
		elif op == 3:
			print(c.div(value2))
	else:
		print('Option invalid')