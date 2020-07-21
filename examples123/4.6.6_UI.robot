*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Variables       ../src/CxtaBPA/BpaConstants.py
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***
4.6.6 JOB LISTING PAGE TEST 
    set browser timeout to "${BPA__MAX_WAIT_TIME}" seconds
    Wait for the loading icon to disappear    
    click on the object with XPath "${BPA_OS_UPGRADE_TILE_XPATH}"
    wait until object is clickable via XPath "${BPA_SELECT_DEVICE_LBL_TILE}"
    Wait for the loading icon to disappear
    STC upgrade select device "${osupgrade.device_name}"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__SELECT_CREATE_NEW_XPATH}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__SELECT_CREATE_NEW_XPATH}"
    Wait for the loading icon to disappear
    Create device values with active os upgrade status reset model platform "${osupgrade.create_new}"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__SELECT_OK_CONFIRMATION}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__SELECT_OK_CONFIRMATION}"

*** Keywords ***
Testcase setup
    Start Browser    browser_name=chrome  remote_url=${REMOTE_URL}
    Login to BPA UI "${login.bpa_url}" with credentials "${login.bpa_username}" and "${login.bpa_password}"

Testcase teardown
    Logout of BPA UI
    close browser
