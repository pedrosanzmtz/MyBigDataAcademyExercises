from __future__ import division

class Calculator:
	def __init__(self, value2=15):
		self.value2 = value2
	def add(self, value1):
		return value1 + self.value2

	def sub(self, value1):
		return value1 - self.value2

	def mul(self, value1):
		return value1 * self.value2

	def div(self, value1):
		return value1 / self.value2