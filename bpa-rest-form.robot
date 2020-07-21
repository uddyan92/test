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
Gets a list of all the forms
     via BPA REST API get list of all forms from FormBuilder using "${formbuilder.list_all}"

Clones the form based on current selected form
     via BPA REST API clone a form in FormBuilder using "${formbuilder.clone}" and validate using "${formbuilder.list_all}"

Clone form to create an exisitng form
     Via BPA REST API clone form to create an existing form using "${formbuilder.clone_negative}" and expect error code 400

Deletes form by form name
     via BPA REST API delete a form in FormBuilder using "${formbuilder.delete_single}" and validate using "${formbuilder.list_all}"

Updates form by form name
     via BPA REST API update a form in FormBuilder using "${formbuilder.update_form}" and validate using "${formbuilder.list_all}"

Imports data from a file to create a form entity
     via BPA REST API import data from a file to create a form entity in FormBuilder using "${formbuilder.import_form}" and validate using "${formbuilder.list_all}"

Post form data and save instance of the form
     via BPA REST API post form data and save instance of the form in FormBuilder using "${formbuilder.post_form_data}" and validate using "${formbuilder.list_all}"

Retrieves form by form name
     via BPA REST API retrieve form by form name in FormBuilder using "${formbuilder.retrieve_form}"

Delete all the selected forms by form name
     via BPA REST API delete all the selected forms by form name in FormBuilder using "${formbuilder.delete_multiple}" and validate using "${formbuilder.list_all}"
