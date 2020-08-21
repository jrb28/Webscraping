# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 07:57:10 2016

@author: james.bradley
"""

import requests

search_url = 'https://www.airbnb.com/api/v2/calendar_months?_format=with_conditions&count=4&listing_id=9595397&month=9&year=2018&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=USD&locale=en'
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
response = requests.get(search_url, headers=header)

root=response.json()

print('Example Data Elements')
print('Available? ',root['calendar_months'][0]['days'][0]['available'])
print('Date: ',root['calendar_months'][0]['days'][0]['date'])
print('Price: ',root['calendar_months'][0]['days'][0]['price']['local_price_formatted'])