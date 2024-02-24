
def clientdb_client_one_tech(client_id):

    import logging
    import requests
    #import xml.etree.ElementTree as ET
    from bs4 import BeautifulSoup
    from requests.auth import HTTPBasicAuth

    logger = logging.getLogger(__name__)
    # Change to whatever level of logging you want in the line below
    logging.basicConfig(level=logging.INFO)

    clientdb_base_url = 'https://clientdb-staging.heanet.ie:8443'
    clientdb_username = 'schools'
    clientdb_password = 'sQuola'

    uri_begin = '/api/clients/'
    client_id = str(client_id)
    uri_end = '/tech_contacts'

    # To work directly with the CSD system
    url = clientdb_base_url + uri_begin + client_id + uri_end
    logging.debug("URL to interrogate in function clientdb_client_one_tech: " + url)

    # equivalent of
    # curl -k https://schools:sQuola@clientdb-staging.heanet.ie:8443/api/clients/55/tech_contacts
    r = requests.get(url, auth=(clientdb_username, clientdb_password), verify=False, timeout=1)
    logging.debug("Ouput of r.content: " + str(r.content))
    logging.debug("Output of r.headers: " + str(r.headers))
    logging.debug("Output of r.headers['content-type']: " + r.headers['content-type'])
    try:
        logging.debug("Output of r.encoding: " + r.enconding)
    except:
        pass
    logging.debug("Output of r.text: " + r.text)

    # Initialize an empty list, this is what this function will return
    list_to_return = []

    soup = BeautifulSoup(r.text, 'html.parser')
    #list_children = list(soup.children)
    #for l in list_children:
    #    print(l)

    logging.debug("Find all HTML elements with tag 'li'")
    import re
    my_contacts = soup.find_all('li')
    for c in my_contacts:
        contact_details = {}
        #print(c.get_text())

        #https://stackoverflow.com/questions/27387415/how-would-i-get-everything-before-a-in-a-string-python
        email_name = c.get_text().split('(')[0]
        contact_details['email_name'] = email_name.strip()

        # https://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document
        # https://developers.google.com/edu/python/regular-expressions
        email_address = re.search(r'[\w.-]+@[\w.-]+', c.get_text())
        if email_address:
            #print(email_address.group(0))
            contact_details['email_address'] = email_address.group(0)
            #print(contact_details)
            list_to_return.append(contact_details)

    return list_to_return


    


# mark
# uncomment to test
#client_id = 17   # that is DCU
client_id = 55   # that is HEAnet GD5
client_tech_contacts = clientdb_client_one_tech(client_id)
print(client_tech_contacts)


'''
(walter) dlete@xavier:/workspace/pjt_walter/walter/paws/libs/clientdb$
(walter) dlete@xavier:/workspace/pjt_walter/walter/paws/libs/clientdb$ curl -k https://schools:sQuola@clientdb-staging.heanet.ie:8443/api/clients/55/tech_contacts
HEAnet (HEANET)
<ul>
        <li>LAN Support (1894) - lan-support@heanet.ie</li>
        <li>Schools NOC (1013) - noc@schools.edu.ie</li>
        <li>HEAnet NOC (1790) - noc@heanet.ie</li>
        <li>Multimedia Team (2588) - multimedia@heanet.ie</li>
</ul>(walter) dlete@xavier:/workspace/pjt_walter/walter/paws/libs/clientdb$
(walter) dlete@xavier:/workspace/pjt_walter/walter/paws/libs/clientdb$
'''
