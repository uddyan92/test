*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bparest_variables.yaml
Suite Setup     setup-test

*** Variables ***
${testbed}  testbed.yaml
${bpa}  bpa

*** Keywords ***
setup-test
    use testbed "${testbed}"

*** Test Cases ***

Creates new device
    via BPA REST API create new Device using "${DeviceManager.create_device}" and validate creation of new device using "${DeviceManager.get_Devices_list}"

Import devices using JSON format Device details
    via BPA REST API DeviceManager import devices using JSON format Device details using "${DeviceManager.import_devices_using_json}" and list of devices "${DeviceManager.get_Devices_list}"


