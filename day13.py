#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
  lst=['abandon','abase','apple']
  print lst
  book = {
          "abandon": 'to give up to the control or influence of another person or agent',
          "abase": "to lower in rank, office, prestige, or esteem",
          "abash" : "to destroy the self-possession or self-confidence of"
          }
 
  try:
   	look_up(book,lst)
  except Exception,e:
		print '书中没有该单词%s' % (e)
  else:
   	print '查到了该单词 %s' %(item)
  finally:
   	pass
def look_up(book2,lst2):
	for item in lst2:
		if book2.has_key(item):
			print '查到了单词%s' %(item)
		else:
			raise Exception(item)
	
if __name__ == '__main__':
	main()


          		
         

          