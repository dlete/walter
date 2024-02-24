'''
    References:
        http://www.diveintopython3.net/xml.html
    To-do:
        Nothing for the moment
'''

import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

doc_to_read = 'atom_feed.xml'
#doc_to_read = 'get_all_eline_status_none_conductor.xml'

tree = ET.parse(doc_to_read)
root = tree.getroot()

'''
# OK
print("ROOT")
print(root.tag)
print(root.attrib)
print(root.text)
'''

'''
# OK
for child in root:
    print(child.tag)
    print(child.attrib)
'''

'''
# OK
# .iter() hits all the elements with given tag
#for i in root.iter('{http://www.w3.org/2005/Atom}entry'):
for i in root.iter('{http://www.w3.org/2005/Atom}link'):
    print(i.tag)
    print(i.attrib)
    print(i.text)
'''

# OK
# .findall() -> finds ALL elements with a tag which are DIRECT children of the current element
# .find() -> finds the FIRST CHILD with a particular tag or path (XPath)
print("findall() with tag")
for i in root.findall('{http://www.w3.org/2005/Atom}entry'):
    e_title = i.find('{http://www.w3.org/2005/Atom}title').text
    print(e_title)

# NOT OK
print("findall() with XPath")
for i in root.findall("./entry"):
    e_title = i.find('{http://www.w3.org/2005/Atom}title').text
    print(e_title)
