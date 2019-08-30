# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:32:02 2016

@author: james.bradley
"""

from lxml import objectify

f_in = open('CourseScheduleMult.xml')
strResponse = f_in.read()
f_in.close()

root = objectify.fromstring(strResponse)
print(root.tag)

for i in range(len(root)):
    print('\nCOURSE_NAME: ',root['COURSE'][i]["COURSE_NAME"])
    for j in range(len(root['COURSE'][i]['SESSION'])):
        print(root['COURSE'][i]['SESSION'][j]['SESSION_NUMBER'],root['COURSE'][i]['SESSION'][j]['DAY'],root['COURSE'][i]['SESSION'][j]['SESSION_TIME'])   