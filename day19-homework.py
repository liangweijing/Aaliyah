#!/usr/bin/python
# -*- coding: utf-8 -*

class Dog():
	"""docstring for Dog"""
	def __init__(self, name):
		#super(Dog, self).__init__()
		self.name= name
	def bark(self):
		print '%s总是汪汪叫' % (self.name)
def main():
	Snopy = Dog("snopy")
	Snopy.bark()


if __name__ == '__main__':
	main()
	

			