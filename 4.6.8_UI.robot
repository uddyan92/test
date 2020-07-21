*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Variables       ../src/CxtaBPA/BpaConstants.py
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***
4.6.8 STC OS UPGRADE CREATE NEW JOB-EXECUTION TYPE PARALLE-BATCH SIZE MAX VALUE 
    set browser timeout to "${BPA__MAX_WAIT_TIME}" seconds
    Log to Console    "The max wait time of the browser window is 60 seconds"
    Wait for the loading icon to disappear    
    click on the object with XPath "${BPA_OS_UPGRADE_TILE_XPATH}"
    Log to Console     "Select STC OS upgrade tile from the dashboard"
    wait until object is clickable via XPath "${BPA_SELECT_DEVICE_LBL_TILE}"
    Wait for the loading icon to disappear
    STC upgrade select device "${osupgrade.device_name}"
    Log to Console     "The device type:ASR920 is selected from the dropdown"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__SELECT_CREATE_NEW_XPATH}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__SELECT_CREATE_NEW_XPATH}"
    Log to Console   "Job listing page of ASR920 : Create new is clicked"
    Wait for the loading icon to disappear
    Create device values with active os upgrade status device max parallel "${osupgrade.create_new}"
    Log to Console   "Select Platform Model: 'ASR-920-24TZ-M' \n Select Device Role: 'UPE92' \n Select Release Software Version: '3.18.5SP'\n File Transfer Protocol: 'FTP' \n mdt_number: 123 \n Approval Status: 'Approved' \n mutilselect_device: 'STC-ASR920-1'"
    Wait for the loading icon to disappear
    check xpath for the value message batch size max "${BPA__XPATH_BATCH_SIZE_ERROR}"
    Log to Console   "Batch max size error message verified"
    Wait for the loading icon to disappear

*** Keywords ***
Testcase setup
    Start Browser    browser_name=chrome  remote_url=${REMOTE_URL}
    Log to Console    "Opening the google chrome browser with the remote url http://selenium:4444/wd/hub "
    Login to BPA UI "${login.bpa_url}" with credentials "${login.bpa_username}" and "${login.bpa_password}"
    Log to Console    "Logging into console https://10.52.123.82/portal/#/login with the credentials admin and admin"

Testcase teardown
    Logout of BPA UI
    close browser
