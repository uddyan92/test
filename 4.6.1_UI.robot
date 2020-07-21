*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Variables       ../src/CxtaBPA/BpaConstants.py
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***
4.6.1 STC OS UPGRADE JOB LISTING PAGE 
    set browser timeout to "${BPA__MAX_WAIT_TIME}" seconds
    Log to Console    "The max wait time of the browser window is 60 seconds"
    Wait for the loading icon to disappear    
    click on the object with XPath "${BPA_OS_UPGRADE_TILE_XPATH}"
    Log to Console     "Select STC OS upgrade tile from the dashboard"
    wait until object is clickable via XPath "${BPA_SELECT_DEVICE_LBL_TILE}"
    Log to Console     "Wait until object is clickable to select device type"
    Wait for the loading icon to disappear
    STC upgrade select device "${osupgrade.device_name}"
    Log to Console     "The device type:ASR920 is selected from the dropdown"
    Wait for the loading icon to disappear
    Wait until object is clickable via XPath "${BPA__START_DATE_XPATH_REPORT}"
    Log to Console     "Wait until start date of xpath is clickable"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__START_DATE_XPATH_REPORT}"
    Log to Console     "Click the start date tile"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__START_DATE_VALUE}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__START_DATE_VALUE}"
    Log to Console     "Click on the start date value,first day of current month "
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__END_DATE_XPATH_REPORT}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__END_DATE_XPATH_REPORT}"
    Log to Console      "Click the end date tile"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA__END_DATE_VALUE}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA__END_DATE_VALUE}"
    Log to console      "Click the end date value,the current day of month"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA_JOB_STATUS_XPATH}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA_JOB_STATUS_XPATH}"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA_JOB_STATUS_VALUE}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA_JOB_STATUS_VALUE}"
    Log to Console      "Select the job status value as ALL from the dropdown"
    Wait for the loading icon to disappear
    wait until object is clickable via XPath "${BPA_DOWNLOAD_REPORT_XPATH}"
    Wait for the loading icon to disappear
    click on the object with XPath "${BPA_DOWNLOAD_REPORT_XPATH}"
    Log to Console      "Click on the download report"
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
