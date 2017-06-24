#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象

class Shopping():
	def __init__(self,name,day,hour):
		self.name=name
		self.hour=hour
		self.day=day


	def AverageSpeed(self):
		speed=float (20/self.hour)
		print '%s 骑 %s 平均时速 %0.2f km/h' % (self.day,self.name,speed)

def main():
	shopping1 = Shopping('电动车','周一',0.5)
	shopping1.AverageSpeed()

	shopping2 = Shopping('自行车','周二',2)
	shopping2.AverageSpeed()

	shopping3 =Shopping('电动车','周三',0.6)
	shopping3.AverageSpeed()

if __name__ == '__main__':
	main()

