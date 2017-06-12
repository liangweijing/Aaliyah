#!/usr/bin/python
# -*- coding: UTF-8 -*-
def main():
	print '老妈来到菜市场'
	pass
	foods = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	
	for index,foods_item in enumerate(foods):
		if index%2==0:
			print '老妈看到%s,买了%d斤' %(foods_item,index+1)
			print 
		else:
			print '老妈看到%s,不买'%(foods_item)
			print'老妈继续逛'
	return foods
	
def add(foods2):
	foods2.extend(['黄瓜','油麦菜','羊肉'])
	for food in foods2:
		print food
def cut(foods3):
	foods4=foods3[4:9]
	for index,foods_item in enumerate(foods4):
		if index%2==0:
			print '老妈看到%s,买了%d斤' %(foods_item,index+1)
			print '老妈继续逛'
		else:
			print '老妈看到%s,不买'%(foods_item)
			print'老妈继续逛'
			
if __name__ == '__main__':
			foods1=main()
			add(foods1)
			cut(foods1)
