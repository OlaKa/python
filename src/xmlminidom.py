#!/usr/bin/python
#
#Minidom is used to parse xml files
#This is a typical use. Used in real life. 

from xml.dom import minidom
import re

xmlstring="""... Lisa Test, 1992/03/07, I like long
... walks of the beach, watching sun-sets,
... and listening to slow jazz
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
   <PART>
      <ITEM>Video Card</ITEM>
      <MANUFACTURER>ATI</MANUFACTURER>
      <MODEL>All-in-Wonder Pro</MODEL>
      <COST> 160.00</COST>
   </PART>
   <PART>
      <ITEM>Sound Card</ITEM>
      <MANUFACTURER>Creative Labs</MANUFACTURER>
      <MODEL>Sound Blaster Live</MODEL>
      <COST> 80.00</COST>
   </PART>
   <PART>
      <ITEM inch Monitor</ITEM>
      <MANUFACTURER>LG Electronics</MANUFACTURER>
      <MODEL> 995E</MODEL>
      <COST> 290.00</COST>
   </PART>
</PARTS>"""

#Clean file to use only xml code otherwise minidom wont work
l=[]

for line in xmlstring.split('\n'):
    newxml=re.search(r'<..*>$',line)
    if newxml:
        l.append(line.strip())
        newxml='\n'.join(l)
    
