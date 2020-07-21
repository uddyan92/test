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

Gets a list of all the NED's
    via BPA REST Config validator get a list of all the NEDs using "${configValidator.get_list_of_all_NEDs}"

Executes the NED validation command
    via BPA REST Config validator execute NED validation command using "${configValidator.execute_NED_validation_command}" and validate
