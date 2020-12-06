#!/usr/bin/env python
# coding: utf-8

# %%
import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import csv
import pandas as pd

URL = "https://hilo.hawaii.edu/catalog19-20/undergraduate-courses"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []  # array of all department links
for link in results:
    # note: this actually filters and gets relevant links
    # but it may not be the best for generalizing-->
    # is there a standard structure for department links?
    # gets link between the quotation marks
    p = re.search(r'([^"]+)-courses', str(link))

    # print(p)
    # could possible do something with the first group?
    if p:
        departments.append(
            "https://hilo.hawaii.edu/catalog19-20/" + p.group(0))

# departments = departments[9:82]  #elimates the links that aren't course catalog related

# newdep = []  #getting rid of quotation marks around the link

# for item in departments:
#     one = item.split('"')
#     newdep.append(one[0] + one[1])

# departments = newdep

# departments_of_interest = [departments[3], departments[4], departments[5], departments[6], departments[7], departments[8]]

filename = "hawaii" + ".csv"

end = []

csv_writer = csv.writer(open(filename, 'w'))
csv_writer.writerow(["Department", "Course Catalogue Number", "Course Name", "Description", "Graduate/Undergraduate", "Lab", "Year", "Keywords"])
keywords = [' ag ', ' aquifer ', ' additives ', ' adult health ', ' african diaspora ', ' agave ', ' agrarian ', 'agri', 'agro', 'alcohol', ' almond', ' amendment', ' amino acid', ' anemia ', ' animal', ' anorexia ', ' anthropogenic ', ' apiary ', ' apple', 'applied biological systems', ' apricot', ' aquaculture', ' artichoke', ' artificial insemination ', ' asparagus', ' autecolog', ' avian ', ' avocado', ' bake ', ' baking ', ' banana', ' barley', 'basin scale', ' bean ', ' bee ', ' beef', ' beehive', ' beer', ' bees ', ' beet', 'beneficial insect', 'berries', 'berry', 'bio-based', 'biochar', 'bioenergetic', 'biofuel', 'bioremed', 'biosystem', ' boar ', 'botanic', 'botany', ' bovid ', 'bovine', ' brandy ', ' brassica', ' breakfast ', 'breastfeed', 'breed', ' brew', ' broccoli', 'broiler', ' brussel sprout', ' buck ', ' buckwheat ', ' buffalo', ' bullock', 'butter', ' cabbage', ' calf', ' cantaloupe', ' carbohydrate', ' carcass', ' carrot', ' cassava', ' castor oil', ' cattle', ' cauliflower', ' cereal',
            'cheese', ' chef ', ' cherries ', ' cherry ', ' chestnut', ' chicken', ' chickpea', ' chicory', 'child health', ' chocolate', 'chronic condition', ' citrus', 'clover', ' cocktail', ' cocoa ', ' coconut', ' coffee', ' compost', ' contaminant', 'corn', ' cotton ', ' cow', 'cream', 'crop', ' cucumber', ' cuisine', ' culinary ', ' cultivation ', ' curing ', ' dairy ', ' dairies ', ' dessert', ' diabetes ', ' diet', 'digestion', ' dinner', ' distill', ' domesticat', ' drip', 'dryland environments', ' duck', 'dust bowl', ' eat ', ' eating ', ' edaphic ', ' egg', ' eggplant', ' enology', ' ethnobotan', ' ethnomycolog', 'farm', ' FDA ', ' feed ', ' feeding ', ' ferment', ' fertile ', ' fertilize', ' feudal ', ' fiber', 'field equipment', ' fig ', ' fish', ' fistula', 'flavonoid', ' flavor', ' flax', 'floricultur', ' flour ', 'food', 'forage', ' fowl', 'freez', 'french press', 'french toast', ' fruit', ' fry ', ' FSMA ', ' fungal ', 'fungi', ' fungus ', ' furrow', 'game bird', 'garden', ' garlic', 'gastro', ' geese ',
            ' geoarchaeolog', 'geospatial', ' gin ', ' ginger', ' glasshouse ', 'GMO', ' goat', ' gourd', ' grain', ' grape', ' greenhouse', ' groundwater ', ' guava', ' gut ', 'harvest', ' hay ', ' hazelnut', ' heirloom', ' hemp ', ' herb', ' herba', ' herbi', ' heterosis ', 'high tunnels', ' hog ', 'home economics', 'honey', ' hops ', ' horticult', ' hospitality ', ' hunger ', ' hunt', ' husbandry ', 'hydrologic cycle', ' hydroponic', ' inbred', ' inbreed', ' incubat', ' insecticid', ' IPM ', ' iron ', ' irrigat', ' kitchen', ' kiwi', ' lactat', ' lamb', 'land', ' leek', ' legum', ' lemon', ' lentil', ' lettuce', 'life cycle analysis', ' lime', ' limnolog', ' lipid', ' livestock ', ' lunch', ' macadamia', ' macronutrient', ' maize ', ' malnutrition', ' malt', 'management practice', ' mandarin', ' mango', ' manure', 'maple syrup', ' margarine ', ' mastitis ', ' mating ', ' meal', ' meat', 'melon', ' menu', ' metaboli', ' microfung', ' micronutrient', ' milk ', ' milking ', ' millet', ' mollusk', ' mushroom', ' nectarine',
            ' nitrogen', ' nonruminant', ' NPK ', ' nurseries ', ' nursery ', 'nut ', 'nuts ', ' nutra', ' nutri', ' oat', ' obesity ', ' off-farm ', 'olive', ' omelet', ' onion', ' orange', ' orchard', ' oxen ', 'packing plant', ' palatab', 'palm oil', ' pancake', ' pantry ', ' pantries ', ' papaya', ' pasture', ' pathogen ', ' peach', ' pear', ' peasant', ' pecan', ' pedigree', ' pedology', ' pepper', ' periparturient', ' permaculture', ' persimmon', ' pest', ' phosphorus ', ' phytochemical', ' pig', ' pistachio', 'plant path', ' plantain', ' plum', ' poison', ' pollen', ' pollinat', ' pomology ', ' pork ', ' postharvest', ' potassium ', ' potato', ' poultry ', ' productivity ', ' progenitor', ' protein', ' pulses ', ' pumpkin ', ' pyrolysis ', ' quinoa ', ' rabbit', ' rainfed ', 'raised bed', ' raisin', ' ranch', 'range grasses', ' rangeland', ' rapeseed ', ' recipe', ' refrigerat', ' restaurant', ' rice ', ' ripe ', ' root ', ' rubber', ' rumen', ' rumina', ' rural ', ' rye', ' sanitation ', ' sausage', ' seafood ',
            ' seed', ' senescence ', ' sheep ', 'shelf life', ' shellfish', ' slaughter', ' slavery ', ' SNAP ', ' soil', ' sorghum', ' sow', ' soybean', 'species interaction', ' spice', ' spinach', ' spirits ', ' spoil', ' sprinkler', ' squash', ' steer', ' stocker', ' subsistence ', ' sugar', ' swine', ' taco', ' tangerine', ' taro ', ' taste', ' tea ', ' till', ' tobacco', ' tomato', ' tractor', ' transplant', ' transgenic', ' tuber', ' turkey', ' turnip', 'use efficiency', ' vadose ', 'value added', ' vanilla ', ' vegetable', ' vetch', ' vinification ', ' vitamin', ' viticultur', ' vodka', ' waffles', ' watermelon', 'weather risk', ' weed', ' wheat', ' whiskey', ' whisky', ' WIC ', ' wine', ' wool', ' yam', ' yeast', ' zoonoses ', ' zoonotic ']


