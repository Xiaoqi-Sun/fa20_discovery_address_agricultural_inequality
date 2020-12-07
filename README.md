
# Addressing Structural Inequality in U.S. Agricultural Higher Education
Visit our project repo [here](https://github.com/Xiaoqi-Sun/fa20_discovery_address_agricultural_inequality).

## Define the Problem
Our research project, titled “Addressing Structural Inequality in U.S. Agricultural Higher Education: An Assessment of Pedagogical Practices and Food Systems Coursework at Land-grant Institutions ”, seeks to create the first comprehensive database of coursework content at all 114 land-grant institutions, tracking food and agricultural courses across these universities and identifying pedagogical methods and food justice content utilized and discussed in these classes.

The land grant university system was established through the Morrill Act in 1862, distributing indigenous land to raise funding for these universities. There are three types of land grant universities, historically white colleges (established in 1862), historically Black colleges (1890) and Tribal colleges (1994). The project will examine how inequities within food and agriculture education in these universities perpetuate food systems injustices in the U.S. outside of the educational system.


## What success would look like  

To reiterate, the overall goal of our project is to web-scrape the course catalogues of 114 land-grant universities using a list of keywords in order to analyze and understand more about the higher-education agriculture classes offered at these universities and the pedagogical techniques utilized there. However, soon after we finished onboarding the project, we realized that completing all 114 schools with 4 years of data from each seemed unlikely to be achieved in the time we had left. As a result, we decided to prioritize getting data in order to make meaningful conclusions and analysis as well as our own learning experiences over the excessively pedantic process of finding each unique pattern for every school and every year to scrape that class catalogue. In the end, we were able to scrape fifteen schools fully and used the data gathered to complete some data analysis.

## Data

Initially, we began with no prepared data and needed to gather all the data by ourselves. We web-scraped four consecutive years of course catalogues using around 300 keywords in order to get a comprehensive look at the agricultural education in these universities. In the process of web scraping, the biggest challenge was to work with different formats of catalogs. The three major formats are HTML, PDF, and Drop-down. It was labor-intensive to scrape PDF catalogs as a new regex pattern is required for each university. For drop-down menu ones, knowledge of Selenium is required. Therefore considering the limited time, we decided to focus on HTML scrapers using the Beautiful Soup library.

Potential bias arose from the selection of keywords, which were determined by the social science team, as we are only interested in agriculture-related coursework. Additionally, the schools we have analyzed are 93% historically white colleges because of accessibility, it might not properly represent the full picture.



![Result of webscraping for Oklahoma State University](https://github.com/Xiaoqi-Sun/fa20_discovery_address_agricultural_inequality/blob/main/Picures/Oklahoma%20State%20University.png?raw=true)
<center>Result of webscraping for Oklahoma State University</center>

## Statistical Models  
Our project did not require any statistical models, as it was not applicable to our goals. When we finished scraping the fifteen schools, we simply analyzed the data we scraped using a variety of approaches. The main variable we were interested in was the frequency of keywords found at different scopes of an institution. We compared the most frequently found keywords between different departments in a single school, between different schools, between different geographic regions of the US, and also between the different types of land grant institutions.


![Bar plot for the top 5 keywords in the Animal Science department of Oklahoma State University](https://github.com/Xiaoqi-Sun/fa20_discovery_address_agricultural_inequality/blob/main/Picures/Oklahoma%20State%20University%20bar%20plot.jpg?raw=true)

<center>Bar plot for the top 5 keywords in the Animal Science department of Oklahoma State University</center>    



![Stacked bar plot for top keywords in the Southwest region](https://github.com/Xiaoqi-Sun/fa20_discovery_address_agricultural_inequality/blob/main/Picures/South%20West.png?raw=true)

<center>Stacked bar plot for top keywords in the Southwest region</center>  

## Impact/Next Steps
The results of this project are still inconclusive due to the lack of data that was able to be collected. We were hoping to compare patterns in the frequency of keywords between the regions and between the three types of land grant institutions; however, we did not not have a comprehensive enough set of data to be truly representative of these different groups, so we were unable to make conclusions about our data. If enough data was collected, we would have expected regions to have clearly distinct courses and frequent keywords that were dependent on the regional geography. Also, as mentioned before, there was a significant bias towards Historically White Schools (HWS) vs Historically Black Schools (HBS), as there was only one HBS that we were able to fully web-scrape. This highlights the inequities within these land-grant universities between HWS and HBS, as HWS had more resources to make these course catalogues more accessible to web-scrape.

The next steps of this project would include scraping the rest of the land grant institutions’ course catalogs, before analyzing the full set of data and making comparisons between the courses and pedagogy found across these institutions. The remaining schools that are still needed to be scraped are in one of two forms: a PDF or a website involving drop down menus. In order to scrape the PDF course catalogs, we will need to come up with REGEX patterns for each catalog, and in order to handle the drop down menus, we would need to use another external tool called Selenium. Both of these forms required more time than we had for the project.

Considering the data we expected to collect, this work may only be relevant in the short/medium term because they are only representative of a specific time period (2016-2020). While we don’t expect much change within universities regarding their food courses and pedagogical methods, COVID may have impacted these universities to a relatively unknown extent.
