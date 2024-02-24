
def service2customer(service_id):
    '''Given a Service ID, returns what client is that service for
    
    Arguments:
        service_id (srt)

    Returns:
        client_details (dict)

    Todo:
    '''

    import logging
    logger = logging.getLogger(__name__)
    # Change to whatever level of logging you want in the line below
    logging.basicConfig(level=logging.INFO)

    # Initialize an empty dictionary, which is what this function will return
    customer = {}

    logger.debug("Get all the details of the service, there we will find who is the customer")
    import csd_get_eline_one_detail
    service_detail = csd_get_eline_one_detail.csd_eline_detail(service_id)
    #print(service_detail)
    
    customer['customer_id'] = service_detail['customer_id']
    return customer


# mark
# uncomment to test
service_id = 1605655
customer = service2customer(service_id)
print(customer)

