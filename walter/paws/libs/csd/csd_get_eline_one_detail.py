
def csd_eline_detail(service_id):
    '''
    Args:
        service_id (int)

    To-do:
        Error handling of course
        If there is an error, raise an exception ourselves
        How to have constants not defined inside the function
            - pass as arguments
            - understand namespaces, include as absolute path?
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
    uri = '/api/space/nsas/eline-ptp/service-management/services/'
    csd_url = csd_base_url + uri + str(service_id)
    print("Next is csd_url from the csd_get_eline_one_detail by cli")
    print(csd_url)
    
    # equivalent of 
    # curl -k https://walter-app:H0BmIkxSs@193.1.255.5/api/space/nsas/eline-ptp/service-management/services/1605655
    r = requests.get(csd_url, auth=(csd_username, csd_password), verify=False, timeout=1)
    #print(r.content)
    root = ET.fromstring(r.content)

    # To work with a local file
    #doc_to_read = 'xml_csd_get_eline_one_detail_csd-proxy.xml'
    #tree = ET.parse(doc_to_read)
    #root = tree.getroot()

    # Initialize an empty dictionary, this is what this function will return
    eline_detail = {}
    
    logger.debug("Find out the A and B end details. Start searching at the ServiceEndPointGroup level")
    # Auxiliary list and counter as helpers to build dictionary key names
    service_endpoints = [ 'a', 'b']
    n = 0

    for s in root.findall('.//{services.schema.networkapi.jmp.juniper.net}ServiceEndPointGroup'):
        device_name = s.find('.//{services.schema.networkapi.jmp.juniper.net}DeviceName').text
        device_id = s.find('.//{services.schema.networkapi.jmp.juniper.net}DeviceID').text
        interface_name = s.find('.//{services.schema.networkapi.jmp.juniper.net}InterfaceName').text

        # for each service endpoint we will construct a dictionary
        endpoint_details = {}
        endpoint_details['device_name'] = device_name
        endpoint_details['device_id'] = device_id
        endpoint_details['interface_name'] = interface_name
        eline_detail['endpoint_' + service_endpoints[n]] = endpoint_details
        n = n + 1


    logger.debug("Now find out the client")
    for s in root[0].iter('{services.schema.networkapi.jmp.juniper.net}Customer'):
        eline_detail['customer_id'] = s.attrib['key']


    return eline_detail


# mark
# uncoment to test
#service_id = 1605655    # in conductor in status None, client DCU
##service_id = 19465051   # in csd-proxy, in status Up, client Test-Customer
#service_detail = csd_eline_detail(service_id)
#print("Next output of invoking csd_eline_detail from cli")
#print(service_detail)


'''
# output of 
# https://csd-proxy.heanet.ie/api/space/nsas/eline-ptp/service-management/services/19465051

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Data xmlns="services.schema.networkapi.jmp.juniper.net">
    <ServiceResource>
        <Service key="19465051" uri="/api/space/nsas/eline-ptp/service-management/services/19465051" href="/api/space/nsas/eline-ptp/service-management/services/19465051">
            <Common>
                <Name>ek.sfpt.1507895727</Name>
                <Identity>19465051</Identity>
                <State>Deployed</State>
                <Comments>test sfpt</Comments>
                <CreatedDate>2017-10-13T13:03:47.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-10-13T13:03:47.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <Signalling>LDP</Signalling>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <endpointcount>0</endpointcount>
            <ServiceEndPointGroup>
                <DeviceInfo>
                    <NA key="19333795" uri="/api/space/nsas/device-roles/pe-devices/19333795" href="/api/space/nsas/device-roles/pe-devices/19333795">
                        <DeviceName>dist1-testlab</DeviceName>
                        <DeviceID>19333795</DeviceID>
                        <CMPDeviceID>19595361</CMPDeviceID>
                    </NA>
                </DeviceInfo>
                <ServiceEndPoint>
                    <InterfaceName>ge-0/2/0.11</InterfaceName>
                    <InterfaceIndex>519</InterfaceIndex>
                    <ServiceEndpointConfiguration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="PTPElineLDPEndPointConfigParameterServiceType">
                        <EndPointCategory>PTP</EndPointCategory>
                        <TrafficType>DOT1Q Transport single vlan</TrafficType>
                        <PhysicalEncapsulation>flexible-ethernet-services</PhysicalEncapsulation>
                        <LogicalEncapsulation>vlan-ccc</LogicalEncapsulation>
                        <StitchingUnit>0</StitchingUnit>
                        <UNIDescription>test</UNIDescription>
                        <OuterTPID>None</OuterTPID>
                        <UnitId>11</UnitId>
                        <VlanId>11</VlanId>
                        <MTU>9090</MTU>
                        <Bandwidth unit="Mbps">0</Bandwidth>
                    </ServiceEndpointConfiguration>
                    <ServiceTemplates>
                        <ServiceTemplate href="/api/space/nsas/eline-ptp/service-management/service-templates/16941061" uri="/api/space/nsas/eline-ptp/service-management/service-templates/16941061" key="16941061">
                            <ID>16941061</ID>
                            <Name>HEAnet output-vlan-map swap</Name>
                        </ServiceTemplate>
                    </ServiceTemplates>
                </ServiceEndPoint>
                <ServiceEndPointGroupParameter xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="PTPServiceEndpointGroupParameterServiceType">
                    <PEDevice_LoopBackIP>87.44.48.99</PEDevice_LoopBackIP>
                    <PEDevice_NeighborIP>87.44.48.101</PEDevice_NeighborIP>
                </ServiceEndPointGroupParameter>
            </ServiceEndPointGroup>
            <ServiceEndPointGroup>
                <DeviceInfo>
                    <NA key="19333830" uri="/api/space/nsas/device-roles/pe-devices/19333830" href="/api/space/nsas/device-roles/pe-devices/19333830">
                        <DeviceName>edge4-testlab</DeviceName>
                        <DeviceID>19333830</DeviceID>
                        <CMPDeviceID>19595357</CMPDeviceID>
                    </NA>
                </DeviceInfo>
                <ServiceEndPoint>
                    <InterfaceName>ge-0/0/3.10</InterfaceName>
                    <InterfaceIndex>511</InterfaceIndex>
                    <ServiceEndpointConfiguration xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="PTPElineLDPEndPointConfigParameterServiceType">
                        <EndPointCategory>PTP</EndPointCategory>
                        <TrafficType>DOT1Q Transport single vlan</TrafficType>
                        <PhysicalEncapsulation>flexible-ethernet-services</PhysicalEncapsulation>
                        <LogicalEncapsulation>vlan-ccc</LogicalEncapsulation>
                        <StitchingUnit>0</StitchingUnit>
                        <UNIDescription>test</UNIDescription>
                        <OuterTPID>None</OuterTPID>
                        <UnitId>10</UnitId>
                        <VlanId>10</VlanId>
                        <MTU>9090</MTU>
                        <Bandwidth unit="Mbps">0</Bandwidth>
                    </ServiceEndpointConfiguration>
                    <ServiceTemplates>
                        <ServiceTemplate href="/api/space/nsas/eline-ptp/service-management/service-templates/16941061" uri="/api/space/nsas/eline-ptp/service-management/service-templates/16941061" key="16941061">
                            <ID>16941061</ID>
                            <Name>HEAnet output-vlan-map swap</Name>
                        </ServiceTemplate>
                    </ServiceTemplates>
                </ServiceEndPoint>
                <ServiceEndPointGroupParameter xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="PTPServiceEndpointGroupParameterServiceType">
                    <PEDevice_LoopBackIP>87.44.48.101</PEDevice_LoopBackIP>
                    <PEDevice_NeighborIP>87.44.48.99</PEDevice_NeighborIP>
                </ServiceEndPointGroupParameter>
            </ServiceEndPointGroup>
            <ServiceParameters xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="PTPConfigParameterServiceType">
                <MTU>9090</MTU>
                <VCID>35</VCID>
                <VlanNormalization>Swap</VlanNormalization>
            </ServiceParameters>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19465040" href="/api/space/nsas/eline-ptp/service-management/service-orders/19465040" key="19465040"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/950272" href="/api/space/nsas/customer-management/customers/950272" key="950272">
                    <CustomerName>TEST-Customer</CustomerName>
                </Customer>
            </Reference>
        </Service>
    </ServiceResource>
</Data>
'''
