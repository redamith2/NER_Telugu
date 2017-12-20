import pandas as pd
import numpy as np
df = pd.read_csv('NER_data.txt', sep = '\s+',header=None)
patterns = open("patterns.txt", "w")
#print df[1][0]

#data = open("NER_data.txt", 'rU')

#for line in data:
#	pos = line.split()
	#print pos[0], "and ", pos[1], "and ", pos[2]

num_lines = 56541
	
entities = []	
pos = []
for i in range(0, num_lines):
	if df[1][i] != 'O':
		if df[1][i] == 'P':
			print i
		entities.append(df[1][i])
		pos.append(df[2][i])
		#print df[0][i], " ", df[1][i], " ", df[2][i]
		temp_pattern = [0,0,0,0,0]
		temp_pattern[2] = df[1][i]
		for index in range(1,3):
			if i - index >= 0:
				temp_pattern[2 - index] = df[2][i - index]
		for index in range(1,3):
			if i + index < num_lines:
				temp_pattern[2 + index] = df[2][i + index]
		x = str(temp_pattern[0]) + ' ' + str(temp_pattern[1]) + ' ' + str(temp_pattern[2]) + ' ' + str(temp_pattern[3]) + ' ' + str(temp_pattern[4]) + '\n'
		patterns.write(x)

patterns.close() 
		
entities = list(set(entities))
print "Entity list in the corpus ", entities
pos = list(set(pos))
print "Parts of speech ", pos
