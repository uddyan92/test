*** Settings ***
Library		CXTA
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***

Create Process Template
    Via BPA UI add a process template using "${ProcessTemplate.process_template.Add}"

Edit Process Template
    Via BPA UI edit a process template using "${ProcessTemplate.process_template.Edit}"

Upload Process Template
    ${import_file_upload_template}    Set Variable  ${CURDIR}/${ProcessTemplate.process_template.Upload_process_template.File_path}
    Via BPA UI upload a process template using "${import_file_upload_template}"

Download single Process Template
    Via BPA UI download single template using "${ProcessTemplate.process_template.Download_single_process_template}"

Download multiple Process template
    Via BPA UI download multiple templates using "${ProcessTemplate.process_template.Download_multiple_process_template}"

Download multiple Process Template in CSV format
    Via BPA UI download multiple templates in CSV using "${ProcessTemplate.process_template.Download_multiple_process_template_CSV}"

Download multiple Process Template in Excel format
    Via BPA UI download multiple templates in Excel using "${ProcessTemplate.process_template.Download_multiple_process_template_Excel}"

Delete multiple Process Template
    Via BPA UI delete multiple templates using "${ProcessTemplate.process_template.Delete_multiple_process_template}"

Delete single Process Template through icon
    via BPA UI single delete using icon "${ProcessTemplate.process_template.Single_delete_using_icon}" in process template

Search by name and date in Process Template
    via BPA UI search templates using "${ProcessTemplate.Search_name_date}"

Search by name in Process Template
    via BPA UI search templates using "${ProcessTemplate.Search_name}"

Filter by date in Process Template
    via BPA UI search templates using "${ProcessTemplate.Search_date}"

#Scripts
Add Script in Process Template
    ${import_file}    Set Variable  ${CURDIR}/${ProcessTemplate.Scripts.Add.template.upload.Json_file_path}
    via BPA UI add scripts using "${ProcessTemplate.Scripts.Add}" and select file "${import_file}"

Edit Scripts in Process Template
    ${import_file}    Set Variable  ${CURDIR}/${ProcessTemplate.Scripts.Single_edit.template.upload.Json_file_path}
    via BPA UI edit script using icon "${ProcessTemplate.Scripts.Single_edit}" and selete file "${import_file}"

Upload Scripts in Process Template
    ${import_file}    Set Variable  ${CURDIR}/${ProcessTemplate.Scripts.Upload.File_path}
    Via BPA UI upload a scripts using "${import_file}"

Download multiple Scripts in Process Template
    via BPA UI Download multiple scripts using "${ProcessTemplate.Scripts.Download_multiple_scripts}"

Download single Script in Process Template
    via BPA UI single script download using icon "${ProcessTemplate.Scripts.Single_download}"

Download multiple Scripts in CSV in Process Template
    via BPA UI Download multiple scripts in CSV using "${ProcessTemplate.Scripts.Download_multiple_scripts_CSV}"

Download multiple Scripts in EXCEL in Process Template
    via BPA UI Download multiple scripts in EXCEL using "${ProcessTemplate.Scripts.Download_multiple_scripts_Excel}"

Delete single Script in Process Template
    via BPA UI single script deletion using icon "${ProcessTemplate.Scripts.Single_delete}"

Delete multiple Scripts in Process Template
    via BPA UI Delete multiple scripts using "${ProcessTemplate.Scripts.Delete_multiple_scripts}"

View Scripts in Process Template
    via BPA UI view script using icon "${ProcessTemplate.Scripts.Single_view}"

#Analytics
Add Analytics in Process Template
    Via BPA UI add a process template in analytics using "${ProcessTemplate.Analytics.Add}"

Edit Analytics in Process Template
    Via BPA UI edit a process of analytics in process template using "${ProcessTemplate.Analytics.Edit}"

Download multiple Analytics in CSV in Process Template
    Via BPA UI download process of analytics in CSV using "${ProcessTemplate.Analytics.Download_multiple_CSV}"

Download multiple Analytics in Excel in Process Template
    Via BPA UI download process of analytics in Excel using "${ProcessTemplate.Analytics.Download_multiple_Excel}"

Delete Analytics in Process Template
    Via BPA UI delete a process of analytics using "${ProcessTemplate.Analytics.Delete}"

#Executions
Download Executions in CSV in Process Template
    Via BPA UI download multiple processes of Executions in CSV using "${ProcessTemplate.Executions.Download_multiple_CSV}"

Download multiple Executions in Excel in Process Template
    Via BPA UI download multiple processes of Executions in Excel using "${ProcessTemplate.Executions.Download_multiple_Excel}"

Download single Executions in Excel in Process Template
    Via BPA UI download multiple processes of Executions in Excel using "${ProcessTemplate.Executions.Download_single_Excel}"

Download single Executions in CSV in Process Template
    Via BPA UI download multiple processes of Executions in CSV using "${ProcessTemplate.Executions.Download_single_CSV}"

Download All Executions in CSV in Process Template
    Via BPA UI download all process in execution using "${ProcessTemplate.Executions.Download_All_CSV}"

Download All Executions in Excel in Process Template
    Via BPA UI download all process in execution using "${ProcessTemplate.Executions.Download_All_Excel}"

View Executions in Process Template
    Via BPA UI view in executions "${ProcessTemplate.Executions.View}"


*** Keywords ***
Testcase setup
    Start Local Browser  browser_name=chrome
    Login to BPA UI "${login.bpa_url}" with credentials "${login.bpa_username}" and "${login.bpa_password}"

Testcase teardown
    Logout of BPA UI
    close browser