for dep in departments:
    URL = dep
    try:
        page = requests.get(URL)  # connection refused error keeps popping up
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"

    soup = BeautifulSoup(page.text, 'html.parser')

    # finding department name from page title block
    depname = soup.find(id="page-content-title").text

    # end department name

    year = "2019-2020"

    courses = soup.findAll(class_="courses")
    if not courses:
        continue

    one = re.findall(r'<p>(.+?)</p>', str(courses[0]))

    for course in one:

        # finding title and course number
        full = re.findall(r'<strong>(.+?)</strong>', course)

        for item in full:

            # finding number specicfically
            two = item.split(" ")
            if two[1] == "":
                number = two[0] + str(two[2])
                num = str(two[2])

            else:
                number = two[0] + two[1]
                num = two[1]
            # ending finding number

            # finding course title
            three = item.split(num)
            four = three[1].split("(")
            title = four[0]
            # ending course title
        # end of finding title and course number

        # beginning desc
        desc = re.findall(r'</strong>(.+)', course)[0]
        # end desc

        # beginning undergrad/grad
        grad = "Undergraduate"
        # ending undergrad/grad

        # lab--looking through word lab in course description
        lab = False
        if "lab" in desc:
            lab = True
        # ending lab section

        allKeyWords = []

        for key in keywords:  # <-- filtered
            if (key in title or key in desc):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow(
                [depname, number, title, desc, grad, lab, year, allKeyWords])


# %%

URL = "https://hilo.hawaii.edu/catalog18-19/undergraduate-courses"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []  # array of all department links
for link in results:
    # note: this actually filters and gets relevant links
    # but it may not be the best for generalizing-->
    # is there a standard structure for department links?
    # gets link between the quotation marks
    p = re.search(r'([^"]+)-courses', str(link))

    # could possible do something with the first group?
    if p:
        departments.append(
            "https://hilo.hawaii.edu/catalog18-19/" + p.group(0))

