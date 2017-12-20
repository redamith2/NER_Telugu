import pandas as pd
import numpy as np
df = pd.read_csv('NER_data.txt', sep = '\s+',header=None)

names = open("person_names.txt", "w")

num_lines = 56541
x=''
name_list = []

for i in range(0, num_lines):
	if df[1][i] == 'B-PERSON':
		x+= df[0][i]
		while(df[1][i+1]=='I-PERSON'):
			i+=1
			x+=' ' + df[0][i]
		#x+='\n'
		name_list.append(x)
		x = ''

#print x
#names.write(x)
name_list = list(set(name_list))
#print name_list
x=''
for n in name_list:
	x+=n + '\n'
	
names.write(x)
names.close()
			
