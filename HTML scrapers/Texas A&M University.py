import requests
from bs4 import BeautifulSoup
import re
import time
import urllib.request
import csv

FS_keys = [' ag ', ' aquifer ', ' additives ', ' adult health ', ' african diaspora ', ' agave ', ' agrarian ', 'agri', 'agro', 'alcohol', ' almond', ' amendment', ' amino acid', ' anemia ', ' animal', ' anorexia ', ' anthropogenic ', ' apiary ', ' apple', 'applied biological systems', ' apricot', ' aquaculture', ' artichoke', ' artificial insemination ', ' asparagus', ' autecolog', ' avian ', ' avocado', ' bake ', ' baking ', ' banana', ' barley', 'basin scale', ' bean ', ' bee ', ' beef', ' beehive', ' beer', ' bees ', ' beet', 'beneficial insect', 'berries', 'berry', 'bio-based', 'biochar', 'bioenergetic', 'biofuel', 'bioremed', 'biosystem', ' boar ', 'botanic', 'botany', ' bovid ', 'bovine', ' brandy ', ' brassica', ' breakfast ', 'breastfeed', 'breed', ' brew', ' broccoli', 'broiler', ' brussel sprout', ' buck ', ' buckwheat ', ' buffalo', ' bullock', 'butter', ' cabbage', ' calf', ' cantaloupe', ' carbohydrate', ' carcass', ' carrot', ' cassava', ' castor oil', ' cattle', ' cauliflower', ' cereal', 'cheese', ' chef ', ' cherries ', ' cherry ', ' chestnut', ' chicken', ' chickpea', ' chicory', 'child health', ' chocolate', 'chronic condition', ' citrus', 'clover', ' cocktail', ' cocoa ', ' coconut', ' coffee', ' compost', ' contaminant', 'corn', ' cotton ', ' cow', 'cream', 'crop', ' cucumber', ' cuisine', ' culinary ', ' cultivation ', ' curing ', ' dairy ', ' dairies ', ' dessert', ' diabetes ', ' diet', 'digestion', ' dinner', ' distill', ' domesticat', ' drip', 'dryland environments', ' duck', 'dust bowl', ' eat ', ' eating ', ' edaphic ', ' egg', ' eggplant', ' enology', ' ethnobotan', ' ethnomycolog', 'farm', ' FDA ', ' feed ', ' feeding ', ' ferment', ' fertile ', ' fertilize', ' feudal ', ' fiber', 'field equipment', ' fig ', ' fish', ' fistula', 'flavonoid', ' flavor', ' flax', 'floricultur', ' flour ', 'food', 'forage', ' fowl', 'freez', 'french press', 'french toast', ' fruit', ' fry ', ' FSMA ', ' fungal ', 'fungi', ' fungus ', ' furrow', 'game bird', 'garden', ' garlic', 'gastro', ' geese ', ' geoarchaeolog', 'geospatial', ' gin ', ' ginger', ' glasshouse ', 'GMO', ' goat', ' gourd', ' grain', ' grape', ' greenhouse', ' groundwater ', ' guava', ' gut ', 'harvest', ' hay ', ' hazelnut', ' heirloom', ' hemp ', ' herb', ' herba', ' herbi', ' heterosis ', 'high tunnels', ' hog ', 'home economics', 'honey', ' hops ', ' horticult', ' hospitality ', ' hunger ', ' hunt', ' husbandry ', 'hydrologic cycle', ' hydroponic', ' inbred', ' inbreed', ' incubat', ' insecticid', ' IPM ', ' iron ', ' irrigat', ' kitchen', ' kiwi', ' lactat', ' lamb', 'land', ' leek', ' legum', ' lemon', ' lentil', ' lettuce', 'life cycle analysis', ' lime', ' limnolog', ' lipid', ' livestock ', ' lunch', ' macadamia', ' macronutrient', ' maize ', ' malnutrition', ' malt', 'management practice', ' mandarin', ' mango', ' manure', 'maple syrup', ' margarine ', ' mastitis ', ' mating ', ' meal', ' meat', 'melon', ' menu', ' metaboli', ' microfung', ' micronutrient', ' milk ', ' milking ', ' millet', ' mollusk', ' mushroom', ' nectarine', ' nitrogen', ' nonruminant', ' NPK ', ' nurseries ', ' nursery ', 'nut ', 'nuts ', ' nutra', ' nutri', ' oat', ' obesity ', ' off-farm ', 'olive', ' omelet', ' onion', ' orange', ' orchard', ' oxen ', 'packing plant', ' palatab', 'palm oil', ' pancake', ' pantry ', ' pantries ', ' papaya', ' pasture', ' pathogen ', ' peach', ' pear', ' peasant', ' pecan', ' pedigree', ' pedology', ' pepper', ' periparturient', ' permaculture', ' persimmon', ' pest', ' phosphorus ', ' phytochemical', ' pig', ' pistachio', 'plant path', ' plantain', ' plum', ' poison', ' pollen', ' pollinat', ' pomology ', ' pork ', ' postharvest', ' potassium ', ' potato', ' poultry ', ' productivity ', ' progenitor', ' protein', ' pulses ', ' pumpkin ', ' pyrolysis ', ' quinoa ', ' rabbit', ' rainfed ', 'raised bed', ' raisin', ' ranch', 'range grasses', ' rangeland', ' rapeseed ', ' recipe', ' refrigerat', ' restaurant', ' rice ', ' ripe ', ' root ', ' rubber', ' rumen', ' rumina', ' rural ', ' rye', ' sanitation ', ' sausage', ' seafood ', ' seed', ' senescence ', ' sheep ', 'shelf life', ' shellfish', ' slaughter', ' slavery ', ' SNAP ', ' soil', ' sorghum', ' sow', ' soybean', 'species interaction', ' spice', ' spinach', ' spirits ', ' spoil', ' sprinkler', ' squash', ' steer', ' stocker', ' subsistence ', ' sugar', ' swine', ' taco', ' tangerine', ' taro ', ' taste', ' tea ', ' till', ' tobacco', ' tomato', ' tractor', ' transplant', ' transgenic', ' tuber', ' turkey', ' turnip', 'use efficiency', ' vadose ', 'value added', ' vanilla ', ' vegetable', ' vetch', ' vinification ', ' vitamin', ' viticultur', ' vodka', ' waffles', ' watermelon', 'weather risk', ' weed', ' wheat', ' whiskey', ' whisky', ' WIC ', ' wine', ' wool', ' yam', ' yeast', ' zoonoses ', ' zoonotic ']

