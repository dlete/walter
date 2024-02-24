
def customer2customer_details(customer_id):
    '''Given a Customer ID, returns all the CSD information for that customer
    
    Arguments:
        customer_id (srt)

    Returns:
        customer_details (dict)

    Todo:
    '''

    import logging
    logger = logging.getLogger(__name__)
    # Change to whatever level of logging you want in the line below
    logging.basicConfig(level=logging.INFO)

    # Initialize an empty dictionary, which is what this function will return
    customer_details = {}

    logger.debug("Get all the details of the customer")
    import csd_get_customer_one_detail
    customer_info = csd_get_customer_one_detail.csd_customer_detail(customer_id)

    customer_details['customer_id'] = customer_info['customer_id']
    customer_details['customer_name'] = customer_info['customer_name']
    customer_details['customer_account_no'] = customer_info['customer_account_no']
    #print(customer_detail)
    
    return customer_details


# mark
# uncomment to test
#customer_id = 1605655
#client = customer2customer_details(customer_id)
#print(client)


'''
(walter) dlete@xavier:/workspace/pjt_walter/walter/paws/libs/csd$ python customer2customer_details.py
{'customer_id': 1605655, 'customer_name': 'TEST-Customer', 'customer_account_no': '12345'}
(walter) dlete@xavier:/workspace/pjt_walter/walter/paws/libs/csd$
'''
