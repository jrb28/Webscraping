# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:32:02 2016

@author: james.bradley
"""

from lxml import objectify

f_in = open('CourseSchedule.xml')
strResponse = f_in.read()
f_in.close()

root = objectify.fromstring(strResponse)
print(root.tag)

print('\nCOURSE_NAME: ',root['COURSE']["COURSE_NAME"])
for j in range(len(root['COURSE']['SESSION'])):
    print(root['COURSE']['SESSION'][j]['SESSION_NUMBER'],root['COURSE']['SESSION'][j]['DAY'],root['COURSE']['SESSION'][j]['SESSION_TIME'])