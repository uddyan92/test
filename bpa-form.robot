*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***
Create Form Builder in BPA
    ${import_file}    Set Variable  ${CURDIR}/${formbuilder.Import.filepath}
    Via BPA UI create a form from formbuilder using json payload "${import_file}"

Edit a Form in BPA
    ${formbuilder.edit.edit_json_file_name}    Set Variable  ${CURDIR}/${formbuilder.edit.edit_json_file_name}
    Via BPA UI edit a form from formbuilder using json payload "${formbuilder.edit}"

Delete a Form in BPA
    Via BPA UI delete a form using formbuilder "${formbuilder.Delete.name}"


*** Keywords ***
Testcase setup
    Start Browser    browser_name=chrome  remote_url=${REMOTE_URL}
    Login to BPA UI "${login.bpa_url}" with credentials "${login.bpa_username}" and "${login.bpa_password}"

Testcase teardown
    Logout of BPA UI
    close browser
