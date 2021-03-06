#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import csv
import pandas as pd

URL = "https://catalog.uark.edu/archives/2019-2020/undergraduatecatalog/coursesofinstruction/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
    p = re.search(
        r'\/undergraduatecatalog\/coursesofinstruction\/([^"]+)', str(link))

    if p:
        departments.append("https://catalog.uark.edu" + p.group(0))

departments_of_interest = [departments[3], departments[4],
                           departments[5], departments[6], departments[7]]

filename = "arkansas" + ".csv"

csv_writer = csv.writer(open(filename, 'w'))
csv_writer.writerow(["Department", "Course Catalogue Number", "Course Name",
                     "Description", "Graduate/Undergraduate", "Lab", "Year", "Keywords"])
keywords = [' ag ', ' aquifer ', ' additives ', ' adult health ', ' african diaspora ', ' agave ', ' agrarian ', 'agri', 'agro', 'alcohol', ' almond', ' amendment', ' amino acid', ' anemia ', ' animal', ' anorexia ', ' anthropogenic ', ' apiary ', ' apple', 'applied biological systems', ' apricot', ' aquaculture', ' artichoke', ' artificial insemination ', ' asparagus', ' autecolog', ' avian ', ' avocado', ' bake ', ' baking ', ' banana', ' barley', 'basin scale', ' bean ', ' bee ', ' beef', ' beehive', ' beer', ' bees ', ' beet', 'beneficial insect', 'berries', 'berry', 'bio-based', 'biochar', 'bioenergetic', 'biofuel', 'bioremed', 'biosystem', ' boar ', 'botanic', 'botany', ' bovid ', 'bovine', ' brandy ', ' brassica', ' breakfast ', 'breastfeed', 'breed', ' brew', ' broccoli', 'broiler', ' brussel sprout', ' buck ', ' buckwheat ', ' buffalo', ' bullock', 'butter', ' cabbage', ' calf', ' cantaloupe', ' carbohydrate', ' carcass', ' carrot', ' cassava', ' castor oil', ' cattle', ' cauliflower', ' cereal',
            'cheese', ' chef ', ' cherries ', ' cherry ', ' chestnut', ' chicken', ' chickpea', ' chicory', 'child health', ' chocolate', 'chronic condition', ' citrus', 'clover', ' cocktail', ' cocoa ', ' coconut', ' coffee', ' compost', ' contaminant', 'corn', ' cotton ', ' cow', 'cream', 'crop', ' cucumber', ' cuisine', ' culinary ', ' cultivation ', ' curing ', ' dairy ', ' dairies ', ' dessert', ' diabetes ', ' diet', 'digestion', ' dinner', ' distill', ' domesticat', ' drip', 'dryland environments', ' duck', 'dust bowl', ' eat ', ' eating ', ' edaphic ', ' egg', ' eggplant', ' enology', ' ethnobotan', ' ethnomycolog', 'farm', ' FDA ', ' feed ', ' feeding ', ' ferment', ' fertile ', ' fertilize', ' feudal ', ' fiber', 'field equipment', ' fig ', ' fish', ' fistula', 'flavonoid', ' flavor', ' flax', 'floricultur', ' flour ', 'food', 'forage', ' fowl', 'freez', 'french press', 'french toast', ' fruit', ' fry ', ' FSMA ', ' fungal ', 'fungi', ' fungus ', ' furrow', 'game bird', 'garden', ' garlic', 'gastro', ' geese ',
            ' geoarchaeolog', 'geospatial', ' gin ', ' ginger', ' glasshouse ', 'GMO', ' goat', ' gourd', ' grain', ' grape', ' greenhouse', ' groundwater ', ' guava', ' gut ', 'harvest', ' hay ', ' hazelnut', ' heirloom', ' hemp ', ' herb', ' herba', ' herbi', ' heterosis ', 'high tunnels', ' hog ', 'home economics', 'honey', ' hops ', ' horticult', ' hospitality ', ' hunger ', ' hunt', ' husbandry ', 'hydrologic cycle', ' hydroponic', ' inbred', ' inbreed', ' incubat', ' insecticid', ' IPM ', ' iron ', ' irrigat', ' kitchen', ' kiwi', ' lactat', ' lamb', 'land', ' leek', ' legum', ' lemon', ' lentil', ' lettuce', 'life cycle analysis', ' lime', ' limnolog', ' lipid', ' livestock ', ' lunch', ' macadamia', ' macronutrient', ' maize ', ' malnutrition', ' malt', 'management practice', ' mandarin', ' mango', ' manure', 'maple syrup', ' margarine ', ' mastitis ', ' mating ', ' meal', ' meat', 'melon', ' menu', ' metaboli', ' microfung', ' micronutrient', ' milk ', ' milking ', ' millet', ' mollusk', ' mushroom', ' nectarine',
            ' nitrogen', ' nonruminant', ' NPK ', ' nurseries ', ' nursery ', 'nut ', 'nuts ', ' nutra', ' nutri', ' oat', ' obesity ', ' off-farm ', 'olive', ' omelet', ' onion', ' orange', ' orchard', ' oxen ', 'packing plant', ' palatab', 'palm oil', ' pancake', ' pantry ', ' pantries ', ' papaya', ' pasture', ' pathogen ', ' peach', ' pear', ' peasant', ' pecan', ' pedigree', ' pedology', ' pepper', ' periparturient', ' permaculture', ' persimmon', ' pest', ' phosphorus ', ' phytochemical', ' pig', ' pistachio', 'plant path', ' plantain', ' plum', ' poison', ' pollen', ' pollinat', ' pomology ', ' pork ', ' postharvest', ' potassium ', ' potato', ' poultry ', ' productivity ', ' progenitor', ' protein', ' pulses ', ' pumpkin ', ' pyrolysis ', ' quinoa ', ' rabbit', ' rainfed ', 'raised bed', ' raisin', ' ranch', 'range grasses', ' rangeland', ' rapeseed ', ' recipe', ' refrigerat', ' restaurant', ' rice ', ' ripe ', ' root ', ' rubber', ' rumen', ' rumina', ' rural ', ' rye', ' sanitation ', ' sausage', ' seafood ',
            ' seed', ' senescence ', ' sheep ', 'shelf life', ' shellfish', ' slaughter', ' slavery ', ' SNAP ', ' soil', ' sorghum', ' sow', ' soybean', 'species interaction', ' spice', ' spinach', ' spirits ', ' spoil', ' sprinkler', ' squash', ' steer', ' stocker', ' subsistence ', ' sugar', ' swine', ' taco', ' tangerine', ' taro ', ' taste', ' tea ', ' till', ' tobacco', ' tomato', ' tractor', ' transplant', ' transgenic', ' tuber', ' turkey', ' turnip', 'use efficiency', ' vadose ', 'value added', ' vanilla ', ' vegetable', ' vetch', ' vinification ', ' vitamin', ' viticultur', ' vodka', ' waffles', ' watermelon', 'weather risk', ' weed', ' wheat', ' whiskey', ' whisky', ' WIC ', ' wine', ' wool', ' yam', ' yeast', ' zoonoses ', ' zoonotic ']

