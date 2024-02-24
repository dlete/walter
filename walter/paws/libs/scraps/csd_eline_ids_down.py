
def csd_eline_ids_down():
    import requests
    from requests.auth import HTTPBasicAuth

    from settings_csd import csd_url
    from settings_csd import csd_username
    from settings_csd import csd_password

    #csd_url = 'https://193.1.255.5/api/space/nsas/eline-ptp/service-management/services?faultStatus=None'
    #csd_username = 'walter-app'
    #csd_password = 'H0BmIkxSs'

    r = requests.get(csd_url, auth=(csd_username, csd_password), verify=False)
    #print(r.content)



    import xml.etree.ElementTree as ET

    #doc_to_read = 'csd_get_all_eline_status_none_conductor.xml'
    #tree = ET.parse(doc_to_read)
    #root = tree.getroot()

    root = ET.fromstring(r.content)

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

    eline_ids_down = []
    # OK
    # THIS IS THE ONE
    for s in root[0].iter('{services.schema.networkapi.jmp.juniper.net}Identity'):
    #    print(s.tag)
        #print(s.text)
        eline_ids_down.append(s.text)

    return eline_ids_down



s_ids_down = csd_eline_ids_down()
for s_id in s_ids_down:
    print(s_id)
