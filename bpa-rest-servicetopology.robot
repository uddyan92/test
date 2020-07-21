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
Gets a list of all directly modified services
    via BPA REST service topology get a list of all directly modified services using "${serviceTopology.get_a_list_of_all_directly_modified_services}"

Gets all the modified services
    via BPA REST service topology get all the modified services using "${serviceTopology.get_all_the_modified_services}"

Gets all the locations within the toplogy
    via BPA REST service topology get all the locations within the toplogy using "${serviceTopology.get_all_the_locations_within_the_toplogy}"
