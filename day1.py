#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Aaliyah
def main():
	
		pass
		who ='Aaliyah的老妈'
		good_price =6#修改白菜售价为5元，妈妈会买2斤，不会扬长而去
		good_description="西双版纳大白菜"
		is_cheap=False
		resonable_price=5#修改妈妈认为合理价格为6元，妈妈会买2斤
		buy_amount=2
		while buy_amount<4:
			print '%s上街看到了%s,卖%d元/斤'%(who,good_description,good_price)
			if good_price<=resonable_price:
				print '她认为便宜'
				is_cheap=True
				good_price=good_price-1
				buy_amount=buy_amount+1
				print '她买了%d斤'%(buy_amount)
			else:
				print '她认为贵了'
				good_price=good_price-1
				is_cheap=False
				buy_amount=buy_amount+1
				#print '她并没有买，扬长而去'
if __name__ == '__main__':
	main()
#number是python的数字数据类型，包括int型，浮点型，长整型，string是字符串类型，boolean是布尔类型。
#if就是“如果”“假如”表示判断的语句
#我们需要<>=来做运算中的比较
#计算器：用一个数组存放用户需要计算的数字，然后用switch语句来选择运算
