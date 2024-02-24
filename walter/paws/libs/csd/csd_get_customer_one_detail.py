

def csd_customer_detail(customer_id):
    '''
    Args:
        customer_id (int)

    Return:
        customer_details (dict)

    To-do:
        Error handling of course
    '''

    import logging
    import requests
    import xml.etree.ElementTree as ET
    from requests.auth import HTTPBasicAuth

    #from settings_csd import csd_base_url
    #from settings_csd import csd_username
    #from settings_csd import csd_password
    
    csd_base_url = 'https://193.1.255.5'
    csd_username = 'walter-app'
    csd_password = 'H0BmIkxSs'

    logger = logging.getLogger(__name__)
    # Change to whatever level of logging you want in the line below
    logging.basicConfig(level=logging.INFO)

    # To work directly with the CSD system
    uri = '/api/space/nsas/customer-management/customers/'
    csd_url = csd_base_url + uri + str(customer_id)
    logging.debug("URL to query: " + csd_url)
    '''
    try:
        r = requests.get(csd_url, auth=(csd_username, csd_password), verify=False, timeout=1)
        ##print(r.content)
        root = ET.fromstring(r.content)
    except Exception as err:
        my_error = "WARNING, the following error has happened: " + str(err)
        return my_error
    '''
    # equivalent of
    # curl -k https://walter-app:H0BmIkxSs@193.1.255.5/api/space/nsas/customer-management/customers/1245258
    r = requests.get(csd_url, auth=(csd_username, csd_password), verify=False, timeout=1)
    ##print(r.content)
    root = ET.fromstring(r.content)

    # To work with a local file
    #doc_to_read = 'xml.csd_get_customer_one_by_customer_id_csd-proxy.xml'
    #tree = ET.parse(doc_to_read)
    #root = tree.getroot()
    
    # Initialize an empty dictionary, this is what this function will return
    customer_details = {}

    customer_name = root.find('.//{services.schema.networkapi.jmp.juniper.net}CustomerName').text
    customer_identity = root.find('.//{services.schema.networkapi.jmp.juniper.net}Identity').text
    customer_account_no = root.find('.//{services.schema.networkapi.jmp.juniper.net}AccountNo').text

    customer_details['customer_name'] = customer_name
    customer_details['customer_id'] = customer_id
    customer_details['customer_account_no'] = customer_account_no

    return customer_details


# mark
# uncomment to test
customer_id = 1245258   # that is DCU in conductor
#customer_id = 950272   # that is TEST-Customer in csd-proxy
customer_details = csd_customer_detail(customer_id)
print(customer_details)


'''
# output of
# https://csd-proxy.heanet.ie/api/space/nsas/customer-management/customers/950272
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Data xmlns="services.schema.networkapi.jmp.juniper.net">
    <Customers>
        <Customer key="950272" uri="/api/space/nsas/customer-management/customers/950272" href="/api/space/nsas/customer-management/  customers/950272">
            <Common>
                <CustomerName>TEST-Customer</CustomerName>
                <Identity>950272</Identity>
                <CreatedDate>2016-10-27T12:26:37.000+01:00</CreatedDate>
                <LastUpdatedDate>2016-10-27T12:26:37.000+01:00</LastUpdatedDate>
            </Common>
            <AccountNo>12345</AccountNo>
        </Customer>
    </Customers>
</Data>
'''
