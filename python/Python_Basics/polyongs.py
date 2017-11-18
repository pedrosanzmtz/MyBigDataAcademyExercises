from __future__ import division, print_function
from math import tan

def print_features(area, perimeter):
	print('perimeter:', perimeter)
	print('area:', area)

def triangle():
	base = float(raw_input('Base: '))
	height = float(raw_input('Height: '))
	perimeter = base * 3 
	area = (base * height) / 2
	print_features(area, perimeter)

def square():
	side = float(raw_input('Side: '))
	perimeter = lado * 4
	area = side * side
	print_features(area, perimeter)

def rectangle():
	base = float(raw_input('Base: '))
	height = float(raw_input('Height: '))
	perimeter = (base + height) * 2
	area = base * height
	print_features(area, perimeter)

def nPolygon(N):
	side = float(raw_input('Side: '))
	a = 360 / N
	ap = side / (2 * tan(a / 2))
	area = (N * side * ap) / 2
	perimeter = N * side
	print_features(area, perimeter)

if __name__ == '__main__':
	polygons = ['triangle', 'square', 'rectangle', 'pentagon', 'hexagon', 'heptagon', 'octagon']
	indexes = list(range(len(polygons)))
	for i, f in enumerate(polygons):
		print(i, ':', f)
	polygon = int(raw_input('index of polygon: '))
	if polygon in indexes:
		if polygon == 0:
			triangle()
		elif polygon == 1:
			square()
		elif polygon == 2:
			rectangle()
		elif polygon == 3:
			nPolygon(5)
		elif polygon == 4:
			nPolygon(6)
		elif polygon == 5:
			nPolygon(7)
		elif polygon == 6:
			nPolygon(8)
	else:
		print('Polygon unknown')