# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 07:57:10 2016

@author: james.bradley
"""

import requests

#search_url = 'https://www.airbnb.com/api/v2/calendar_months?_format=with_conditions&count=3&listing_id=4494357&month=8&year=2018&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en'
search_url = 'https://www.airbnb.com/api/v2/homes_pdp_availability_calendar?currency=USD&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&listing_id=19551496&month=8&year=2019&count=3'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
response = requests.get(search_url, headers=header)

root=response.json()
days = root['calendar_months'][0]['days']
print('Type of variable days: ', type(days))
for day in days:
    print('Data Type of day: ',type(day))
    for k,v in day.items():
        print(k,': ',v)
    print()