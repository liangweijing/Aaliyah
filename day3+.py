#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Aaliyah

# 
def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def buybuybuy():
  good_price = 5 #每降低一元，多买一斤
  reasonable_price = 5
  buy_amount = 2 #每降低一元，多买一斤
  
  who = 'xiao的老妈'
  good_description = "西双版纳大白菜"

  is_cheap = False

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

  return is_cheap, buy_amount,good_price

def record_account(buy_amount4,good_price2):
  pass
  total_cost=buy_amount4*good_price2
  print '老妈在小本子记了买菜花销%d元'%(total_cost)

def main():
  is_cheap2, buy_amount2 ,good_price3 = buybuybuy()
  
  talk_with_daddy(is_cheap2, buy_amount2)  
  #记记记
  record_account(buy_amount2,good_price3)

if __name__ == '__main__':
  main()

  #单一职责原则就是不同的代码块有自己的职责，一个代码块只负责一个功能。