import requests
from bs4 import BeautifulSoup
import re
import urllib.request
import csv
import pandas as pd

#URL = "https://catalog.uidaho.edu/courses/"
#URL = "https://catalog.uidaho.edu/archive/2019-2020/courses/"
#URL = "https://catalog.uidaho.edu/archive/2018-2019/courses/"
URL = "http://uidaho.smartcatalogiq.com/2017-2018/University-of-Idaho-General-Catalog/Courses"
#2017-2018 is weird

page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.findAll('a')

departments = [] #array of all department links
for link in results:
    #note: this actually filters and gets relevant links
    #but it may not be the best for generalizing-->
    #is there a standard structure for department links?
    p =  re.search(r'\/courses\/([^"]+)', str(link))
    #could possible do something with the first group?
    if p:
        departments.append("http://uidaho.smartcatalogiq.com/2017-2018/University-of-Idaho-General-Catalog" + p.group(0))
        
        
#departments_of_interest = [departments[5], departments[4], departments[6], departments[7], departments[10]]

filename = "idaho18-19" + ".csv"

csv_writer = csv.writer(open(filename, 'w'))
csv_writer.writerow(["Department", "Course Catalogue Number", "Course Name", "Description", "Graduate/Undergraduate" "Lab","Year", "Keywords" ])
keywords = [' ag ', ' aquifer ', ' additives ', ' adult health ', ' african diaspora ', ' agave ', ' agrarian ', 'agri', 'agro', 'alcohol', ' almond', ' amendment', ' amino acid', ' anemia ', ' animal', ' anorexia ', ' anthropogenic ', ' apiary ', ' apple', 'applied biological systems', ' apricot', ' aquaculture', ' artichoke', ' artificial insemination ', ' asparagus', ' autecolog', ' avian ', ' avocado', ' bake ', ' baking ', ' banana', ' barley', 'basin scale', ' bean ', ' bee ', ' beef', ' beehive', ' beer', ' bees ', ' beet', 'beneficial insect', 'berries', 'berry', 'bio-based', 'biochar', 'bioenergetic', 'biofuel', 'bioremed', 'biosystem', ' boar ', 'botanic', 'botany', ' bovid ', 'bovine', ' brandy ', ' brassica', ' breakfast ', 'breastfeed', 'breed', ' brew', ' broccoli', 'broiler', ' brussel sprout', ' buck ', ' buckwheat ', ' buffalo', ' bullock', 'butter', ' cabbage', ' calf', ' cantaloupe', ' carbohydrate', ' carcass', ' carrot', ' cassava', ' castor oil', ' cattle', ' cauliflower', ' cereal', 'cheese', ' chef ', ' cherries ', ' cherry ', ' chestnut', ' chicken', ' chickpea', ' chicory', 'child health', ' chocolate', 'chronic condition', ' citrus', 'clover', ' cocktail', ' cocoa ', ' coconut', ' coffee', ' compost', ' contaminant', 'corn', ' cotton ', ' cow', 'cream', 'crop', ' cucumber', ' cuisine', ' culinary ', ' cultivation ', ' curing ', ' dairy ', ' dairies ', ' dessert', ' diabetes ', ' diet', 'digestion', ' dinner', ' distill', ' domesticat', ' drip', 'dryland environments', ' duck', 'dust bowl', ' eat ', ' eating ', ' edaphic ', ' egg', ' eggplant', ' enology', ' ethnobotan', ' ethnomycolog', 'farm', ' FDA ', ' feed ', ' feeding ', ' ferment', ' fertile ', ' fertilize', ' feudal ', ' fiber', 'field equipment', ' fig ', ' fish', ' fistula', 'flavonoid', ' flavor', ' flax', 'floricultur', ' flour ', 'food', 'forage', ' fowl', 'freez', 'french press', 'french toast', ' fruit', ' fry ', ' FSMA ', ' fungal ', 'fungi', ' fungus ', ' furrow', 'game bird', 'garden', ' garlic', 'gastro', ' geese ', ' geoarchaeolog', 'geospatial', ' gin ', ' ginger', ' glasshouse ', 'GMO', ' goat', ' gourd', ' grain', ' grape', ' greenhouse', ' groundwater ', ' guava', ' gut ', 'harvest', ' hay ', ' hazelnut', ' heirloom', ' hemp ', ' herb', ' herba', ' herbi', ' heterosis ', 'high tunnels', ' hog ', 'home economics', 'honey', ' hops ', ' horticult', ' hospitality ', ' hunger ', ' hunt', ' husbandry ', 'hydrologic cycle', ' hydroponic', ' inbred', ' inbreed', ' incubat', ' insecticid', ' IPM ', ' iron ', ' irrigat', ' kitchen', ' kiwi', ' lactat', ' lamb', 'land', ' leek', ' legum', ' lemon', ' lentil', ' lettuce', 'life cycle analysis', ' lime', ' limnolog', ' lipid', ' livestock ', ' lunch', ' macadamia', ' macronutrient', ' maize ', ' malnutrition', ' malt', 'management practice', ' mandarin', ' mango', ' manure', 'maple syrup', ' margarine ', ' mastitis ', ' mating ', ' meal', ' meat', 'melon', ' menu', ' metaboli', ' microfung', ' micronutrient', ' milk ', ' milking ', ' millet', ' mollusk', ' mushroom', ' nectarine', ' nitrogen', ' nonruminant', ' NPK ', ' nurseries ', ' nursery ', 'nut ', 'nuts ', ' nutra', ' nutri', ' oat', ' obesity ', ' off-farm ', 'olive', ' omelet', ' onion', ' orange', ' orchard', ' oxen ', 'packing plant', ' palatab', 'palm oil', ' pancake', ' pantry ', ' pantries ', ' papaya', ' pasture', ' pathogen ', ' peach', ' pear', ' peasant', ' pecan', ' pedigree', ' pedology', ' pepper', ' periparturient', ' permaculture', ' persimmon', ' pest', ' phosphorus ', ' phytochemical', ' pig', ' pistachio', 'plant path', ' plantain', ' plum', ' poison', ' pollen', ' pollinat', ' pomology ', ' pork ', ' postharvest', ' potassium ', ' potato', ' poultry ', ' productivity ', ' progenitor', ' protein', ' pulses ', ' pumpkin ', ' pyrolysis ', ' quinoa ', ' rabbit', ' rainfed ', 'raised bed', ' raisin', ' ranch', 'range grasses', ' rangeland', ' rapeseed ', ' recipe', ' refrigerat', ' restaurant', ' rice ', ' ripe ', ' root ', ' rubber', ' rumen', ' rumina', ' rural ', ' rye', ' sanitation ', ' sausage', ' seafood ', ' seed', ' senescence ', ' sheep ', 'shelf life', ' shellfish', ' slaughter', ' slavery ', ' SNAP ', ' soil', ' sorghum', ' sow', ' soybean', 'species interaction', ' spice', ' spinach', ' spirits ', ' spoil', ' sprinkler', ' squash', ' steer', ' stocker', ' subsistence ', ' sugar', ' swine', ' taco', ' tangerine', ' taro ', ' taste', ' tea ', ' till', ' tobacco', ' tomato', ' tractor', ' transplant', ' transgenic', ' tuber', ' turkey', ' turnip', 'use efficiency', ' vadose ', 'value added', ' vanilla ', ' vegetable', ' vetch', ' vinification ', ' vitamin', ' viticultur', ' vodka', ' waffles', ' watermelon', 'weather risk', ' weed', ' wheat', ' whiskey', ' whisky', ' WIC ', ' wine', ' wool', ' yam', ' yeast', ' zoonoses ', ' zoonotic ']

