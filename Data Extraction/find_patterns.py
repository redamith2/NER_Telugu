import numpy as np
import pandas as pd

patterns = open("patterns.txt", 'rU')
dict_pat = {}
for line in patterns:
	each = line.split()
	if each[2] == 'B-LOC':
		del each[2]
		tup = tuple(each)
		if tup in dict_pat:
			dict_pat[tup] +=1
		else:
			dict_pat[tup] = 1
			
#print dict_pat

for i in sorted(dict_pat, key = dict_pat.get, reverse = True):
	print i, " ", dict_pat[i]
