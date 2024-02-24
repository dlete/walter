
def host2csd_servies(hostname, service_fault_status):
    '''Finds out what services are associated with a given host

    Args:
        hostname (str)
        service_fault_status (str)
    '''
    import logging

    logger = logging.getLogger(__name__)
    # Change to whatever level of logging you want in the line below
    logging.basicConfig(level=logging.INFO)

    # Initialize an empty list, which is what this function will return
    csd_eline_services = []

    logger.debug("Get all the services in fault status: " + service_fault_status)
    #import csd_get_all_eline_by_status
    import csd_get_eline_all_by_fault_status
    services_by_status = csd_get_eline_all_by_fault_status.csd_elines_by_fault_status(service_fault_status)
    logger.debug("Next is services_fault_status, a list with all the services in fault status: " + service_fault_status) 
    logger.debug(services_by_status)

    logger.debug("Now we interrogate CSD for the details of each service in fault status: " + service_fault_status)
    logger.debug("And the trick is: ")
    logger.debug("Compare the hostname in the arg with the a_end and the b_end")
    logger.debug("If there is a match, then that is one service we will return")
    #import csd_get_one_eline_detail
    import csd_get_eline_one_detail
    for service_id in services_by_status:
        #print(service_id)
        service_detail = csd_get_eline_one_detail.csd_eline_detail(service_id)
        #print(service_detail)

        #print(hostname)
        #print(service_detail['endpoint_a']['device_name'])
        #print(service_detail['endpoint_b']['device_name'])

        if service_detail['endpoint_a']['device_name'] == hostname:
            #print("OLE!!! end AAAA")
            #print(service_id)
            csd_eline_services.append(service_id)
        if service_detail['endpoint_b']['device_name'] == hostname:
            #print("OLE!!! end BBBB")
            #print(service_id)
            csd_eline_services.append(service_id)

    return csd_eline_services


# mark
# uncomment to test
#my_hostname = 'edge4-testlab'
#my_service_fault_status = 'Down'
#my_services = host2csd_servies(my_hostname, my_service_fault_status)
#print(my_services)