for dep in departments:
    
    URL = dep
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    #finding department name from page title block
    depname = soup.find(class_= "page-title")
    if depname is None:
        continue
    depname = depname.text
    #end department name


    courses = soup.findAll(class_="courseblock")
    
    
    for course in courses:
  
        #title and course number
        title = course.find(class_= "courseblocktitle").text
    
        count = 0
    
        #splitting title text by the third digit 
        for letter in title:
            if letter.isdigit():
                count +=1
            if count == 3:
                one = title.split(" ")
                number = one[0]
    
                title = title.split(number)[1] 
                count +=1
        #special case where notes are marked in parentheses
        for letter in title:
            if letter == ")":
                one = title.split(")")
                
                title = one[1]
        #title and course number ends
        
        
        #beginning course description  
        if course.find(class_= "courseblockdesc") != None:
            check = course.find(class_= "courseblockdesc")
        
        string = repr(check) #converting check to string
   
        #splitting by html tag
    
        if "</p>" in string:
            lst = string.split("</p>")
        if "<br>" in string:
            lst = string.split("<br>")
        if "<br/>" in string:
            lst = string.split("<br/>")
            
        desc = lst[1]
        #ending course description -- deletes courses without descriptions
        
        #beginning undergrad/grad
        for char in number:
            if char.isdigit():
                if int(char) >=5:
                    
                    
                    grad = "Graduate"
                else:
                    grad = "Undergraduate"
                break #checks only digit in the hundreds column        
        #ending undergrad/grad
        
        #lab--looking through word lab in course description
        lab = False
        if "lab" in desc:
            lab = True
        #ending lab section
        
        year = "2018-2019"
        
        keys = []
        for key in keywords: #<-- filtered
            if (key in title or key in desc):
                keys.append(key)

        if len(keys) > 0:
            csv_writer.writerow([depname, number, title, desc, grad, lab, year, keys])