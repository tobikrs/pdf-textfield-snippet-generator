#!/usr/bin/python

import xml.etree.ElementTree as ET
import gzip
import math


# Unzipp

with gzip.open('editor.xopp', 'rb') as f:
    xml_content = f.read()

with open('object_tree.xml', 'wb') as f:
    f.write(xml_content)


# Load Template

with open('template.txt', 'r') as f:
    template = f.read()


# Parse XML

root = ET.parse('object_tree.xml').getroot()


# Gererate Output

output =    '''<?php
# Here is your generated snippet:
'''

for page in root.findall('page'):    
    for text in page.findall('layer/text'):
        string =  text.text
        x = (float(text.get('x')) * math.sqrt(2) / 4) - 1
        y = (float(text.get('y')) * math.sqrt(2) / 4) - 1

        output += template.replace('|text|', string).replace('|x|', str(round(x, 1))).replace('|y|', str(round(y, 1)))


# Create output file

with open('snippet.php', 'w') as f:
    f.write(output)