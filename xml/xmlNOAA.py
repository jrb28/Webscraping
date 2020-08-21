# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:32:02 2016

@author: james.bradley
"""

import requests
from lxml import objectify

response = requests.get("http://w1.weather.gov/xml/current_obs/KJGG.xml").content

print("\nXML from web site")
print("===========================")
print(response)

root = objectify.fromstring(response)
print('Root Tag: ', root.tag, '\n')

print("Selected data from XML structure")
print("=================================")
print('Temperature: ',root["temperature_string"])
print('Wind: ', root['wind_string'])
#print('Heat Index: ',root['heat_index_string'])