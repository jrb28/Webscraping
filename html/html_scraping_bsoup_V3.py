# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:29:00 2016

@author: james.bradley
"""
"""
Based on this web site: http://stackoverflow.com/questions/11709079/parsing-html-using-python
"""

import re        # Regular Expressions (Regex) package
import requests  # Internet information requests
from bs4 import BeautifulSoup  # Parsing HTML

html_path = 'https://www.basketball-reference.com/players/w/walljo01/gamelog-advanced/2017/'
html_doc = requests.get(html_path).content

""" parse html """
parsed_html = BeautifulSoup(html_doc, 'lxml')
""" get target row(s) """
target_rows = parsed_html.find_all('tr', attrs={'id' : 'pgl_advanced.424'})  # will find one row of data
#target_rows = parsed_html.find_all('tr', attrs={'id' : re.compile('^pgl_advanced.')})  # uses Regex.  Will find all rows of data

print('Number of games found:',len(target_rows))
print('Stats are in data type:',type(target_rows),'\n')
all_games = []
for row in target_rows:
    new_row = []
    for x in row.find_all('td'):
        new_row.append(x.text)    #x.text.encode("ascii",'ignore')
        
    all_games.append(new_row)
    
print('\nHere\'s the Data')
print(all_games)