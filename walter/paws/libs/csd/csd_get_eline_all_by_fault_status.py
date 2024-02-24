
def csd_elines_by_fault_status(fault_status):
    '''Gets list of ELINE in a given status
    
    Args:
        fault_status (str). Possible values are 'Down', 'Up' and 'None'
    
    Returns:
        eline_ids (list)

    Todo:
        Error checking of course
        If there is an error, raise an exception ourselves
        How to have constants not defined inside the function
            - pass as arguments
            - understand namespaces, include as absolute path?
    '''

    import requests
    import xml.etree.ElementTree as ET

    from requests.auth import HTTPBasicAuth

    #from settings_csd import csd_url
    #from settings_csd import csd_username
    #from settings_csd import csd_password

    csd_base_url = 'https://193.1.255.5'
    csd_username = 'walter-app'
    csd_password = 'H0BmIkxSs'


    # To work directly with the CSD system
    #uri = '/api/space/nsas/eline-ptp/service-management/services?faultStatus=None'
    #csd_url = csd_base_url + uri 
    uri = '/api/space/nsas/eline-ptp/service-management/services?faultStatus='
    csd_url = csd_base_url + uri + fault_status
    '''
    try:
        r = requests.get(csd_url, auth=(csd_username, csd_password), verify=False, timeout=1)
        #print(r.content)
        root = ET.fromstring(r.content)
    except Exception as err:
        my_error = "WARNING, the following error has happened: " + str(err)
        return my_error
    '''

    # curl -k https://walter-app:H0BmIkxSs@193.1.255.5/api/space/nsas/eline-ptp/service-management/services?faultStatus=None
    r = requests.get(csd_url, auth=(csd_username, csd_password), verify=False, timeout=1)
    print(csd_url)
    #print(r.content)
    root = ET.fromstring(r.content)


    # To work with a local file
    #doc_to_read = 'xml_csd_get_eline_all_by_status_none_conductor.xml'
    #tree = ET.parse(doc_to_read)
    #root = tree.getroot()


    eline_ids = []
    for s in root[0].iter('{services.schema.networkapi.jmp.juniper.net}Identity'):
        eline_ids.append(s.text)

    print("This is from file csd_elines_by_fault_status")
    print(eline_ids)
    return eline_ids


# mark
# uncomment to test
fault_status = 'Down'
fault_status = 'None'
s_ids_down = csd_elines_by_fault_status(fault_status)
print("Next is from involing csd_elines_by_fault_status from cli")
print(s_ids_down)
#for s_id in s_ids_down:
#    print(s_id)


