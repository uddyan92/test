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

Gets all workflow details
    via BPA REST API Get all workflow details using "${workflow.get_all_workflow_details}"

Gets the activity instance count
    via BPA REST API Get the activity instance count using "${workflow.get_activity_instance_count}"

Gets all workflow active instances
    via BPA REST API Get all workflow active instances using "${workflow.get_all_workflow_active_instances}"

Gets a list of all the variables for each workflow
    via BPA REST API Get a list of all the variables for each workflow using "${workflow.get_list_of_variables_each_workflow}"

Gets the workflow incident count
    via BPA REST API Get the workflow incident count using "${workflow.get_workflow_incident_count}"

Gets a list of all the default workflow definitions
    via BPA REST API Get the list of process definitions using "${workflow.get_list_of_process_definitions}"

Gets the process instance count
    via BPA REST API Get the process instance count using "${workflow.get_the_process_instance_count}"

Gets a list of all the workflow instances
    via BPA REST API Get a list of all the workflow instances using "${workflow.get_list_all_workflow_instances}"

Gets the workflow task count
    via BPA REST API Get the workflow task count using "${workflow.get_workflow_task_count}"

Creates a new workflow deployment
    ${workflow.create_workflow.files}    Set Variable  ${CURDIR}/${workflow.create_workflow.files}
    via BPA REST API Create a new workflow deployment using "${workflow.create_workflow}" and validate using "${workflow.get_list_of_process_definitions}"

Creates the process instance history
    via BPA REST API Create the process instance history using "${workflow.create_process_instance_history}"

Creates the instance variable history
    via BPA REST API Create the instance variable history using "${workflow.create_instance_variable_history}"

Setup permissions for the group
    via BPA REST API Setup permissions for the group "${workflow.setup_permissions_group}"

Submits the workflow process definition form by ID
    via BPA REST API Submit the workflow process definition form using "${workflow.submit_workflow_process_definition_form_by_id}" and validate using "${workflow.get_list_of_process_definitions}"

Deletes workflow by ID
    via BPA REST API Delete workflow by ID using "${workflow.delete_workflow_by_ID}" and validate using "${workflow.get_list_of_process_definitions}"

Deletes process instance by the instance ID
    via BPA REST API Delete process instance by the instance ID using "${workflow.delete_process_instance_by_instanceID}" and validate using "${workflow.get_list_all_workflow_instances}"

Update suspended workflow process instance by instance ID
    via BPA REST API Update suspended workflow process instance by instance ID "${workflow.update_suspended_workflowprocessinstance_instanceID}"

Claims the workflow instance task
    via BPA REST API Claim the workflow instance task "${workflow.claim_workflow_instance_task}" and validate using "${workflow.get_list_of_all_assigned_tasks}"

Process instance history migration
    via BPA REST API display process instance history migration using "${workflow.process_instance_history_migration}"

Get list of all definded workflow
    via BPA REST API get list of all definded workflow using "${workflow.get_list_of_all_defined_workflow}"

Delete workflow draft details by id
    via BPA REST API delete workflow draft details by id using "${workflow.delete_workflow_draft_by_id}" and validate using "${workflow.get_list_of_all_defined_workflow}"

Get single workflow draft details by id
    via BPA REST API get single workflow draft details by id using "${workflow.get_single_worlflow_details}"

Create new workflow draft
    via BPA REST API create new workflow draft using "${workflow.create_workflow_draft}" and validate using "${workflow.get_list_of_all_defined_workflow}"

Gets form variables
    via BPA REST API gets form variables using "${workflow.gets_form_variables}"

Gets process template
    via BPA REST API gets process template using "${workflow.gets_process_template}"

Gets the XML data
    via BPA REST API gets the XML data using "${workflow.gets_xml_data}"

Restart Workflow
    via BPA REST API restart workflow using "${workflow.restart_workflow}" and validate using "${workflow.create_process_instance_history}"

Gets all process instance count
    via BPA REST API gets all process instance count using "${workflow.get_all_process_instance_count}"

Gets the list of process definitions
    via BPA REST API gets the list of process definitions using "${workflow.get_all_workflow_definitions}"

Gets element template details
    via BPA REST API gets element template details using "${workflow.get_element_template_details}"

Gets the default form object/schema for the forms corresponding to a workflow task
    via BPA REST API gets the default form object/schema for the forms corresponding to a workflow task using "${workflow.get_default_form_object_for_forms}"

Gets the default data for the forms corresponding to a workflow task
    via BPA REST API gets the default data for the forms corresponding to a workflow task using "${workflow.get_default_data_for_forms}"

Gets a workflow instance task using task ID
    via BPA REST API gets a workflow instance task using task ID using "${workflow.get_workflow_instance_task}"

Unclaims the workflow instance task
    via BPA REST API unclaims the workflow instance task using "${workflow.unclaims_workflow_instance_task}" and validate using "${workflow.list_of_unassigned_tasks}"

Gets the variables corresponding to a workflow task
    via BPA REST API gets the variables corresponding to a workflow task using "${workflow.variables_corresponding_to_workflow_task}"

Submits the workflow process definition form by key
    via BPA REST API submits the workflow process definition form by key using "${workflow.submit_workflow_process_definition_form_by_key}" and validate using "${workflow.create_process_instance_history}"

Completes the workflow instance task
    via BPA REST API complete the workflow instance task using "${workflow.complete_workflow_instance_task}"

Submits the workflow instance task form
    via BPA REST API submits the workflow instance task form using "${workflow.submit_workflow_instance_form}"

Creates element templates
    via BPA REST API creates element templates using "${workflow.create_element_templates}"

Update workflow draft details by id
    via BPA REST API update workflow draft details by id using "${workflow.update_workflow_by_id}" and validate