for dep in departments:
    URL = dep
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    courses = soup.findAll(class_="courseblock")
    department = soup.title
    department = re.findall('\>(.*)\ &', str(department))[0]
    for course in courses:
        intro = course.find(class_="courseblocktitle").text
        splt = intro.split(".")
        title = splt[0] + splt[1]
        desc = course.find(class_="courseblockdesc").text
        ccn = re.findall('[0-9]+\w?', str(title))[0]
        graduate = "U"
        year = "2019-2020"

        allKeyWords = []
        for key in keywords:  # filtered
            if (re.search(key, title, flags=re.IGNORECASE) or
                    re.search(key, desc, flags=re.IGNORECASE)):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow([department, ccn.encode(
                'utf-8'), title.encode('utf-8'), desc.encode('utf-8'), None, None, year, allKeyWords])

# In[6]:


URL = "https://catalog.uark.edu/archives/2018-19/undergraduatecatalog/coursesofinstruction/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
    p = re.search(
        r'\/undergraduatecatalog\/coursesofinstruction\/([^"]+)', str(link))

    if p:
        departments.append("https://catalog.uark.edu" + p.group(0))

for dep in departments:
    URL = dep
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    courses = soup.findAll(class_="courseblock")
    department = soup.title
    department = re.findall('\>(.*)\ &', str(department))[0]
    for course in courses:
        intro = course.find(class_="courseblocktitle").text
        splt = intro.split(".")
        title = splt[0] + splt[1]
        desc = course.find(class_="courseblockdesc").text
        ccn = re.findall('[0-9]+\w?', str(title))[0]
        graduate = "U"
        year = "2018-2019"

        allKeyWords = []
        for key in keywords:  # filtered
            if (re.search(key, title, flags=re.IGNORECASE) or
                    re.search(key, desc, flags=re.IGNORECASE)):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow([department, ccn.encode(
                'utf-8'), title.encode('utf-8'), desc.encode('utf-8'), None, None, year, allKeyWords])