'''
# output of
# https://csd-proxy.heanet.ie/api/space/nsas/eline-ptp/service-management/services
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Data xmlns="services.schema.networkapi.jmp.juniper.net">
    <ServiceResource size="34">
        <Service key="16712529" uri="/api/space/nsas/eline-ptp/service-management/services/16712529" href="/api/space/nsas/eline-ptp/service-management/services/16712529">
            <Common>
                <Name>itb.gn-kp.1490261522</Name>
                <Identity>16712529</Identity>
                <State>Deployed</State>
                <CreatedDate>2017-03-23T09:42:50.000Z</CreatedDate>
                <LastUpdatedDate>2017-03-23T09:42:50.000Z</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Up</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>None</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>Up</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/16712518" href="/api/space/nsas/eline-ptp/service-management/service-orders/16712518" key="16712518"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/15826962" href="/api/space/nsas/customer-management/customers/15826962" key="15826962">
                    <CustomerName>ITB-Institute of Technology Blanchardstown</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="16712562" uri="/api/space/nsas/eline-ptp/service-management/services/16712562" href="/api/space/nsas/eline-ptp/service-management/services/16712562">
            <Common>
                <Name>itb.gn-kp.1490261979</Name>
                <Identity>16712562</Identity>
                <State>Deployed</State>
                <CreatedDate>2017-03-23T09:44:04.000Z</CreatedDate>
                <LastUpdatedDate>2017-03-23T09:44:04.000Z</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Up</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>None</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>Up</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/16712551" href="/api/space/nsas/eline-ptp/service-management/service-orders/16712551" key="16712551"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/15826962" href="/api/space/nsas/customer-management/customers/15826962" key="15826962">
                    <CustomerName>ITB-Institute of Technology Blanchardstown</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="16712586" uri="/api/space/nsas/eline-ptp/service-management/services/16712586" href="/api/space/nsas/eline-ptp/service-management/services/16712586">
            <Common>
                <Name>itb.gn-kp.1490262021</Name>
                <Identity>16712586</Identity>
                <State>Deployed</State>
                <CreatedDate>2017-03-23T09:43:26.000Z</CreatedDate>
                <LastUpdatedDate>2017-03-23T09:43:26.000Z</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Up</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>None</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>Up</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/16712575" href="/api/space/nsas/eline-ptp/service-management/service-orders/16712575" key="16712575"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/15826962" href="/api/space/nsas/customer-management/customers/15826962" key="15826962">
                    <CustomerName>ITB-Institute of Technology Blanchardstown</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="17268782" uri="/api/space/nsas/eline-ptp/service-management/services/17268782" href="/api/space/nsas/eline-ptp/service-management/services/17268782">
            <Common>
                <Name>qqi.gn-kp.1493882721</Name>
                <Identity>17268782</Identity>
                <State>Deployed</State>
                <Comments>QQI - Denzille Lane GN VLAN 82</Comments>
                <CreatedDate>2017-05-05T13:21:07.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-05-05T13:21:07.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Up</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>Up</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/17268771" href="/api/space/nsas/eline-ptp/service-management/service-orders/17268771" key="17268771"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/14778530" href="/api/space/nsas/customer-management/customers/14778530" key="14778530">
                    <CustomerName>QQI-Quality and Qualifications Ireland</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="17268806" uri="/api/space/nsas/eline-ptp/service-management/services/17268806" href="/api/space/nsas/eline-ptp/service-management/services/17268806">
            <Common>
                <Name>qqi.gn-kp.1493883303</Name>
                <Identity>17268806</Identity>
                <State>Deployed</State>
                <Comments>QQI Denzille Lane - GN VLAN 83</Comments>
                <CreatedDate>2017-05-05T13:20:27.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-05-05T13:20:27.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Up</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>Up</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/17268795" href="/api/space/nsas/eline-ptp/service-management/service-orders/17268795" key="17268795"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/14778530" href="/api/space/nsas/customer-management/customers/14778530" key="14778530">
                    <CustomerName>QQI-Quality and Qualifications Ireland</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="17268865" uri="/api/space/nsas/eline-ptp/service-management/services/17268865" href="/api/space/nsas/eline-ptp/service-management/services/17268865">
            <Common>
                <Name>Phase3-Traffic-Test</Name>
                <Identity>17268865</Identity>
                <State>Deployed</State>
                <Comments>10Gb/s link to allow traffic testing on the Phase 3 ring</Comments>
                <CreatedDate>2017-05-29T17:03:54.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-05-29T17:03:54.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Up</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Down</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>Up</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/17268858" href="/api/space/nsas/eline-ptp/service-management/service-orders/17268858" key="17268858"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/950272" href="/api/space/nsas/customer-management/customers/950272" key="950272">
                    <CustomerName>TEST-Customer</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18808925" uri="/api/space/nsas/eline-ptp/service-management/services/18808925" href="/api/space/nsas/eline-ptp/service-management/services/18808925">
            <Common>
                <Name>dcu-glasnevin.dcu.1500910000</Name>
                <Identity>18808925</Identity>
                <State>Deployed</State>
                <Comments>Eline for DCU from DCU Innovation Alpha Glasnevin</Comments>
                <CreatedDate>2017-07-24T17:17:13.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-07-24T17:17:13.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>None</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18808918" href="/api/space/nsas/eline-ptp/service-management/service-orders/18808918" key="18808918"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333171" href="/api/space/nsas/customer-management/customers/19333171" key="19333171">
                    <CustomerName>DCU</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809039" uri="/api/space/nsas/eline-ptp/service-management/services/18809039" href="/api/space/nsas/eline-ptp/service-management/services/18809039">
            <Common>
                <Name>dcu-spd.dcu.1500974300</Name>
                <Identity>18809039</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for DCU to St.Patrick's #1</Comments>
                <CreatedDate>2017-07-25T13:39:09.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-07-25T13:39:09.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>None</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809032" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809032" key="18809032"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333171" href="/api/space/nsas/customer-management/customers/19333171" key="19333171">
                    <CustomerName>DCU</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809053" uri="/api/space/nsas/eline-ptp/service-management/services/18809053" href="/api/space/nsas/eline-ptp/service-management/services/18809053">
            <Common>
                <Name>dcu-spd.dcu.1500974239</Name>
                <Identity>18809053</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for DCU to St.Patrick's #2</Comments>
                <CreatedDate>2017-07-25T13:38:56.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-07-25T13:38:56.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809046" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809046" key="18809046"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333171" href="/api/space/nsas/customer-management/customers/19333171" key="19333171">
                    <CustomerName>DCU</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809093" uri="/api/space/nsas/eline-ptp/service-management/services/18809093" href="/api/space/nsas/eline-ptp/service-management/services/18809093">
            <Common>
                <Name>nuig-csc.nuig.1501158898</Name>
                <Identity>18809093</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for NUIG</Comments>
                <CreatedDate>2017-08-01T12:10:51.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-01T12:10:51.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>None</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809086" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809086" key="18809086"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809107" uri="/api/space/nsas/eline-ptp/service-management/services/18809107" href="/api/space/nsas/eline-ptp/service-management/services/18809107">
            <Common>
                <Name>nuig-neb.nuig.1501510003</Name>
                <Identity>18809107</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for NUIG</Comments>
                <CreatedDate>2017-08-02T11:40:14.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-02T11:40:14.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Down</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809100" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809100" key="18809100"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809121" uri="/api/space/nsas/eline-ptp/service-management/services/18809121" href="/api/space/nsas/eline-ptp/service-management/services/18809121">
            <Common>
                <Name>nuig-srb.nuig.1501518093</Name>
                <Identity>18809121</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for NUIG-SRB</Comments>
                <CreatedDate>2017-08-02T14:26:47.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-02T14:26:47.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809114" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809114" key="18809114"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809162" uri="/api/space/nsas/eline-ptp/service-management/services/18809162" href="/api/space/nsas/eline-ptp/service-management/services/18809162">
            <Common>
                <Name>nuig-carron.nuig.1502978348</Name>
                <Identity>18809162</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for carron to NUIG</Comments>
                <CreatedDate>2017-08-24T17:34:33.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-24T17:34:33.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809155" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809155" key="18809155"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809190" uri="/api/space/nsas/eline-ptp/service-management/services/18809190" href="/api/space/nsas/eline-ptp/service-management/services/18809190">
            <Common>
                <Name>nuig-lgh.nuig.1502807754</Name>
                <Identity>18809190</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for lgh to NUIG</Comments>
                <CreatedDate>2017-08-25T11:41:31.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-25T11:41:31.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809183" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809183" key="18809183"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809216" uri="/api/space/nsas/eline-ptp/service-management/services/18809216" href="/api/space/nsas/eline-ptp/service-management/services/18809216">
            <Common>
                <Name>lyit-killybegs.lyit.1502983595</Name>
                <Identity>18809216</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for killybegs to lyit</Comments>
                <CreatedDate>2017-08-25T13:28:22.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-25T13:28:22.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809209" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809209" key="18809209"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645023" href="/api/space/nsas/customer-management/customers/18645023" key="18645023">
                    <CustomerName>LYIT</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809295" uri="/api/space/nsas/eline-ptp/service-management/services/18809295" href="/api/space/nsas/eline-ptp/service-management/services/18809295">
            <Common>
                <Name>TEST-KG</Name>
                <Identity>18809295</Identity>
                <State>DeploymentPending</State>
                <Comments>TEst</Comments>
                <CreatedDate>2017-09-15T10:10:46.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-09-15T10:10:46.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>None</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809288" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809288" key="18809288"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16711680" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16711680" key="16711680">
                        <ServiceDefinitionName>HEAnet-Eline-Untagg-UNI</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/950272" href="/api/space/nsas/customer-management/customers/950272" key="950272">
                    <CustomerName>TEST-Customer</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809315" uri="/api/space/nsas/eline-ptp/service-management/services/18809315" href="/api/space/nsas/eline-ptp/service-management/services/18809315">
            <Common>
                <Name>dkit.kp.1504616825</Name>
                <Identity>18809315</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for GN</Comments>
                <CreatedDate>2017-09-20T16:30:30.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-09-21T08:49:51.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809304" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809304" key="18809304"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645020" href="/api/space/nsas/customer-management/customers/18645020" key="18645020">
                    <CustomerName>DKIT</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809337" uri="/api/space/nsas/eline-ptp/service-management/services/18809337" href="/api/space/nsas/eline-ptp/service-management/services/18809337">
            <Common>
                <Name>dkit.kp.1504616830</Name>
                <Identity>18809337</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for GN</Comments>
                <CreatedDate>2017-09-20T16:30:09.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-09-21T10:34:03.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809326" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809326" key="18809326"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645020" href="/api/space/nsas/customer-management/customers/18645020" key="18645020">
                    <CustomerName>DKIT</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809359" uri="/api/space/nsas/eline-ptp/service-management/services/18809359" href="/api/space/nsas/eline-ptp/service-management/services/18809359">
            <Common>
                <Name>dkit.kp.1504616840</Name>
                <Identity>18809359</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for GN</Comments>
                <CreatedDate>2017-09-20T16:29:24.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-09-21T10:34:32.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809348" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809348" key="18809348"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645020" href="/api/space/nsas/customer-management/customers/18645020" key="18645020">
                    <CustomerName>DKIT</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="18809646" uri="/api/space/nsas/eline-ptp/service-management/services/18809646" href="/api/space/nsas/eline-ptp/service-management/services/18809646">
            <Common>
                <Name>dun1.pw.1504619216</Name>
                <Identity>18809646</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for OrangeNET Parkwest</Comments>
                <CreatedDate>2017-10-03T16:27:45.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-10-03T16:27:45.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Down</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/18809635" href="/api/space/nsas/eline-ptp/service-management/service-orders/18809635" key="18809635"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333173" href="/api/space/nsas/customer-management/customers/19333173" key="19333173">
                    <CustomerName>HEANET</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464236" uri="/api/space/nsas/eline-ptp/service-management/services/19464236" href="/api/space/nsas/eline-ptp/service-management/services/19464236">
            <Common>
                <Name>tcd-lofar.cwt.1499432682</Name>
                <Identity>19464236</Identity>
                <State>Deployed</State>
                <Comments>I-Lofar 10G circuit to Groningen via GEANT and Surfnet</Comments>
                <CreatedDate>2017-07-07T14:07:49.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-07-07T14:07:49.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464229" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464229" key="19464229"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333138" href="/api/space/nsas/customer-management/customers/19333138" key="19333138">
                    <CustomerName>TCD</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464300" uri="/api/space/nsas/eline-ptp/service-management/services/19464300" href="/api/space/nsas/eline-ptp/service-management/services/19464300">
            <Common>
                <Name>dcu-tonyryan.dcu.1501062210</Name>
                <Identity>19464300</Identity>
                <State>Deployed</State>
                <Comments>Eline for DCU from DCU Tony Ryan Citywest</Comments>
                <CreatedDate>2017-07-27T11:59:57.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-07-27T11:59:57.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464293" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464293" key="19464293"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333171" href="/api/space/nsas/customer-management/customers/19333171" key="19333171">
                    <CustomerName>DCU</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464314" uri="/api/space/nsas/eline-ptp/service-management/services/19464314" href="/api/space/nsas/eline-ptp/service-management/services/19464314">
            <Common>
                <Name>ucd-olhsc.ucd.1501172495</Name>
                <Identity>19464314</Identity>
                <State>Deployed</State>
                <Comments>Eline for UCD from OLHSC Crumlin</Comments>
                <CreatedDate>2017-07-31T12:58:27.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-07-31T12:58:27.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464307" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464307" key="19464307"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645011" href="/api/space/nsas/customer-management/customers/18645011" key="18645011">
                    <CustomerName>UCD</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464374" uri="/api/space/nsas/eline-ptp/service-management/services/19464374" href="/api/space/nsas/eline-ptp/service-management/services/19464374">
            <Common>
                <Name>allhallows.dcu.1499864222</Name>
                <Identity>19464374</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for DCU</Comments>
                <CreatedDate>2017-08-09T18:48:12.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-09T18:48:12.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Down</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464367" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464367" key="19464367"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333171" href="/api/space/nsas/customer-management/customers/19333171" key="19333171">
                    <CustomerName>DCU</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464400" uri="/api/space/nsas/eline-ptp/service-management/services/19464400" href="/api/space/nsas/eline-ptp/service-management/services/19464400">
            <Common>
                <Name>allhallows.dcu.1499864111</Name>
                <Identity>19464400</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for DCU</Comments>
                <CreatedDate>2017-08-09T18:51:02.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-09T18:51:02.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Down</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464393" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464393" key="19464393"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333171" href="/api/space/nsas/customer-management/customers/19333171" key="19333171">
                    <CustomerName>DCU</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464426" uri="/api/space/nsas/eline-ptp/service-management/services/19464426" href="/api/space/nsas/eline-ptp/service-management/services/19464426">
            <Common>
                <Name>nuig-carna.nuig.1503065256</Name>
                <Identity>19464426</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for Carna to NUIG</Comments>
                <CreatedDate>2017-08-22T12:25:05.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-22T12:25:05.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464419" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464419" key="19464419"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464442" uri="/api/space/nsas/eline-ptp/service-management/services/19464442" href="/api/space/nsas/eline-ptp/service-management/services/19464442">
            <Common>
                <Name>nuig-asng.nuig.1502960082</Name>
                <Identity>19464442</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for asng to NUIG</Comments>
                <CreatedDate>2017-08-22T13:08:25.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-22T13:08:25.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464435" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464435" key="19464435"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464468" uri="/api/space/nsas/eline-ptp/service-management/services/19464468" href="/api/space/nsas/eline-ptp/service-management/services/19464468">
            <Common>
                <Name>nuig-carrarow.nuig.1502961082</Name>
                <Identity>19464468</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for Carraroe to NUIG</Comments>
                <CreatedDate>2017-08-22T15:17:07.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-22T15:17:07.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464461" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464461" key="19464461"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464494" uri="/api/space/nsas/eline-ptp/service-management/services/19464494" href="/api/space/nsas/eline-ptp/service-management/services/19464494">
            <Common>
                <Name>nuig-cimru.nuig.1502965979</Name>
                <Identity>19464494</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for CIMRU to NUIG</Comments>
                <CreatedDate>2017-08-23T11:52:10.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-23T11:52:10.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464487" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464487" key="19464487"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464518" uri="/api/space/nsas/eline-ptp/service-management/services/19464518" href="/api/space/nsas/eline-ptp/service-management/services/19464518">
            <Common>
                <Name>nuig-sma.nuig.1502810314</Name>
                <Identity>19464518</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for sma to NUIG</Comments>
                <CreatedDate>2017-08-24T11:55:29.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-24T11:55:29.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464511" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464511" key="19464511"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464568" uri="/api/space/nsas/eline-ptp/service-management/services/19464568" href="/api/space/nsas/eline-ptp/service-management/services/19464568">
            <Common>
                <Name>nuig-mhars.nuig.1503910079</Name>
                <Identity>19464568</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for MHARS to NUIG</Comments>
                <CreatedDate>2017-08-30T11:53:20.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-30T11:53:20.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464561" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464561" key="19464561"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464600" uri="/api/space/nsas/eline-ptp/service-management/services/19464600" href="/api/space/nsas/eline-ptp/service-management/services/19464600">
            <Common>
                <Name>nuig-martinryan.nuig.1503909191</Name>
                <Identity>19464600</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for Martin Ryan to NUIG</Comments>
                <CreatedDate>2017-08-30T14:01:28.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-08-30T14:01:28.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Up</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>Up</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464593" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464593" key="19464593"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" href="/api/space/nsas/eline-ptp/service-management/service-definitions/9797657" key="9797657">
                        <ServiceDefinitionName>HEAnet-ELINE-untagg-UNI-NoBW</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/18645024" href="/api/space/nsas/customer-management/customers/18645024" key="18645024">
                    <CustomerName>NUIG</CustomerName>
                </Customer>
            </Reference>
        </Service>
        <Service key="19464802" uri="/api/space/nsas/eline-ptp/service-management/services/19464802" href="/api/space/nsas/eline-ptp/service-management/services/19464802">
            <Common>
                <Name>dun1.cwt.1504619204</Name>
                <Identity>19464802</Identity>
                <State>Deployed</State>
                <Comments>Eline point to point for OrangeNET Parkwest</Comments>
                <CreatedDate>2017-09-27T11:44:32.000+01:00</CreatedDate>
                <LastUpdatedDate>2017-09-27T11:44:32.000+01:00</LastUpdatedDate>
            </Common>
            <ServiceType>LDP</ServiceType>
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
            <Reference>
                <ServiceOrder uri="/api/space/nsas/eline-ptp/service-management/service-orders/19464791" href="/api/space/nsas/eline-ptp/service-management/service-orders/19464791" key="19464791"/>
                <ServiceDefinition>
                    <ServiceDefinitionID uri="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" href="/api/space/nsas/eline-ptp/service-management/service-definitions/16712375" key="16712375">
                        <ServiceDefinitionName>HEAnet-Eline-Dot1q-SingleVLAN-Translation</ServiceDefinitionName>
                    </ServiceDefinitionID>
                </ServiceDefinition>
                <Customer uri="/api/space/nsas/customer-management/customers/19333173" href="/api/space/nsas/customer-management/customers/19333173" key="19333173">
                    <CustomerName>HEANET</CustomerName>
                </Customer>
            </Reference>
        </Service>
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
            <AuditFlag>
                <FunctionalAudit>Pending</FunctionalAudit>
                <ConfigurationAudit>Pending</ConfigurationAudit>
                <FaultStatus>Up</FaultStatus>
                <SLAStatus>None</SLAStatus>
                <OverallStatus>N/A</OverallStatus>
            </AuditFlag>
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
