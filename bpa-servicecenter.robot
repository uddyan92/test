*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Test Setup      Testcase setup
Test Teardown   Testcase teardown


*** Test Cases ***
Add Service in BPA
    Via BPA UI add a service from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${ServiceCenter.Add}"

Edit service in BPA
    ${edit_service_instance}    Set Variable  ${CURDIR}/${ServiceCenter.Edit.Edit_Json_file_Name}
    Via BPA UI Edit a service "${ServiceCenter.Edit.Name}" from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${edit_service_instance}"

Upload service center in BPA
    ${upload_service_instance}    Set Variable  ${CURDIR}/${ServiceCenter.Upload.Json_file_path}
    Via BPA UI create instance from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${upload_service_instance}"

Download Service in BPA
    Via BPA UI download a service from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${ServiceCenter.Download}"

View service in BPA
    Via BPA UI view service from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${ServiceCenter.View.Name}"

Revert service in BPA
    Via BPA UI revert service from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${ServiceCenter.Delete}"

Delete service center in BPA
    Via BPA UI delete service from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${ServiceCenter.Delete}"

Delete multiple services in BPA
    Via BPA UI delete multiple services from Selected "${ServiceCenter.NSO}" and "${ServiceCenter.ServiceList}" using Service Center "${ServiceCenter.DeleteAll}"


*** Keywords ***
Testcase setup
    Start Browser    browser_name=chrome  remote_url=${REMOTE_URL}
    Login to BPA UI "${login.bpa_url}" with credentials "${login.bpa_username}" and "${login.bpa_password}"

Testcase teardown
    Logout of BPA UI
    close browser
