import xml.etree.ElementTree as ET


doc_to_read = 'csd_get_all_eline_status_none_conductor.xml'
tree = ET.parse(doc_to_read)
root = tree.getroot()

'''
# OK
print("ROOT")
print("Next is root.tag")
print(root.tag)
print("Next is root.attrib")
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
for child in root[0]:   # for child under <ServiceResource size="1">
    print(child.tag)
    print(child.attrib)
'''

# OK
#for s in root[0].iter('{services.schema.networkapi.jmp.juniper.net}Identity'):
#    print(s.tag)
#    print(s.text)


for s in root[0].findall('{services.schema.networkapi.jmp.juniper.net}Service'):
    print(s.tag)
    #service_id = s.find('{services.schema.networkapi.jmp.juniper.net}Identity')
    #print(service_id)
