*** Settings ***
Library         CXTA
Resource        cxta.robot
Resource        CxtaBPA/bpa.robot
Variables       bparest_variables.yaml
Suite Setup     setup-test

*** Variables ***
${testbed}  testbed.yaml
${bpa}  bpa

*** Keywords ***
setup-test
    use testbed "${testbed}"

*** Test Cases ***
Gets process template list
    via BPA REST ProcessTemplate Get the list based on template ids using "${processTemplate.get_list_based_on_template_ids}"

Gets template list by ID
    via BPA REST ProcessTemplate Get list by id using "${processTemplate.get_list_by_id}"

Pass new parameters by analytics
    via BPA REST ProcessTemplate Pass new parameters by analytics using "${processTemplate.pass_new_parameters_by_analytics}"

Execute the commands in the process template
    via BPA REST ProcessTemplate Execute the commands in the process template using "${processTemplate.execute_commands_in_processtemplate}"

Deletes analytics templates by template ID
    via BPA REST API Delete analytics templates by id using "${processTemplate.delete_analytics}" and validate using "${processTemplate.pass_new_parameters_by_analytics}"

Updates template by ID
    via BPA REST API Update template by ID using "${processTemplate.update_template}" and validate

Deletes templates by template ID
    via BPA REST API Delete Process Templates by id using "${processTemplate.delete_templates}" and validate using "${processTemplate.get_list_based_on_template_ids}"

Executes a template
    via BPA REST API Execute the analytics template using "${processTemplate.execute_analytics}"

Adds process template by NSO
    via BPA REST ProcessTemplate Add process template by NSO using "${processTemplate.add_process_template_by_NSO}"
