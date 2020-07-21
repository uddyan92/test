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

Gets AuthGroups details
    via BPA REST DeviceManager AuthGroups Details using "${DeviceManager.get_authGroups}"

Gets all device group details
    via BPA REST DeviceManager Get all group details using "${DeviceManager.get_all_group_details}"

Gets list of all the devices
    via BPA REST DeviceManager Get list of all the devices using "${DeviceManager.get_Devices_list}"

Delete authgroups by group name
    Via BPA REST device group deletion using "${DeviceManager.delete_authgroup}" and validate using device group list "${DeviceManager.get_authGroups}"

Deletes group by name
    Via BPA REST device group deletion using "${DeviceManager.delete_group_by_name}" and validate using device group list "${DeviceManager.get_all_group_details}"

Updates auth group by name
    via BPA REST API DeviceManager Update auth group by ID using "${DeviceManager.update_auth_group_by_name}"

Updates groups by ID
    via BPA REST API DeviceManager Update groups by ID using "${DeviceManager.update_groups_by_name}"

Gets Auth Group by NSO Instance
    via BPA REST API DeviceManager add Auth Group by NSO Instance using "${DeviceManager.auth_Group_by_NSO}"

Executes the connect device action
    via BPA REST API DeviceManager Execute the connect device action using "${DeviceManager.execute_connect}"

Gets the device configuration
    via BPA REST API DeviceManager Get the device configuration using "${DeviceManager.get_device_configuration}"

Create new device group
    via BPA REST API DeviceManager Create new NsoInstance by groups using "${DeviceManager.create_new_device_group}"

Get the user map of the auth groups by the group name
    via BPA REST API DeviceManager Get the user map of the auth groups by the group id using "${DeviceManager.get_user_map}"

Creates new device
    via BPA REST API create new Device using "${DeviceManager.create_device}" and validate creation of new device using "${DeviceManager.get_Devices_list}"

#Import Devices
#    via BPA REST API DeviceManager import devices using "${DeviceManager.import_devices_file}"

Gets list of the device from all Controllers
    via BPA REST API DeviceManager Gets list of the device from all Controllers using "${DeviceManager.gets_list_of_the_device_from_all_controllers}"

Gets list of all the devices from all Controllers
    via BPA REST API DeviceManager Gets list of all the devices from all Controllers using "${DeviceManager.gets_list_of_all_devices_from_all_controllers}"

Deletes multiple devices from NSO
    via BPA REST API DeviceManager Deletes multiple devices from NSO using "${DeviceManager.deletes_multiple_devices_from_nso}" and validate using device list "${DeviceManager.get_Devices_list}"

Gets all controller names where the device name is available
    via BPA REST API DeviceManager Get all the controller names where the device name is available using "${DeviceManager.gets_all_controller_names}"

Deletes device from default controllers
    via BPA REST API DeviceManager device deletion from default controllers using "${DeviceManager.deletes_device_from_default_controllers}" and validate using device group list "${DeviceManager.get_Devices_list}"

Executes ping, connect, fetch-host-keys, check-sync, compare-config, getDeviceConfig, sync-from and sync-to Operation on a Device
    via BPA REST API DeviceManager execute an action on the device "${DeviceManager.execute_an_opertion}"

Import devices using JSON format Device details
    via BPA REST API DeviceManager import devices using JSON format Device details using "${DeviceManager.import_devices_using_json}" and list of devices "${DeviceManager.get_Devices_list}"

Device Config Paths
    via BPA REST API DeviceManager get device Config Paths using "${DeviceManager.device_config_paths}"

Gets controller details for multiple devices
    via BPA REST API DeviceManager get controller details for multiple devices using "${DeviceManager.gets_controller_details_for_multiple_devices}"

