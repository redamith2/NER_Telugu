import wikipedia as wk
wk.set_lang('te')
person_names = open('person_names.txt','rU')

person_cat = []

i = 0

for word in person_names:
	i+=1
	try:
		page = wk.page(word)
		#print page.summary
		person_cat.extend(page.categories)
	except:
		print "could not find ", word	
	if i==5:
		break
		
person_cat = list(set(person_cat))
#print person_cat

name_cats = open('names_categories.txt', 'w')
text = ''	
for x in person_cat:
	text +=  x.encode('utf-8')  + '\n'
	#name_cats.write(x)

name_cats.write(text)
name_cats.close()

