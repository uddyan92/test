*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Variables       ../src/CxtaBPA/BpaConstants.py
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***
4.6.11 STC OS UPGRADE CREATE NEW JOB-EXECUTION TIME LATER-SELECT TIME
    set browser timeout to "${BPA__MAX_WAIT_TIME}" seconds
    Log to Console    "The max wait time of the browser window is 60 seconds"   
    Wait for the loading icon to disappear
    [Documentation]    Waiting to test the documentation commment visible on screen
    click on the object with XPath "${BPA_OS_UPGRADE_TILE_XPATH}"
    Log to Console    "Click the STC OS Upgrade icon  "
    wait until object is clickable via XPath "${BPA_SELECT_DEVICE_LBL_TILE}"
    Log to Console    "Wait until SELECT DEVICE label is visible"
    Wait for the loading icon to disappear
    STC upgrade select device "${osupgrade.device_name}"
    Log to Console    "The device type selected for upgrade is ASR920"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__SELECT_CREATE_NEW_XPATH}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__SELECT_CREATE_NEW_XPATH}"
    Log to Console   "Job listing page of ASR920 : Create new is clicked"
    Wait for the loading icon to disappear
    Create device values with later time "${osupgrade.create_new_later}"
    Log to Console   "Select Platform Model: 'ASR-920-24TZ-M' \n Select Device Role: 'UPE92' \n Select Release Software Version: '3.18.5SP'\n File Transfer Protocol: 'FTP' \n mdt_number: 123 \n Approval Status: 'Approved' \n mutilselect_device: 'STC-ASR920-1'"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__CREATE_NEW_SUBMIT}"
    click on the object with XPath "${BPA__CREATE_NEW_SUBMIT}"
    Log to Console    "Submit button is clicked for the JOB"
    Wait for the loading icon to disappear
    check xpath for the value message "${BPA__SELECT_TIME_VALUE}"
    Log to Console     "xpath : verified the schedule time must be greater than current time is, verified"
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
