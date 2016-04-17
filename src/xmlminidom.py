#!/usr/bin/python
#
#Minidom is used to parse xml files
#This is a typical use. Used in real life. 

import xml.dom.minidom
import re

xmlstring="""
... and listening to slow jazz <---should not be here
<?xml version="1.0"?>
<!DOCTYPE PARTS SYSTEM "parts.dtd">
<?xml-stylesheet type="text/css" href="xmlpartsstyle.css"?>
<PARTS>
   <TITLE>Computer Parts</TITLE>
   <PART>
      <ITEM>Motherboard</ITEM>
      <MANUFACTURER>ASUS</MANUFACTURER>
      <MODEL>P3B-F</MODEL>
      <COST> 123.00</COST>
   </PART>
foo <---should not be here
   <PART>
      <ITEM>Video Card</ITEM>
      <MANUFACTURER>ATI</MANUFACTURER>
bar  <---should not be here
      <MODEL>All-in-Wonder Pro</MODEL>
      <COST> 160.00</COST>
   </PART>
</PARTS>"""

#Clean file to use only xml code otherwise minidom wont work
l=[]

for line in xmlstring.split('\n'):
    newxml=re.search(r'<..*>$',line)
    if newxml:
        l.append(line.strip())
        newxml='\n'.join(l)
    
dom = xml.dom.minidom.parseString(newxml)
Topic=dom.getElementsByTagName('PARTS')
i = 0
for node in Topic:
    alist=node.getElementsByTagName('MANUFACTURER')
    for a in alist:
        Title= a.firstChild.data
        print Title

#Output would be ASUS and ATI
