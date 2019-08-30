# -*- coding: utf-8 -*-
"""
Created on Thu May 26 21:29:00 2016

@author: james.bradley
"""

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

html_path = './CourseScheduleWClues.htm'
f = open(html_path)
html_doc = f.read()
f.close()

# parse html 
parsed_html = BeautifulSoup(html_doc,"lxml")

stats1 = parsed_html.find_all('td', attrs={'clue' : 'SessionNum'})
print(stats1)
print('Type of stats1: ', type(stats1))
print('stats1: ', len(stats1))
print('Full Result                             Tag Width  Clue')
for result in stats1:
    print( result, result.text, result['width'], result['clue'])