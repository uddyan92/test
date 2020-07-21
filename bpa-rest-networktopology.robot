*** Settings ***
Library         CXTA
Resource        cxta.robot
Resource        CxtaBPA/bpa.robot
Variables       bparest_variables.yaml
Suite Setup     setup-test

*** Variables ***
${testbed}  testbed.yaml
${bpa}  bpa

*** Keywords ***
setup-test
    use testbed "${testbed}"

*** Test Cases ***

Gets list of execution devices
    via BPA REST Network Topology Get list of execution devices using "${networktopology.get_list_of_execution_devices}"

Gets topology by filter with name and devices
    via BPA REST Network Topology Get topology by filter with name and devices using "${networktopology.get_topology_by_filter_with_name_and_devices}"
