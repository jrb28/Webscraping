# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 07:35:39 2018

@author: jrbrad
"""

template = 'My name is %s %s'
fName = 'Jim'
lName = 'Bradley'
print(template % (fName,lName))


""" National Data Buoy Center 
    Site offered by National Ocenaic and Atmospehric Administration (NOAA)
    See instructions fore retrieving data at:
        https://www.ndbc.noaa.gov/rss_access.shtml """
template = 'https://www.ndbc.noaa.gov/rss/ndbc_obs_search.php?lat=%sN&lon=%s&radius=%s'
lat = '37.211781'
lon = '-76.782376'
radius = '50'
URL1 = template % (lat,lon,radius)
print(URL1)

template = 'http://rss.nytimes.com/services/xml/rss/nyt/%s'
subject = 'Science.xml'
#subject = 'Environment.xml'
URL2 = template % subject
print(URL2)

template = 'http://rss.nytimes.com/services/xml/rss/nyt/%s'
#subject = 'Science.xml'
subject = 'Environment.xml'
URL3 = template % subject
print(URL3)

parameter = ''
state = ''
month = ''
year = ''
""" Construct proper template with %s placeholders in urlTemplate """
urlTemplate = ''
""" Place parameter, state, month, year in parentheses in proper order """
URL4 = urlTemplate  % ()
print(URL4)