#!/usr/bin/python
# -*- coding: utf-8 -*-
def __main__():
	
	book = {
			"abandon": 'to give up to the control or influence of another person or agent',
          	"abase": "to lower in rank, office, prestige, or esteem",
          	"abash" : "to destroy the self-possession or self-confidence of"
		}

	who = '老妈'
	if not book.has_key('etiquette'):

		print '%s愤怒了，把含有abandon一页单词撕掉了'%(who)
		del book['abandon']
	if book.has_key('abase'):
		print '%s查到了abase:'%(who),book['abase']
		print '%s很开心又把abandon加入字典'%(who)
		book['abandon'] = "to give up to the control or influence of another person or agent"
		if book.has_key('abash'):
			print '%s查到了abash %s'%(who,book['abash'])
		else:
			print '%s没有查到abash'%(who)
if __name__ == '__main__':
	__main__()
