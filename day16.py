#!/usr/bin/python
# -*- coding: utf-8 -*-
import turtle

def main():
	windows = turtle.Screen()

	windows .bgcolor('blue')

	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')

	bran.speed(1)

	for i in xrange(1,100):
		bran.forward(100)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(100)
		bran.right(90)   
  #停下来

if __name__ == '__main__':
	main()