# -*- coding: utf-8 -*-
"""
Created on Wed Jun 01 11:36:23 2016

@author: james.bradley
"""

from sys import *
from lxml import etree, objectify   # For DTD parsing and XML vaidation
# from io import StringIO           # For alternate approach (see other code components below)

""" Read XML file for validation """
error_found = False
xml_doc_path = 'CourseScheduleMult.xml'
f = open(xml_doc_path)
xml_doc = f.read()
f.close()

""" Read XML file line-by-line for error writing """
f = open(xml_doc_path)
xml_doc_lines = f.readlines()
f.close()

""" Create list of elements representing the lines of the XML document """
xml_doc_lines_strip = []
for this_line in xml_doc_lines:
    xml_doc_lines_strip.append(this_line.rstrip('\n'))

""" Use with alternate approach using StringIO from io package
f = open('COURSE_SCHEDULE.dtd')
dtd_doc = f.read()
f.close()
"""

dtd = etree.DTD(file='COURSE_SCHEDULE.dtd')
#dtd = etree.DTD(StringIO(dtd_doc))  # Alternate using StringIO from io package
#tree = objectify.parse(StringIO(xml_doc))
tree = objectify.fromstring(xml_doc)
dtd.validate(tree) 
    
if len(dtd.error_log.filter_from_errors()) > 0:
    error_found = True
    for error in dtd.error_log.filter_from_errors():
        error_message = error.message
        error_line = error.line
        error_column = error.column
    for this_line in range(len(xml_doc_lines_strip)):
        for this_char in range(len(xml_doc_lines_strip[this_line])):
            if this_line == error_line and this_char == error_column:
                #print ('\033[0;30;41m ' + xml_doc_lines_strip[this_line][this_char])
                stdout.write('\033[0;30;41m' + xml_doc_lines_strip[this_line][this_char])
                 #print "Here it is"
            else:
                #print ('\033[0m ' +xml_doc_lines_strip[this_line][this_char])
                stdout.write('\033[0m' +xml_doc_lines_strip[this_line][this_char])
        print
    #print
    print("\n\033[0;31m Error Message: " + error_message)
    print('\033[0;30m')
    #print
else:
    print("\n\nXML doc okay")
            
        
"""        
thistree = etree.parse(StringIO(xml_doc))
r = thistree.xpath('/COURSE_SCHEDULE/COURSE_NAME')
for rr in r:
    print rr.text
    
print

s = thistree.xpath('/COURSE_SCHEDULE/SESSION/SESSION_NUMBER')
for ss in s:
    print ss.text, type(ss)
    
print
print

s = thistree.xpath('/COURSE_SCHEDULE/SESSION')
print 'len(s): ',len(s)
for ss in s:
    print ss.tag, type(ss)
    try:
        tt = ss.getnext()
        print tt.tag
    except:
        continue
"""