# In[7]:

URL = "https://catalog.uark.edu/archives/2017-18/undergraduatecatalog/coursesofinstruction/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
    p = re.search(
        r'\/undergraduatecatalog\/coursesofinstruction\/([^"]+)', str(link))

    if p:
        departments.append("https://catalog.uark.edu" + p.group(0))

for dep in departments:
    URL = dep
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    courses = soup.findAll(class_="courseblock")
    department = soup.title
    department = re.findall('\>(.*)\ &', str(department))

    if department:
        department = department[0]
    else:
        continue

    for course in courses:
        intro = course.find(class_="courseblocktitle").text
        splt = intro.split(".")
        title = splt[0] + splt[1]
        desc = course.find(class_="courseblockdesc").text
        ccn = re.findall('[0-9]+\w?', str(title))[0]
        graduate = "U"
        year = "2017-2018"

        allKeyWords = []
        for key in keywords:  # filtered
            if (re.search(key, title, flags=re.IGNORECASE) or
                    re.search(key, desc, flags=re.IGNORECASE)):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow([department, ccn.encode(
                'utf-8'), title.encode('utf-8'), desc.encode('utf-8'), None, None, year, allKeyWords])


# %%

URL = "https://catalog.uark.edu/archives/2016-17/undergraduatecatalog/coursesofinstruction/"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []
for link in results:
    p = re.search(
        r'\/undergraduatecatalog\/coursesofinstruction\/([^"]+)', str(link))

    if p:
        departments.append("https://catalog.uark.edu" + p.group(0))

for dep in departments:
    URL = dep
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    courses = soup.findAll(class_="courseblock")
    department = soup.title
    department = re.findall('\>(.*)\ &', str(department))

    if department:
        department = department[0]
    else:
        continue

    for course in courses:
        intro = course.find(class_="courseblocktitle").text
        splt = intro.split(".")
        title = splt[0] + splt[1]
        desc = course.find(class_="courseblockdesc").text
        ccn = re.findall('[0-9]+\w?', str(title))[0]
        graduate = "U"
        year = "2016-2017"

        allKeyWords = []
        for key in keywords:  # filtered
            if (re.search(key, title, flags=re.IGNORECASE) or
                    re.search(key, desc, flags=re.IGNORECASE)):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow([department, ccn.encode(
                'utf-8'), title.encode('utf-8'), desc.encode('utf-8'), None, None, year, allKeyWords])

# %%

data = pd.read_csv('arkansas.csv')
data
# %%

# %%