filename = "Texas_A&M_University 2016-20 Webscraped.csv"
csv_writer = csv.writer(open(filename, 'w'))
csv_writer.writerow(["Course Catalogue Number", "Department Name", "Course Name", "Course Description", "Graduate/Undergraduate", "Format", "Lab", 
 "Academic Catalogue Year", "Food Systems", "Food Justice/Equity",
 "Critical Pedagogy",'Keyword'])

### start repeat ### 2016-17

#change year
year = "2016-2017"

#change URL
URL = 'https://catalog.tamu.edu/archives/2016-2017/undergraduate/course-descriptions/'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
	p =  re.search(r'\/undergraduate\/course-descriptions\/([^"#]+)', str(link))
	if p:
		# change department URL
		departments.append("https://catalog.tamu.edu/archives/2016-2017" + p.group(0))



G_UG = "UG"

for dep in departments:
	URL = dep
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	
	Department_Name = soup.find(class_="pageTitle")
	if Department_Name:
		Department_Name = Department_Name.text

	courses = soup.findAll(class_="courseblock")
	for course in courses:

		title = course.find(class_="courseblocktitle").text

		desc = course.find(class_="courseblockdesc")
		if desc:
			desc = desc.text
		else:
			desc = "No Description"

		other = course.find(class_="hours").text
		if "Lecture" in other:
			form = "Lecture"
		else:
			form = "Other"
		
		if "Lab" in other:
			lab = True
		else:
			lab = False
		
		t = re.search(r"([^\d]+\s\d+\w+)\s(.+)", title)
		if t:
			course_name = t.group(2)
			course_number = t.group(1)

		allkeys = []
		for key in FS_keys:
			if (re.search(key, title, flags=re.IGNORECASE) or re.search(key, desc, flags=re.IGNORECASE)):
				allkeys.append(key)
		
		if len(allkeys)>0:
			csv_writer.writerow([course_number, Department_Name, course_name, desc, G_UG, form, lab, year, None, None, None, allkeys])

### END REPEAT ###


### start repeat ### 2017-2018

#change year
year = "2017-2018"

#change URL
URL = 'https://catalog.tamu.edu/archives/2017-2018/undergraduate/course-descriptions/'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
	p =  re.search(r'\/undergraduate\/course-descriptions\/([^"#]+)', str(link))
	if p:
		# change department URL
		departments.append("https://catalog.tamu.edu/archives/2017-2018" + p.group(0))



