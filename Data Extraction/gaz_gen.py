import wikipedia as wk
wk.set_lang('te')
file1 = open('names_categories.txt', 'rU')
file2 = open('location_categories.txt', 'rU')

person_cat = []
location_cat = []

for name in file1:
	person_cat.append(name)
	
for name in file2:
	location_cat.append(name)


for x in person_cat:
	if x in location_cat:
		person_cat.remove(x)
		location_cat.remove(x)
		
for x in location_cat:
	if x in person_cat:
		person_cat.remove(x)
		location_cat.remove(x)

#print person_cat
#print location_cat

data = open('tewiki-latest-all-titles-in-ns0', 'rU')

person_names = ''
location_names = ''

i=0

for title in data:
	i+=1
	try:
		page = wk.page(title)
	except:
		continue
	per = 0
	loc = 0
	title_cat = page.categories
	for x in title_cat:
		x = x.encode('utf-8')
		if x in person_cat:
			per+=1
		elif x in location_cat:
			loc+=1
	if per > loc:
		if per > 2:
			#person_names.append(title)
			person_names += title.encode('utf-8') + '\n'
	elif loc > per:
		if loc > 2:
			#location_names.append(title)
			location_names += title.encode('utf-8') + '\n'
	if i == 5:
		break

gaz_names = open('person_gazetteer.txt', 'w')
gaz_loc = open('location_gazetteer.txt', 'w')

gaz_names.write(person_names)
gaz_names.close()

gaz_loc.write(location_names)
gaz_loc.close()
	
