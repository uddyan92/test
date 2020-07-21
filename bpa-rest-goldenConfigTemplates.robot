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

Gets all golden config template list
    via BPA REST Golden Config Template get all golden config template list using "${goldenConfigTemplates.get_all_golden_config_template_list}"

Gets the details of specific template by record ID
    via BPA REST Golden Config Template get the details of specific template by record ID using "${goldenConfigTemplates.get_details_of_specific_template_by_Record_id}"

Check if template with same name exists
    via BPA REST Golden Config Template check if template with same name exists using "${goldenConfigTemplates.check_if_template_with_same_name_exists}"

Adds a template for existing device
    via BPA REST Golden Config Template add a template for existing device using "${goldenConfigTemplates.add_template_for_device}"

Adds a new golden config template
    via BPA REST Golden Config Template add a new golden config template using "${goldenConfigTemplates.add_new_golden_config_template}" and validate using "${goldenConfigTemplates.get_all_golden_config_template_list}"

Commits a dry run on NSO
    via BPA REST Golden Config Template do a commit dry run on NSO using "${goldenConfigTemplates.commit_dry_run}"

Final commit of the template on NSO
    via BPA REST Golden Config Template do a final commit of the template on NSO using "${goldenConfigTemplates.final_commit_template}"

Compares two or more golden config templates
    via BPA REST Golden Config Template compare two or more golden config templates using "${goldenConfigTemplates.compare_two_golden_templates}"

Update specific template by record ID
    via BPA REST Golden Config Template update specific template by record ID using "${goldenConfigTemplates.update_specific_golden_template}" and validate

Deletes all templates
    via BPA REST Golden Config Template delete all templates using "${goldenConfigTemplates.delete_all_golden_templates}" and validate using "${goldenConfigTemplates.get_all_golden_config_template_list}"
