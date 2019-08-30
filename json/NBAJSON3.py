# -*- coding: utf-8 -*-
"""
Created on Thu Sep 01 07:57:10 2016

@author: james.bradley
"""

import requests

search_url = 'http://buckets.peterbeshai.com/api/?player=201935&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
#response = requests.get(search_url)

for shot in response.json():
    print(shot["ACTION_TYPE"])