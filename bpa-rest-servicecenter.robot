*** Settings ***
Library	        CXTA
Resource        cxta.robot
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
Get all service details
     via BPA REST get all service details using "${servicecenter.all_service}"

Retrieves the schema structure used for creating a service instance
     via BPA REST get all service schema details using "${servicecenter.all_service_schemas}"

Adds new parameters for service manager
     via BPA REST API add a service form service center using "${servicecenter.add}" and verify using "${servicecenter.all_service}"

Executes the commit dry run operation for the service data changes
     via BPA REST API commit a service form service center using "${servicecenter.commit_dryrun}"

Gets all the leaf references of the service
     via BPA REST API Get all the leafRefs of the service using "${ServiceCenter.leafRefs}"

Gets all the service points using NSO Instance
     via BPA REST get all service points using "${servicecenter.all_service_points_nsoInstance}"

Gets all the service instances for a service point
     via BPA REST get all service instances using "${servicecenter.all_service_instances}"

Gets the default values for a service instance when it is modified or added
     via BPA REST get default values for a service instance using "${servicecenter.default_values_service_instance}"

Syncs all the services from a given NSO Instance
     via BPA REST syncs all the services using "${servicecenter.sync_all_services}"

Retrieves the evaluated schema for services
     via BPA REST retrieve the evaluated schema for services using "${servicecenter.retrieve_evaluated_service_schema}"

Retrieves the evaluated schema for services using whenTarget
     via BPA REST retrieve the evaluated schema with whenTarget for services using "${servicecenter.retrieve_evaluated_service_schema_whenTarget}"

Execute bulk payload commit
     via BPA REST execute bulk payload commit for services using "${servicecenter.execute_bulk_payload_commit}"