G_UG = "UG"

for dep in departments:
	URL = dep
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')
	
	Department_Name = soup.find(class_="pageTitle")
	if Department_Name:
		Department_Name = Department_Name.text

	courses = soup.findAll(class_="courseblock")
	for course in courses:

		title = course.find(class_="courseblocktitle").text

		desc = course.find(class_="courseblockdesc")
		if desc:
			desc = desc.text
		else:
			desc = "No Description"

		other = course.find(class_="hours").text
		if "Lecture" in other:
			form = "Lecture"
		else:
			form = "Other"
		
		if "Lab" in other:
			lab = True
		else:
			lab = False
		
		t = re.search(r"([^\d]+\s\d+\w*)\s(.+)", title)
		if t:
			course_name = t.group(2)
			course_number = t.group(1)

		allkeys = []
		for key in FS_keys:
			if (re.search(key, title, flags=re.IGNORECASE) or re.search(key, desc, flags=re.IGNORECASE)):
				allkeys.append(key)
		
		if len(allkeys)>0:
			csv_writer.writerow([course_number, Department_Name, course_name, desc, G_UG, form, lab, year, None, None, None, allkeys])

### END REPEAT ###

### start repeat ### 2018-2019

#change year
year = "2018-2019"

#change URL
URL = 'https://catalog.tamu.edu/archives/2018-2019/undergraduate/course-descriptions/'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
	p =  re.search(r'\/undergraduate\/course-descriptions\/([^"#]+)', str(link))
	if p:
		# change department URL
		departments.append("https://catalog.tamu.edu/archives/2018-2019" + p.group(0))



G_UG = "UG"

for dep in departments:
	URL = dep
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')

	Department_Name = soup.find(class_="pageTitle")
	if Department_Name:
		Department_Name = Department_Name.text

	courses = soup.findAll(class_="courseblock")

	for course in courses:

		title = course.find(class_="courseblocktitle").text

		desc = course.find(class_="courseblockdesc")
		if desc:
			desc = desc.text
		else:
			desc = "No Description"

		other = course.find(class_="hours").text
		if "Lecture" in other:
			form = "Lecture"
		else:
			form = "Other"
		
		if "Lab" in other:
			lab = True
		else:
			lab = False
		
		t = re.search(r"([^\d]+\s\d+\w*)\s(.+)", title)
		if t:
			course_name = t.group(2)
			course_number = t.group(1)

		allkeys = []
		for key in FS_keys:
			if (re.search(key, title, flags=re.IGNORECASE) or re.search(key, desc, flags=re.IGNORECASE)):
				allkeys.append(key)
		
		if len(allkeys)>0:
			csv_writer.writerow([course_number, Department_Name, course_name, desc, G_UG, form, lab, year, None, None, None, allkeys])

### END REPEAT ###

### start repeat ### 2019-2020

#change year
year = "2019-2020"

#change URL
URL = 'https://catalog.tamu.edu/archives/2019-2020/undergraduate/course-descriptions/'
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
	p =  re.search(r'\/undergraduate\/course-descriptions\/([^"#]+)', str(link))
	if p:
		# change department URL
		departments.append("https://catalog.tamu.edu/archives/2019-2020" + p.group(0))



G_UG = "UG"

for dep in departments:
	URL = dep
	page = requests.get(URL)
	soup = BeautifulSoup(page.text, 'html.parser')

	Department_Name = soup.find(class_="pageTitle")
	if Department_Name:
		Department_Name = Department_Name.text

	courses = soup.findAll(class_="courseblock")
	for course in courses:

		title = course.find(class_="courseblocktitle").text

		desc = course.find(class_="courseblockdesc")
		if desc:
			desc = desc.text
		else:
			desc = "No Description"

		other = course.find(class_="hours").text
		if "Lecture" in other:
			form = "Lecture"
		else:
			form = "Other"
		
		if "Lab" in other:
			lab = True
		else:
			lab = False
		
		t = re.search(r"([^\d]+\s\d+\w*)\s(.+)", title)
		if t:
			course_name = t.group(2)
			course_number = t.group(1)

		allkeys = []
		for key in FS_keys:
			if (re.search(key, title, flags=re.IGNORECASE) or re.search(key, desc, flags=re.IGNORECASE)):
				allkeys.append(key)
		
		if len(allkeys)>0:
			csv_writer.writerow([course_number, Department_Name, course_name, desc, G_UG, form, lab, year, None, None, None, allkeys])

### END REPEAT ###