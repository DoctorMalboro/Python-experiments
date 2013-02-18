import os, sys, urllib2, re, jsonlib


class KPopFinder(object):
	def __repr__(self):
		return '>tfw no average korean gf ;_;'

	def search(self):
		self.url = urllib2.urlopen('http://api.4chan.org/mu/catalog.json')\
		.read()
		self.data = jsonlib.read(self.url)

		pattern = '(.*)KPOP(.*)'
		compiled = re.compile(pattern)

		for threads in self.data:
			for thread in threads['threads']:
				if 'sub' in thread:
					if 'KPOP General' in thread['sub'] or 'KPOP general' in thread['sub']:
						print thread['sub']
						if 'com' in thread:
							print thread['com']
						print 'https://boards.4chan.org/mu/res/%d' % thread['no']

if __name__ == '__main__':
	find = KPopFinder()
	find.search()