for dep in departments:
    URL = dep
    try:
        page = requests.get(URL)  # connection refused error keeps popping up
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"

    soup = BeautifulSoup(page.text, 'html.parser')

    # finding department name from page title block
    depname = soup.find(id="page-content-title").text

    # end department name

    year = "2018-2019"

    courses = soup.findAll(class_="courses")
    if not courses:
        continue

    one = re.findall(r'<p>(.+?)</p>', str(courses[0]))

    for course in one:

        # finding title and course number
        full = re.findall(r'<strong>(.+?)</strong>', course)

        for item in full:

            # finding number specicfically
            two = item.split(" ")

            if len(two) <= 1:
                continue
            elif two[1] == "":
                number = two[0] + str(two[2])
                num = str(two[2])

            else:
                number = two[0] + two[1]
                num = two[1]
            # ending finding number

            # finding course title
            three = item.split(num)
            four = three[1].split("(")
            title = four[0]
            # ending course title
        # end of finding title and course number

        # beginning desc
        desc = re.findall(r'</strong>(.+)', course)[0]
        # end desc

        # beginning undergrad/grad
        grad = "Undergraduate"
        # ending undergrad/grad

        # lab--looking through word lab in course description
        lab = False
        if "lab" in desc:
            lab = True
        # ending lab section

        allKeyWords = []

        for key in keywords:  # <-- filtered
            if (key in title or key in desc):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow(
                [depname, number, title, desc, grad, lab, year, allKeyWords])

# %%

URL = "https://hilo.hawaii.edu/catalog17-18/undergraduate-courses"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []  # array of all department links
for link in results:
    # note: this actually filters and gets relevant links
    # but it may not be the best for generalizing-->
    # is there a standard structure for department links?
    # gets link between the quotation marks
    p = re.search(r'([^"]+)-courses', str(link))

    # could possible do something with the first group?
    if p:
        departments.append(
            "https://hilo.hawaii.edu/catalog17-18/" + p.group(0))

for dep in departments:
    URL = dep
    try:
        page = requests.get(URL)  # connection refused error keeps popping up
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"

    soup = BeautifulSoup(page.text, 'html.parser')

    # finding department name from page title block
    depname = soup.find(id="page-content-title").text

    # end department name

    year = "2017-2018"

    courses = soup.findAll(class_="courses")
    if not courses:
        continue

    one = re.findall(r'<p>(.+?)</p>', str(courses[0]))

    for course in one:

        # finding title and course number
        full = re.findall(r'<strong>(.+?)</strong>', course)

        for item in full:

            # finding number specicfically
            two = item.split(" ")

            if len(two) <= 1:
                continue
            elif two[1] == "":
                number = two[0] + str(two[2])
                num = str(two[2])

            else:
                number = two[0] + two[1]
                num = two[1]
            # ending finding number

            # finding course title
            three = item.split(num)
            four = three[1].split("(")
            title = four[0]
            # ending course title
        # end of finding title and course number

        # beginning desc
        desc = re.findall(r'</strong>(.+)', course)[0]
        # end desc

        # beginning undergrad/grad
        grad = "Undergraduate"
        # ending undergrad/grad

        # lab--looking through word lab in course description
        lab = False
        if "lab" in desc:
            lab = True
        # ending lab section

        allKeyWords = []

        for key in keywords:  # <-- filtered
            if (key in title or key in desc):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow(
                [depname, number, title, desc, grad, lab, year, allKeyWords])


# %%

URL = "https://hilo.hawaii.edu/catalog16-17/undergraduate-courses"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = []  # array of all department links
for link in results:
    # note: this actually filters and gets relevant links
    # but it may not be the best for generalizing-->
    # is there a standard structure for department links?
    # gets link between the quotation marks
    p = re.search(r'([^"]+)-courses', str(link))

    # could possible do something with the first group?
    if p:
        departments.append(
            "https://hilo.hawaii.edu/catalog16-17/" + p.group(0))

for dep in departments:
    URL = dep
    try:
        page = requests.get(URL)  # connection refused error keeps popping up
    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"

    soup = BeautifulSoup(page.text, 'html.parser')

    # finding department name from page title block
    depname = soup.find(id="page-content-title").text

    # end department name

    year = "2016-2017"

    courses = soup.findAll(class_="courses")
    if not courses:
        continue

    one = re.findall(r'<p>(.+?)</p>', str(courses[0]))

    for course in one:

        # finding title and course number
        full = re.findall(r'<strong>(.+?)</strong>', course)

        for item in full:

            # finding number specicfically
            two = item.split(" ")

            if len(two) <= 1:
                continue
            elif two[1] == "":
                number = two[0] + str(two[2])
                num = str(two[2])

            else:
                number = two[0] + two[1]
                num = two[1]
            # ending finding number

            # finding course title
            three = item.split(num)
            four = three[1].split("(")
            title = four[0]
            # ending course title
        # end of finding title and course number

        # beginning desc
        desc = re.findall(r'</strong>(.+)', course)[0]
        # end desc

        # beginning undergrad/grad
        grad = "Undergraduate"
        # ending undergrad/grad

        # lab--looking through word lab in course description
        lab = False
        if "lab" in desc:
            lab = True
        # ending lab section

        allKeyWords = []

        for key in keywords:  # <-- filtered
            if (key in title or key in desc):
                allKeyWords.append(key)

        if len(allKeyWords) > 0:
            csv_writer.writerow(
                [depname, number, title, desc, grad, lab, year, allKeyWords])


# %%

data = pd.read_csv("hawaii.csv")
data

# %%
