import xml.etree.ElementTree as ET
tree = ET.parse('py3_parsing.xml')
root = tree.getroot()

'''
print(root.tag)
print(root.attrib)
print(root.text)
'''

for child in root:
    print(child.tag, child.attrib)

for neighbor in root.iter('neighbor'):
    print(neighbor.tag)
    print(neighbor.attrib)
    print(neighbor.text)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
