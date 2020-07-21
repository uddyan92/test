*** Settings ***
Library		CXTA
Library         Collections
Resource	cxta.robot
Resource        CxtaBPA/bpa.robot
Variables	bpa_ui_variables.yaml
Test Setup      Testcase setup
Test Teardown   Testcase teardown

*** Test Cases ***
Create Workflow in BPA
    @{import_workflow_files}=    Create List
    :FOR    ${ELEMENT}    IN    @{workflow.upload.filepath}
    \    Log    ${ELEMENT}
    \    Append To List    ${import_workflow_files}   ${CURDIR}/${ELEMENT}
    Log List    ${import_workflow_files}
    Via BPA UI create workflow using file "${import_workflow_files}"

Execute Workflow in BPA
    ${workflow_instance_payload}=   Set Variable    ${CURDIR}/${workflow.execute.jsonpayload}
    Via BPA UI Execute workflow "${workflow.execute}" with version id "${workflow.execute.version}" using Instances data "${workflow_instance_payload}"

Import workflow as draft in BPA
    ${import_file}    Set Variable  ${CURDIR}/${workflow.import_as_draft.filepath}
    Via BPA UI import workflow as draft using payload "${import_file}"

Create workflow using button in BPA
    Via BPA UI create workflow in defined workflows "${workflow.create}"

Edit workflow in BPA
    Via BPA UI edit workflow using json payload "${workflow.edit}"

Download Workflow in BPA
    Via BPA UI download workflow "${workflow.download}"

Download Workflow in CSV in BPA
    Via BPA UI download defined workflow in CSV using "${workflow.download_csv}"

Download Workflow in EXCEL in BPA
    Via BPA UI download defined workflow in Excel using "${workflow.download_excel}"

Delete Workflow in BPA
    Via BPA UI delete workflow "${workflow.delete.single}" for single version

Delete workflow with multiple version ids in BPA
    Via BPA UI delete multiple versions for workflow "${workflow.delete.multiple_versions}"

Delete a workflow for all versions in BPA
    Via BPA UI delete all versions for workflow "${workflow.delete.all_versions}"


*** Keywords ***
Testcase setup
    Start Browser    browser_name=chrome  remote_url=${REMOTE_URL}
    Login to BPA UI "${login.bpa_url}" with credentials "${login.bpa_username}" and "${login.bpa_password}"

Testcase teardown
    Logout of BPA UI
    close browser
