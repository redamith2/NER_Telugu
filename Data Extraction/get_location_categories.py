import wikipedia as wk
wk.set_lang('te')
location_names = open('location_names.txt','rU')

location_cat = []

i = 0

for word in location_names:
	i+=1
	try:
		page = wk.page(word)
		#print page.summary
		location_cat.extend(page.categories)
	except:
		print "could not find ", word	
	if i==5:
		break
		
location_cat = list(set(location_cat))
#print person_cat

loc_cats = open('location_categories.txt', 'w')
text = ''	
for x in location_cat:
	text +=  x.encode('utf-8')  + '\n'
	#name_cats.write(x)

loc_cats.write(text)
loc_cats.close()

