*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***

Add Device
    Via BPA UI add a device from Selected "${deviceManager.nso}" using Device Manager "${deviceManager.add}"

View Device
    Via BPA UI view a device from Selected "${deviceManager.nso}" using Device Manager "${deviceManager.view.name}"

Edit Device
    Via BPA UI edit a device from Selected "${deviceManager.nso}" using Device Manager "${deviceManager.edit}"

Delete device in BPA
    Via BPA UI delete a device from Selected "${deviceManager.nso}" using Device Manager "${deviceManager.delete.name}"

*** Keywords ***
Testcase setup
    Start Browser    browser_name=chrome  remote_url=${REMOTE_URL}
    Login to BPA UI "${login.bpa_url}" with credentials "${login.bpa_username}" and "${login.bpa_password}"

Testcase teardown
    Logout of BPA UI
    close browser
