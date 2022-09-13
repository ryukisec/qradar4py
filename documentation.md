# gui_app_framework

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|DELETE /gui_app_framework/admin_override|def delete_admin_override(self, *, user_id, security_profile_id, **kwargs):|text/plain|UNDOCUMENTED|
|POST /gui_app_framework/admin_override|def post_admin_override(self, *, user_id, security_profile_id, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/admin_override|def get_admin_override(self, **kwargs):|application/json|UNDOCUMENTED|
|POST /gui_app_framework/application_creation_task|def post_application_creation_task(self, *, package, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/application_creation_task|def get_application_creation_task(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /gui_app_framework/application_creation_task/{application_id}|def post_application_creation_task_by_application_id(self, application_id, *, status, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/application_creation_task/{application_id}|def get_application_creation_task_by_application_id(self, application_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /gui_app_framework/application_creation_task/{application_id}/auth|def post_application_creation_task_auth_by_application_id(self, application_id, *, authorisation, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/application_creation_task/{application_id}/auth|def get_application_creation_task_auth_by_application_id(self, application_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /gui_app_framework/application_definitions|def post_application_definitions(self, *, package, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/application_definitions|def get_application_definitions(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|PUT /gui_app_framework/application_definitions/{application_definition_id}|def put_application_definitions_by_application_definition_id(self, application_definition_id, *, package, include_stopped_application=None, fields=None, **kwargs):|application/json|STABLE|
|DELETE /gui_app_framework/application_definitions/{application_definition_id}|def delete_application_definitions_by_application_definition_id(self, application_definition_id, **kwargs):|text/plain|STABLE|
|POST /gui_app_framework/application_definitions/{application_definition_id}|def post_application_definitions_by_application_definition_id(self, application_definition_id, *, status=None, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/application_definitions/{application_definition_id}|def get_application_definitions_by_application_definition_id(self, application_definition_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /gui_app_framework/application_definitions/{application_definition_id}/tenants|def post_application_definitions_tenants_by_application_definition_id(self, application_definition_id, *, tenant_id, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /gui_app_framework/application_definitions/{application_definition_id}/tenants/{tenant_id}|def delete_application_definitions_application_definition_id_tenants_by_tenant_id(self, application_definition_id, tenant_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/application_definitions/{application_definition_id}/user_role_id|def get_application_definitions_user_role_id_by_application_definition_id(self, application_definition_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}|def delete_application_definitions_application_definition_id_user_role_id_by_user_role_id(self, application_definition_id, user_role_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}|def post_application_definitions_application_definition_id_user_role_id_by_user_role_id(self, application_definition_id, user_role_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/applications|def get_applications(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /gui_app_framework/applications|def post_applications(self, *, application_definition_id, security_profile_id=None, force_multitenancy_safe=None, fields=None, **kwargs):|application/json|STABLE|
|POST /gui_app_framework/applications/{application_id}|def post_applications_by_application_id(self, application_id, *, status=None, oauth_user_id=None, security_profile_id=None, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/applications/{application_id}|def get_applications_by_application_id(self, application_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /gui_app_framework/applications/{application_id}|def delete_applications_by_application_id(self, application_id, **kwargs):|text/plain|STABLE|
|PUT /gui_app_framework/applications/{application_id}|def put_applications_by_application_id(self, application_id, *, package, fields=None, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/migration/sourcehost|def get_migration_sourcehost(self, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/migration/status|def get_migration_status(self, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/migration/{type}/check|def get_migration_check_by_type(self, type, **kwargs):|application/json|UNDOCUMENTED|
|POST /gui_app_framework/migration/{type}/start|def post_migration_start_by_type(self, type, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/named_services|def get_named_services(self, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/named_services/{uuid}|def get_named_services_by_uuid(self, uuid, **kwargs):|application/json|STABLE|
|GET /gui_app_framework/resources|def get_resources(self, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/resources/{serviceName}|def get_resources_by_serviceName(self, serviceName, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/runtime/status|def get_runtime_status(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /gui_app_framework/runtime/{type}/enable|def post_runtime_enable_by_type(self, type, *, hostTypeParams, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/runtime/{type}/exclusions|def get_runtime_exclusions_by_type(self, type, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /gui_app_framework/runtime/{type}/exclusions|def post_runtime_exclusions_by_type(self, type, *, exclusion, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /gui_app_framework/runtime/{type}/exclusions/{uuid}|def delete_runtime_type_exclusions_by_uuid(self, type, uuid, **kwargs):|text/plain|UNDOCUMENTED|
|GET /gui_app_framework/runtime/{type}/exclusions/{uuid}|def get_runtime_type_exclusions_by_uuid(self, type, uuid, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/runtime/{type}/metrics|def get_runtime_metrics_by_type(self, type, *, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /gui_app_framework/user/applications|def get_user_applications(self, **kwargs):|application/json|UNDOCUMENTED|

# ariel

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /ariel/databases|def get_databases(self, *, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /ariel/databases/{database_name}|def get_databases_by_database_name(self, database_name, *, Range=None, fields=None, filter=None, **kwargs):|application/json|STABLE|
|GET /ariel/datanode/clusters|def get_datanode_clusters(self, *, id_type=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /ariel/datanode/clusters/{id}|def get_datanode_clusters_by_id(self, id, *, id_type=None, timeout_msec=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /ariel/datanode/nodes|def get_datanode_nodes(self, *, id_type=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /ariel/datanode/nodes/{id}|def get_datanode_nodes_by_id(self, id, *, id_type=None, timeout_msec=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /ariel/event_saved_search_groups|def get_event_saved_search_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /ariel/event_saved_search_groups/{group_id}|def get_event_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /ariel/event_saved_search_groups/{group_id}|def delete_event_saved_search_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|POST /ariel/event_saved_search_groups/{group_id}|def post_event_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/flow_saved_search_groups|def get_flow_saved_search_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /ariel/flow_saved_search_groups/{group_id}|def delete_flow_saved_search_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|GET /ariel/flow_saved_search_groups/{group_id}|def get_flow_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/flow_saved_search_groups/{group_id}|def post_flow_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/flow_vlans|def post_flow_vlans(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/flow_vlans|def get_flow_vlans(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /ariel/flow_vlans/{id}|def get_flow_vlans_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /ariel/flow_vlans/{id}|def delete_flow_vlans_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /ariel/function/{function_name}|def get_function_by_function_name(self, function_name, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /ariel/functions|def get_functions(self, *, database, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/functions/{function_name}|def get_functions_by_function_name(self, function_name, *, database, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/lookups|def get_lookups(self, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/lookups|def post_lookups(self, *, data=None, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/lookups/{name}|def get_lookups_by_name(self, name, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /ariel/lookups/{name}|def delete_lookups_by_name(self, name, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/lookups/{name}|def post_lookups_by_name(self, name, *, data=None, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/parser_keywords|def get_parser_keywords(self, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/processors/aql_metadata|def post_processors_aql_metadata(self, *, query_expression, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/saved_search_delete_tasks/{task_id}|def get_saved_search_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/saved_search_dependent_tasks/{task_id}|def post_saved_search_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/saved_search_dependent_tasks/{task_id}|def get_saved_search_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/saved_search_dependent_tasks/{task_id}/results|def get_saved_search_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/saved_searches|def get_saved_searches(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /ariel/saved_searches/{id}|def delete_saved_searches_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/saved_searches/{id}|def post_saved_searches_by_id(self, id, *, saved_search, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/saved_searches/{id}|def get_saved_searches_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/saved_searches/{id}/dependents|def get_saved_searches_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/searches|def post_searches(self, *, query_expression=None, saved_search_id=None, **kwargs):|application/json|STABLE|
|GET /ariel/searches|def get_searches(self, *, db_name=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /ariel/searches/{search_id}|def post_searches_by_search_id(self, search_id, *, status=None, save_results=None, **kwargs):|application/json|STABLE|
|DELETE /ariel/searches/{search_id}|def delete_searches_by_search_id(self, search_id, **kwargs):|application/json|STABLE|
|GET /ariel/searches/{search_id}|def get_searches_by_search_id(self, search_id, *, Prefer=None, **kwargs):|application/json|STABLE|
|GET /ariel/searches/{search_id}/metadata|def get_searches_metadata_by_search_id(self, search_id, *, Range=None, fields=None, filter=None, **kwargs):|application/json|STABLE|
|GET /ariel/searches/{search_id}/results|def get_searches_results_by_search_id(self, search_id, *, Range=None, **kwargs):|application/json|STABLE|
|GET /ariel/servers|def get_servers(self, *, id_type=None, server_types=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /ariel/servers/{id}|def get_servers_by_id(self, id, *, id_type=None, timeout_msec=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /ariel/taggedfieldcategories|def get_taggedfieldcategories(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /ariel/taggedfieldcategories|def post_taggedfieldcategories(self, *, body, **kwargs):|application/json|STABLE|
|DELETE /ariel/taggedfieldcategories/{id}|def delete_taggedfieldcategories_by_id(self, id, **kwargs):|text/plain|STABLE|
|POST /ariel/taggedfieldcategories/{id}|def post_taggedfieldcategories_by_id(self, id, *, body, **kwargs):|application/json|STABLE|
|GET /ariel/taggedfieldcategories/{id}|def get_taggedfieldcategories_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/taggedfields|def post_taggedfields(self, *, body, **kwargs):|application/json|STABLE|
|GET /ariel/taggedfields|def get_taggedfields(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|GET /ariel/taggedfields/{id}|def get_taggedfields_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/taggedfields/{id}|def post_taggedfields_by_id(self, id, *, body, **kwargs):|application/json|STABLE|
|DELETE /ariel/taggedfields/{id}|def delete_taggedfields_by_id(self, id, **kwargs):|text/plain|STABLE|
|DELETE /ariel/taggedfields/{tag}|def delete_taggedfields_by_tag(self, tag, *, fields=None, **kwargs):|application/json|STABLE|
|GET /ariel/taggedfields/{tag}|def get_taggedfields_by_tag(self, tag, *, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/taggedfields/{tag}|def post_taggedfields_by_tag(self, tag, *, format_class_name=None, format_params=None, description=None, fields=None, **kwargs):|application/json|STABLE|
|POST /ariel/validators/aql|def post_validators_aql(self, *, query_expression, fields=None, **kwargs):|application/json|STABLE|

# asset_model

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /asset_model/assets|def get_assets(self, *, filter=None, fields=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /asset_model/assets/{asset_id}|def post_assets_by_asset_id(self, asset_id, *, asset, **kwargs):|text/plain|STABLE|
|POST /asset_model/configuration|def post_configuration(self, *, AssetConfiguration, fields=None, **kwargs):|application/json|STABLE|
|GET /asset_model/configuration|def get_configuration(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /asset_model/properties|def get_properties(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /asset_model/saved_search_groups|def get_saved_search_groups(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /asset_model/saved_search_groups/{group_id}|def delete_saved_search_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|POST /asset_model/saved_search_groups/{group_id}|def post_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /asset_model/saved_search_groups/{group_id}|def get_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /asset_model/saved_searches|def get_saved_searches(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /asset_model/saved_searches/{saved_search_id}|def get_saved_searches_by_saved_search_id(self, saved_search_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /asset_model/saved_searches/{saved_search_id}|def delete_saved_searches_by_saved_search_id(self, saved_search_id, **kwargs):|text/plain|STABLE|
|POST /asset_model/saved_searches/{saved_search_id}|def post_saved_searches_by_saved_search_id(self, saved_search_id, *, saved_search, fields=None, **kwargs):|application/json|STABLE|
|GET /asset_model/saved_searches/{saved_search_id}/results|def get_saved_searches_results_by_saved_search_id(self, saved_search_id, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|

# qvm

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /qvm/assets|def get_assets(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):|application/json|STABLE|
|GET /qvm/filters|def get_filters(self, **kwargs):|application/json|STABLE|
|GET /qvm/network|def get_network(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):|application/json|STABLE|
|GET /qvm/openservices|def get_openservices(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_search_groups|def get_saved_search_groups(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_search_groups/{group_id}|def get_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /qvm/saved_search_groups/{group_id}|def delete_saved_search_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|POST /qvm/saved_search_groups/{group_id}|def post_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_searches|def get_saved_searches(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_searches/vuln_instances/{task_id}/results/assets|def get_saved_searches_vuln_instances_results_assets_by_task_id(self, task_id, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_searches/vuln_instances/{task_id}/results/vuln_instances|def get_saved_searches_vuln_instances_results_vuln_instances_by_task_id(self, task_id, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_searches/vuln_instances/{task_id}/results/vulnerabilities|def get_saved_searches_vuln_instances_results_vulnerabilities_by_task_id(self, task_id, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|POST /qvm/saved_searches/vuln_instances/{task_id}/status|def post_saved_searches_vuln_instances_status_by_task_id(self, task_id, *, status=None, retention_period_in_days=None, fields=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_searches/vuln_instances/{task_id}/status|def get_saved_searches_vuln_instances_status_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /qvm/saved_searches/{saved_search_id}|def post_saved_searches_by_saved_search_id(self, saved_search_id, *, saved_search, fields=None, **kwargs):|application/json|STABLE|
|DELETE /qvm/saved_searches/{saved_search_id}|def delete_saved_searches_by_saved_search_id(self, saved_search_id, **kwargs):|text/plain|STABLE|
|GET /qvm/saved_searches/{saved_search_id}|def get_saved_searches_by_saved_search_id(self, saved_search_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /qvm/saved_searches/{saved_search_id}/vuln_instances|def get_saved_searches_vuln_instances_by_saved_search_id(self, saved_search_id, *, filter=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /qvm/savedsearches|def get_savedsearches(self, **kwargs):|application/json|STABLE|
|POST /qvm/tickets/assign|def post_tickets_assign(self, *, ticket, **kwargs):|application/json|STABLE|
|GET /qvm/vulninstances|def get_vulninstances(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):|application/json|STABLE|
|GET /qvm/vulns|def get_vulns(self, *, savedSearchId=None, savedSearchName=None, filters=None, **kwargs):|application/json|STABLE|

# staged_config

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /staged_config/access/security_profiles|def get_access_security_profiles(self, *, tenant_id=None, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /staged_config/access/security_profiles/{id}|def get_access_security_profiles_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/access/user_delete_tasks/{task_id}|def get_access_user_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/access/user_roles|def get_access_user_roles(self, *, contains=None, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /staged_config/access/user_roles/{id}|def get_access_user_roles_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/access/users|def get_access_users(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /staged_config/access/users|def post_access_users(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/access/users/{id}|def post_access_users_by_id(self, id, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/access/users/{id}|def get_access_users_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/access/users/{id}|def delete_access_users_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/access/users_with_capability_filter|def get_access_users_with_capability_filter(self, *, capabilities, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /staged_config/access_control/user_delete_tasks/{task_id}|def get_access_control_user_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /staged_config/access_control/users|def get_access_control_users(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /staged_config/access_control/users/{id}|def delete_access_control_users_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /staged_config/access_control/users/{id}|def get_access_control_users_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /staged_config/backup_and_restore/scheduled_backup_configurations|def get_backup_and_restore_scheduled_backup_configurations(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/backup_and_restore/scheduled_backup_configurations/{id}|def get_backup_and_restore_scheduled_backup_configurations_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/backup_and_restore/scheduled_backup_configurations/{id}|def post_backup_and_restore_scheduled_backup_configurations_by_id(self, id, *, backupConfiguration, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/certificates/certificate_signing_request|def post_certificates_certificate_signing_request(self, *, CSRModel, **kwargs):|text/plain|STABLE|
|GET /staged_config/certificates/certificate_signing_request|def get_certificates_certificate_signing_request(self, *, filter=None, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/certificates/certificate_signing_request/{id}|def delete_certificates_certificate_signing_request_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /staged_config/certificates/certificate_signing_request/{id}|def get_certificates_certificate_signing_request_by_id(self, id, **kwargs):|application/octet-stream|STABLE|
|POST /staged_config/certificates/end_certificates|def post_certificates_end_certificates(self, *, CertificateDTO, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/certificates/end_certificates|def get_certificates_end_certificates(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/certificates/end_certificates/{id}|def get_certificates_end_certificates_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/certificates/end_certificates/{id}|def delete_certificates_end_certificates_by_id(self, id, **kwargs):|text/plain|STABLE|
|POST /staged_config/certificates/end_certificates/{id}|def post_certificates_end_certificates_by_id(self, id, *, CertificateDTO, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/certificates/root_certificates|def post_certificates_root_certificates(self, *, certificate_content, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/certificates/root_certificates|def get_certificates_root_certificates(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/certificates/root_certificates/{id}|def delete_certificates_root_certificates_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /staged_config/certificates/root_certificates/{id}|def get_certificates_root_certificates_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/deploy_status|def post_deploy_status(self, *, deploy_status, **kwargs):|application/json|STABLE|
|GET /staged_config/deploy_status|def get_deploy_status(self, **kwargs):|application/json|STABLE|
|GET /staged_config/deployment/hosts|def get_deployment_hosts(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/deployment/hosts/{id}|def get_deployment_hosts_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/deployment/hosts/{id}/tunnels|def get_deployment_hosts_tunnels_by_id(self, id, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/deployment/hosts/{id}/tunnels/{name}|def post_deployment_hosts_id_tunnels_by_name(self, id, name, *, tunnel, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/disaster_recovery/disaster_recovery_config|def get_disaster_recovery_disaster_recovery_config(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /staged_config/disaster_recovery/disaster_recovery_config|def post_disaster_recovery_disaster_recovery_config(self, *, drConfig, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /staged_config/flow/applications/active_applications|def post_flow_applications_active_applications(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/flow/applications/active_applications|def get_flow_applications_active_applications(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):|application/json|STABLE|
|GET /staged_config/flow/applications/active_applications/{id}|def get_flow_applications_active_applications_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/flow/applications/active_applications/{id}|def post_flow_applications_active_applications_by_id(self, id, *, body, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/flow/applications/active_applications/{id}|def delete_flow_applications_active_applications_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /staged_config/remote_networks|def get_remote_networks(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /staged_config/remote_networks|def post_remote_networks(self, *, network, fields=None, **kwargs):|application/json|STABLE|
|GET /staged_config/remote_networks/{network_id}|def get_remote_networks_by_network_id(self, network_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/remote_networks/{network_id}|def post_remote_networks_by_network_id(self, network_id, *, network, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/remote_networks/{network_id}|def delete_remote_networks_by_network_id(self, network_id, **kwargs):|text/plain|STABLE|
|GET /staged_config/remote_services|def get_remote_services(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /staged_config/remote_services|def post_remote_services(self, *, service, fields=None, **kwargs):|application/json|STABLE|
|POST /staged_config/remote_services/{service_id}|def post_remote_services_by_service_id(self, service_id, *, service, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/remote_services/{service_id}|def delete_remote_services_by_service_id(self, service_id, **kwargs):|text/plain|STABLE|
|GET /staged_config/remote_services/{service_id}|def get_remote_services_by_service_id(self, service_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /staged_config/yara_rules|def delete_yara_rules(self, **kwargs):|text/plain|STABLE|
|PUT /staged_config/yara_rules|def put_yara_rules(self, *, file, **kwargs):|text/plain|STABLE|

# qni

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /qni/hosts/{host_id}/configs|def get_hosts_configs_by_host_id(self, host_id, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /qni/hosts/{host_id}/configs/{id}|def post_hosts_host_id_configs_by_id(self, host_id, id, *, qni_configuration, fields=None, **kwargs):|application/json|STABLE|
|POST /qni/stacking/stacks|def post_stacking_stacks(self, *, stack, fields=None, **kwargs):|application/json|STABLE|
|GET /qni/stacking/stacks|def get_stacking_stacks(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /qni/stacking/stacks/{stack_id}|def get_stacking_stacks_by_stack_id(self, stack_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /qni/stacking/stacks/{stack_id}|def delete_stacking_stacks_by_stack_id(self, stack_id, **kwargs):|text/plain|STABLE|
|POST /qni/stacking/stacks/{stack_id}|def post_stacking_stacks_by_stack_id(self, stack_id, *, stack, fields=None, **kwargs):|application/json|STABLE|
|GET /qni/stacking/standalone_hosts|def get_stacking_standalone_hosts(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|

# configservices

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /configservices/deployment/token|def get_deployment_token(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /configservices/host_capabilities/report|def post_host_capabilities_report(self, *, hostcapabilities, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /configservices/host_capabilities/report/{task_id}|def get_host_capabilities_report_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# config

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|POST /config/access/authorized_services|def post_access_authorized_services(self, *, authorized_service, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/authorized_services|def get_access_authorized_services(self, *, current_authorized_service=None, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/access/authorized_services/{id}|def delete_access_authorized_services_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/access/authorized_services/{id}|def get_access_authorized_services_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/access/authorized_services/{id}|def post_access_authorized_services_by_id(self, id, *, authorized_service, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/roles|def get_access_roles(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access/roles/{id}|def get_access_roles_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access/security_profiles|def get_access_security_profiles(self, *, tenant_id=None, current_security_profile=None, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/access/security_profiles/{id}|def get_access_security_profiles_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/access/staged_roles|def post_access_staged_roles(self, *, name, capabilities, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access/staged_roles|def get_access_staged_roles(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/access/staged_roles/{id}|def delete_access_staged_roles_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access/staged_roles/{id}|def get_access_staged_roles_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/access/tenant_management/tenants|def post_access_tenant_management_tenants(self, *, tenant, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/tenant_management/tenants|def get_access_tenant_management_tenants(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/access/tenant_management/tenants/{tenant_id}|def get_access_tenant_management_tenants_by_tenant_id(self, tenant_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/access/tenant_management/tenants/{tenant_id}|def delete_access_tenant_management_tenants_by_tenant_id(self, tenant_id, **kwargs):|application/json|STABLE|
|POST /config/access/tenant_management/tenants/{tenant_id}|def post_access_tenant_management_tenants_by_tenant_id(self, tenant_id, *, tenant, fields=None, **kwargs):|application/json|STABLE|
|POST /config/access/user_dependent_tasks/{task_id}|def post_access_user_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/user_dependent_tasks/{task_id}|def get_access_user_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/user_dependent_tasks/{task_id}/results|def get_access_user_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/user_roles|def get_access_user_roles(self, *, contains=None, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/access/user_roles/{id}|def get_access_user_roles_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/users|def get_access_users(self, *, current_user=None, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /config/access/users|def post_access_users(self, *, user, **kwargs):|text/plain|UNDOCUMENTED|
|POST /config/access/users/{id}|def post_access_users_by_id(self, id, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/users/{id}|def get_access_users_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/users/{id}/dependents|def get_access_users_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/access/users_with_capability_filter|def get_access_users_with_capability_filter(self, *, capabilities, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access_control/roles|def get_access_control_roles(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access_control/roles/{id}|def get_access_control_roles_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access_control/user_dependent_tasks/{task_id}|def get_access_control_user_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/access_control/user_dependent_tasks/{task_id}|def post_access_control_user_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access_control/user_dependent_tasks/{task_id}/results|def get_access_control_user_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access_control/users|def get_access_control_users(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access_control/users/{id}|def get_access_control_users_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/access_control/users/{id}/dependents|def get_access_control_users_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/backup_and_restore/scheduled_backup_configurations|def get_backup_and_restore_scheduled_backup_configurations(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/backup_and_restore/scheduled_backup_configurations/{id}|def get_backup_and_restore_scheduled_backup_configurations_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/certificates/components|def get_certificates_components(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):|application/json|STABLE|
|GET /config/certificates/end_certificates|def get_certificates_end_certificates(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|GET /config/certificates/end_certificates/{id}|def get_certificates_end_certificates_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/certificates/end_certificates/{id}/full_chain|def get_certificates_end_certificates_full_chain_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/certificates/root_certificates|def get_certificates_root_certificates(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|GET /config/certificates/root_certificates/{id}|def get_certificates_root_certificates_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/certificates/root_certificates/{id}/get_dependant_ids|def get_certificates_root_certificates_get_dependant_ids_by_id(self, id, **kwargs):|application/json|STABLE|
|POST /config/data_lake/properties|def post_data_lake_properties(self, *, data_lake_property, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/data_lake/properties|def get_data_lake_properties(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/data_lake/properties/{name}|def post_data_lake_properties_by_name(self, name, *, data_lake_property, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/data_lake/properties/{name}|def get_data_lake_properties_by_name(self, name, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/data_lake/properties/{name}|def delete_data_lake_properties_by_name(self, name, **kwargs):|text/plain|UNDOCUMENTED|
|POST /config/deploy_action|def post_deploy_action(self, *, type=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deploy_action|def get_deploy_action(self, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/components|def get_deployment_components(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/components/{id}|def get_deployment_components_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/hosts|def get_deployment_hosts(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|GET /config/deployment/hosts/{id}|def get_deployment_hosts_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/deployment/hosts/{id}|def post_deployment_hosts_by_id(self, id, *, host, fields=None, **kwargs):|application/json|STABLE|
|GET /config/deployment/hosts/{id}/capabilities|def get_deployment_hosts_capabilities_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/hosts/{id}/tunnels|def get_deployment_hosts_tunnels_by_id(self, id, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|GET /config/deployment/license_pool|def get_deployment_license_pool(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/deployment/licenses|def get_deployment_licenses(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/natgroups|def get_deployment_natgroups(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/natgroups/{id}|def get_deployment_natgroups_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/deployment/staged_components|def post_deployment_staged_components(self, *, type, hostid=None, properties=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/staged_components|def get_deployment_staged_components(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/deployment/staged_components/{id}|def delete_deployment_staged_components_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/deployment/staged_components/{id}|def post_deployment_staged_components_by_id(self, id, *, targetids=None, updated_properties=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/staged_components/{id}|def get_deployment_staged_components_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/deployment/staged_hosts|def post_deployment_staged_hosts(self, *, deploymentHost, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/staged_hosts|def get_deployment_staged_hosts(self, *, showall=None, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/deployment/staged_hosts/{id}|def delete_deployment_staged_hosts_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/deployment/staged_hosts/{id}|def post_deployment_staged_hosts_by_id(self, id, *, deploymentHost, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/staged_hosts/{id}|def get_deployment_staged_hosts_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/staged_natgroups|def get_deployment_staged_natgroups(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/deployment/staged_natgroups|def post_deployment_staged_natgroups(self, *, name, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/staged_natgroups/{id}|def get_deployment_staged_natgroups_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/deployment/staged_natgroups/{id}|def delete_deployment_staged_natgroups_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/deployment/staged_natgroups/{id}|def post_deployment_staged_natgroups_by_id(self, id, *, name, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/deployment/summary|def get_deployment_summary(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/disaster_recovery/disaster_recovery_config|def get_disaster_recovery_disaster_recovery_config(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/domain_management/domains|def post_domain_management_domains(self, *, domain, fields=None, **kwargs):|application/json|STABLE|
|GET /config/domain_management/domains|def get_domain_management_domains(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/domain_management/domains/{domain_id}|def get_domain_management_domains_by_domain_id(self, domain_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/domain_management/domains/{domain_id}|def delete_domain_management_domains_by_domain_id(self, domain_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/domain_management/domains/{domain_id}|def post_domain_management_domains_by_domain_id(self, domain_id, *, domain, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_retention_buckets|def get_event_retention_buckets(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/event_retention_buckets/{id}|def get_event_retention_buckets_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_retention_buckets/{id}|def post_event_retention_buckets_by_id(self, id, *, retention_bucket, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_retention_buckets/{id}|def delete_event_retention_buckets_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/custom_properties/aql_properties/dep/{aql_property_id}|def get_event_sources_custom_properties_aql_properties_dep_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/custom_properties/aql_properties/{aql_property_id}|def post_event_sources_custom_properties_aql_properties_by_aql_property_id(self, aql_property_id, *, data, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_properties/{aql_property_id}|def get_event_sources_custom_properties_aql_properties_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_properties/{aql_property_id}/dependents|def get_event_sources_custom_properties_aql_properties_dependents_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_properties/{aql_property_id}/dependents/disable|def get_event_sources_custom_properties_aql_properties_dependents_disable_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_property/{aql_property_name}|def get_event_sources_custom_properties_aql_property_by_aql_property_name(self, aql_property_name, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}|def get_event_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}|def post_event_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}/results|def get_event_sources_custom_properties_aql_property_dependent_tasks_disable_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/custom_properties/aql_property_dependent_tasks/{task_id}|def post_event_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_property_dependent_tasks/{task_id}|def get_event_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/aql_property_dependent_tasks/{task_id}/results|def get_event_sources_custom_properties_aql_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/custom_properties/calculated_properties|def post_event_sources_custom_properties_calculated_properties(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_properties|def get_event_sources_custom_properties_calculated_properties(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_properties/dep/{calculated_property_id}|def get_event_sources_custom_properties_calculated_properties_dep_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}|def post_event_sources_custom_properties_calculated_properties_by_calculated_property_id(self, calculated_property_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}|def delete_event_sources_custom_properties_calculated_properties_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}|def get_event_sources_custom_properties_calculated_properties_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents|def get_event_sources_custom_properties_calculated_properties_dependents_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/change_field_type|def get_event_sources_custom_properties_calculated_properties_dependents_change_field_type_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable|def get_event_sources_custom_properties_calculated_properties_dependents_disable_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_property/{calculated_property_name}|def get_event_sources_custom_properties_calculated_property_by_calculated_property_name(self, calculated_property_name, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_property_delete_tasks/{task_id}|def get_event_sources_custom_properties_calculated_property_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}|def get_event_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}|def post_event_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}/results|def get_event_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}|def get_event_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}|def post_event_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results|def get_event_sources_custom_properties_calculated_property_dependent_tasks_disable_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}|def get_event_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}|def post_event_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results|def get_event_sources_custom_properties_calculated_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/calculated_property_operands|def get_event_sources_custom_properties_calculated_property_operands(self, *, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_aql_expressions|def post_event_sources_custom_properties_property_aql_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_aql_expressions|def get_event_sources_custom_properties_property_aql_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_aql_expressions/{expression_id}|def get_event_sources_custom_properties_property_aql_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_aql_expressions/{expression_id}|def post_event_sources_custom_properties_property_aql_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_aql_expressions/{expression_id}|def delete_event_sources_custom_properties_property_aql_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/custom_properties/property_calculated_expressions|def get_event_sources_custom_properties_property_calculated_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_calculated_expressions|def post_event_sources_custom_properties_property_calculated_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_calculated_expressions/{expression_id}|def post_event_sources_custom_properties_property_calculated_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_calculated_expressions/{expression_id}|def delete_event_sources_custom_properties_property_calculated_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/custom_properties/property_calculated_expressions/{expression_id}|def get_event_sources_custom_properties_property_calculated_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_cef_expressions|def get_event_sources_custom_properties_property_cef_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_cef_expressions|def post_event_sources_custom_properties_property_cef_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_cef_expressions/{expression_id}|def post_event_sources_custom_properties_property_cef_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_cef_expressions/{expression_id}|def get_event_sources_custom_properties_property_cef_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_cef_expressions/{expression_id}|def delete_event_sources_custom_properties_property_cef_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|POST /config/event_sources/custom_properties/property_expressions|def post_event_sources_custom_properties_property_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_expressions|def get_event_sources_custom_properties_property_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_expressions/{expression_id}|def delete_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/custom_properties/property_expressions/{expression_id}|def get_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_expressions/{expression_id}|def post_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_genericlist_expressions|def post_event_sources_custom_properties_property_genericlist_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_genericlist_expressions|def get_event_sources_custom_properties_property_genericlist_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}|def delete_event_sources_custom_properties_property_genericlist_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}|def get_event_sources_custom_properties_property_genericlist_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}|def post_event_sources_custom_properties_property_genericlist_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_json_expressions|def get_event_sources_custom_properties_property_json_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_json_expressions|def post_event_sources_custom_properties_property_json_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_json_expressions/{expression_id}|def delete_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|POST /config/event_sources/custom_properties/property_json_expressions/{expression_id}|def post_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_json_expressions/{expression_id}|def get_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_leef_expressions|def post_event_sources_custom_properties_property_leef_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_leef_expressions|def get_event_sources_custom_properties_property_leef_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_leef_expressions/{expression_id}|def post_event_sources_custom_properties_property_leef_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_leef_expressions/{expression_id}|def get_event_sources_custom_properties_property_leef_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_leef_expressions/{expression_id}|def delete_event_sources_custom_properties_property_leef_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|POST /config/event_sources/custom_properties/property_nvp_expressions|def post_event_sources_custom_properties_property_nvp_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_nvp_expressions|def get_event_sources_custom_properties_property_nvp_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/property_nvp_expressions/{expression_id}|def get_event_sources_custom_properties_property_nvp_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_nvp_expressions/{expression_id}|def post_event_sources_custom_properties_property_nvp_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_nvp_expressions/{expression_id}|def delete_event_sources_custom_properties_property_nvp_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/custom_properties/property_xml_expressions|def get_event_sources_custom_properties_property_xml_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_xml_expressions|def post_event_sources_custom_properties_property_xml_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/property_xml_expressions/{expression_id}|def delete_event_sources_custom_properties_property_xml_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/custom_properties/property_xml_expressions/{expression_id}|def get_event_sources_custom_properties_property_xml_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/property_xml_expressions/{expression_id}|def post_event_sources_custom_properties_property_xml_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_properties|def get_event_sources_custom_properties_regex_properties(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/regex_properties|def post_event_sources_custom_properties_regex_properties(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/regex_properties/{regex_property_id}|def post_event_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}|def get_event_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/custom_properties/regex_properties/{regex_property_id}|def delete_event_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents|def get_event_sources_custom_properties_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type|def get_event_sources_custom_properties_regex_properties_dependents_change_field_type_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/disable|def get_event_sources_custom_properties_regex_properties_dependents_disable_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_property_delete_tasks/{task_id}|def get_event_sources_custom_properties_regex_property_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}|def post_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}|def get_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results|def get_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}|def get_event_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}|def post_event_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results|def get_event_sources_custom_properties_regex_property_dependent_tasks_disable_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}|def post_event_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}|def get_event_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results|def get_event_sources_custom_properties_regex_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/disconnected_log_collectors|def get_event_sources_disconnected_log_collectors(self, *, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/disconnected_log_collectors|def post_event_sources_disconnected_log_collectors(self, *, disconnected_log_collector, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/disconnected_log_collectors/{id}|def get_event_sources_disconnected_log_collectors_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/disconnected_log_collectors/{id}|def post_event_sources_disconnected_log_collectors_by_id(self, id, *, log_source_data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/disconnected_log_collectors/{id}|def delete_event_sources_disconnected_log_collectors_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/event_collectors|def get_event_sources_event_collectors(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/event_collectors/{id}|def get_event_sources_event_collectors_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/generated_regexes|def post_event_sources_generated_regexes(self, *, payload, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_extensions|def post_event_sources_log_source_extensions(self, *, file, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_extensions|def get_event_sources_log_source_extensions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/log_source_extensions/{log_source_extension_id}|def post_event_sources_log_source_extensions_by_log_source_extension_id(self, log_source_extension_id, *, data=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/event_sources/log_source_extensions/{log_source_extension_id}|def delete_event_sources_log_source_extensions_by_log_source_extension_id(self, log_source_extension_id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /config/event_sources/log_source_extensions/{log_source_extension_id}|def get_event_sources_log_source_extensions_by_log_source_extension_id(self, log_source_extension_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/autodetection/autodetection_global_enabled_check|def get_event_sources_log_source_management_autodetection_autodetection_global_enabled_check(self, **kwargs):|text/plain|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/autodetection/config_records|def get_event_sources_log_source_management_autodetection_config_records(self, *, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/autodetection/config_records|def post_event_sources_log_source_management_autodetection_config_records(self, *, config_record, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/autodetection/config_records/{config_id}|def post_event_sources_log_source_management_autodetection_config_records_by_config_id(self, config_id, *, config_record, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/autodetection/config_records/{config_id}|def get_event_sources_log_source_management_autodetection_config_records_by_config_id(self, config_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_bulk_tasks/{id}|def get_event_sources_log_source_management_log_source_bulk_tasks_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_bulk_tasks/{id}|def post_event_sources_log_source_management_log_source_bulk_tasks_by_id(self, id, *, updated_log_source_bulk_task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_counter/{id}|def get_event_sources_log_source_management_log_source_counter_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/log_source_extensions|def get_event_sources_log_source_management_log_source_extensions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_extensions/{id}|def get_event_sources_log_source_management_log_source_extensions_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_groups|def get_event_sources_log_source_management_log_source_groups(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_groups|def post_event_sources_log_source_management_log_source_groups(self, *, log_source_data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_groups/{id}|def get_event_sources_log_source_management_log_source_groups_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_languages|def get_event_sources_log_source_management_log_source_languages(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_languages/{id}|def get_event_sources_log_source_management_log_source_languages_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_statistics|def post_event_sources_log_source_management_log_source_statistics(self, *, statistics=None, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_tests|def post_event_sources_log_source_management_log_source_tests(self, *, test, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/log_source_tests/{id}|def get_event_sources_log_source_management_log_source_tests_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/log_source_management/log_source_tests/{id}|def post_event_sources_log_source_management_log_source_tests_by_id(self, id, *, updated_log_source_test, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/log_source_types|def get_event_sources_log_source_management_log_source_types(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_types|def post_event_sources_log_source_management_log_source_types(self, *, log_source_data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values|def get_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values|def patch_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values(self, *, dsm_paramater_allowed_values, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}|def post_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values_by_id(self, id, *, dsm_paramater_allowed_value, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}|def get_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}|def delete_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values|def patch_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values(self, *, dsm_paramater_allowed_values, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values|def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}|def post_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_by_id(self, id, *, dsm_paramater_allowed_value, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}|def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}|def delete_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_definition|def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_definition(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters|def patch_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters(self, *, dsm_paramaters, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters|def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}|def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}|def post_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_by_id(self, id, *, dsm_paramaters, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}|def delete_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_definition|def get_event_sources_log_source_management_log_source_types_dsm_parameter_definition(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameters|def patch_event_sources_log_source_management_log_source_types_dsm_parameters(self, *, dsm_paramaters, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameters|def get_event_sources_log_source_management_log_source_types_dsm_parameters(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/log_source_types/dsm_parameters/{id}|def get_event_sources_log_source_management_log_source_types_dsm_parameters_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameters/{id}|def delete_event_sources_log_source_management_log_source_types_dsm_parameters_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|POST /config/event_sources/log_source_management/log_source_types/dsm_parameters/{id}|def post_event_sources_log_source_management_log_source_types_dsm_parameters_by_id(self, id, *, dsm_paramaters, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/event_sources/log_source_management/log_source_types/{id}|def get_event_sources_log_source_management_log_source_types_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_source_types/{id}|def post_event_sources_log_source_management_log_source_types_by_id(self, id, *, log_source_type_data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/log_source_management/log_source_types/{id}|def delete_event_sources_log_source_management_log_source_types_by_id(self, id, **kwargs):|text/plain|STABLE|
|POST /config/event_sources/log_source_management/log_sources|def post_event_sources_log_source_management_log_sources(self, *, log_source_data, fields=None, **kwargs):|application/json|STABLE|
|PATCH /config/event_sources/log_source_management/log_sources|def patch_event_sources_log_source_management_log_sources(self, *, log_source_data, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/log_source_management/log_sources|def get_event_sources_log_source_management_log_sources(self, *, x-qrd-encryption-algorithm=None, x-qrd-encryption-password=None, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/log_sources/{id}|def get_event_sources_log_source_management_log_sources_by_id(self, id, *, x-qrd-encryption-algorithm=None, x-qrd-encryption-password=None, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/log_source_management/log_sources/{id}|def post_event_sources_log_source_management_log_sources_by_id(self, id, *, log_source_data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/log_source_management/log_sources/{id}|def delete_event_sources_log_source_management_log_sources_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/log_source_management/protocol_types|def get_event_sources_log_source_management_protocol_types(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/log_source_management/protocol_types/{id}|def get_event_sources_log_source_management_protocol_types_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/property_discovery_profiles|def post_event_sources_property_discovery_profiles(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/property_discovery_profiles|def get_event_sources_property_discovery_profiles(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/event_sources/property_discovery_profiles/{id}|def post_event_sources_property_discovery_profiles_by_id(self, id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/property_discovery_profiles/{id}|def get_event_sources_property_discovery_profiles_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/event_sources/property_discovery_profiles/{id}|def delete_event_sources_property_discovery_profiles_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/event_sources/wincollect/wincollect_agents|def get_event_sources_wincollect_wincollect_agents(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/wincollect/wincollect_agents/{id}|def get_event_sources_wincollect_wincollect_agents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/wincollect/wincollect_destinations|def get_event_sources_wincollect_wincollect_destinations(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/event_sources/wincollect/wincollect_destinations/{id}|def get_event_sources_wincollect_wincollect_destinations_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/extension_management/extension_export_tasks|def post_extension_management_extension_export_tasks(self, *, configData, fields=None, **kwargs):|application/json|STABLE|
|GET /config/extension_management/extension_export_tasks/{task_id}|def get_extension_management_extension_export_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/extension_management/extension_export_tasks/{task_id}/extension_export|def get_extension_management_extension_export_tasks_extension_export_by_task_id(self, task_id, **kwargs):|application/zip|STABLE|
|GET /config/extension_management/extension_export_tasks/{task_id}/results|def get_extension_management_extension_export_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/extension_management/extensions|def post_extension_management_extensions(self, *, file, fields=None, **kwargs):|application/json|STABLE|
|GET /config/extension_management/extensions|def get_extension_management_extensions(self, *, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|STABLE|
|POST /config/extension_management/extensions/{extension_id}|def post_extension_management_extensions_by_extension_id(self, extension_id, *, action_type, overwrite=None, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/extension_management/extensions/{extension_id}|def delete_extension_management_extensions_by_extension_id(self, extension_id, *, configData, fields=None, **kwargs):|application/json|STABLE|
|GET /config/extension_management/extensions/{extension_id}|def get_extension_management_extensions_by_extension_id(self, extension_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/extension_management/extensions/{extension_id}/metadata|def post_extension_management_extensions_metadata_by_extension_id(self, extension_id, *, metadata, fields=None, **kwargs):|application/json|STABLE|
|GET /config/extension_management/extensions_task_status/{status_id}|def get_extension_management_extensions_task_status_by_status_id(self, status_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/extension_management/extensions_task_status/{status_id}/results|def get_extension_management_extensions_task_status_results_by_status_id(self, status_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow/applications/active_applications|def get_flow_applications_active_applications(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):|application/json|STABLE|
|GET /config/flow/applications/active_applications/{id}|def get_flow_applications_active_applications_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow/applications/default_applications|def get_flow_applications_default_applications(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):|application/json|STABLE|
|GET /config/flow/applications/default_applications/{id}|def get_flow_applications_default_applications_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow/common_destination_ports/active_configurations|def post_flow_common_destination_ports_active_configurations(self, *, body, **kwargs):|application/json|STABLE|
|GET /config/flow/common_destination_ports/active_configurations|def get_flow_common_destination_ports_active_configurations(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):|application/json|STABLE|
|GET /config/flow/common_destination_ports/active_configurations/{id}|def get_flow_common_destination_ports_active_configurations_by_id(self, id, **kwargs):|application/json|STABLE|
|DELETE /config/flow/common_destination_ports/active_configurations/{id}|def delete_flow_common_destination_ports_active_configurations_by_id(self, id, **kwargs):|text/plain|STABLE|
|POST /config/flow/common_destination_ports/active_configurations/{id}|def post_flow_common_destination_ports_active_configurations_by_id(self, id, *, body, **kwargs):|application/json|STABLE|
|GET /config/flow/common_destination_ports/default_configurations|def get_flow_common_destination_ports_default_configurations(self, *, Range=None, filter=None, fields=None, sort=None, **kwargs):|application/json|STABLE|
|GET /config/flow/common_destination_ports/default_configurations/{id}|def get_flow_common_destination_ports_default_configurations_by_id(self, id, **kwargs):|application/json|STABLE|
|GET /config/flow_retention_buckets|def get_flow_retention_buckets(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /config/flow_retention_buckets/{id}|def delete_flow_retention_buckets_by_id(self, id, **kwargs):|text/plain|STABLE|
|POST /config/flow_retention_buckets/{id}|def post_flow_retention_buckets_by_id(self, id, *, retention_bucket, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_retention_buckets/{id}|def get_flow_retention_buckets_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/aql_properties/dep/{aql_property_id}|def get_flow_sources_custom_properties_aql_properties_dep_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_properties/{aql_property_id}|def get_flow_sources_custom_properties_aql_properties_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_properties/{aql_property_id}/dependents|def get_flow_sources_custom_properties_aql_properties_dependents_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_properties/{aql_property_id}/dependents/disable|def get_flow_sources_custom_properties_aql_properties_dependents_disable_by_aql_property_id(self, aql_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_property/{aql_property_name}|def get_flow_sources_custom_properties_aql_property_by_aql_property_name(self, aql_property_name, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}|def post_flow_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}|def get_flow_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}/results|def get_flow_sources_custom_properties_aql_property_dependent_tasks_disable_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}|def get_flow_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}|def post_flow_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}/results|def get_flow_sources_custom_properties_aql_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/calculated_properties|def get_flow_sources_custom_properties_calculated_properties(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/calculated_properties|def post_flow_sources_custom_properties_calculated_properties(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_properties/dep/{calculated_property_id}|def get_flow_sources_custom_properties_calculated_properties_dep_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}|def get_flow_sources_custom_properties_calculated_properties_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}|def post_flow_sources_custom_properties_calculated_properties_by_calculated_property_id(self, calculated_property_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}|def delete_flow_sources_custom_properties_calculated_properties_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents|def get_flow_sources_custom_properties_calculated_properties_dependents_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/change_field_type|def get_flow_sources_custom_properties_calculated_properties_dependents_change_field_type_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable|def get_flow_sources_custom_properties_calculated_properties_dependents_disable_by_calculated_property_id(self, calculated_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_property/{calculated_property_name}|def get_flow_sources_custom_properties_calculated_property_by_calculated_property_name(self, calculated_property_name, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_property_delete_tasks/{task_id}|def get_flow_sources_custom_properties_calculated_property_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}|def post_flow_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}|def get_flow_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}/results|def get_flow_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}|def get_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}|def post_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results|def get_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}|def get_flow_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}|def post_flow_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results|def get_flow_sources_custom_properties_calculated_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/calculated_property_operands|def get_flow_sources_custom_properties_calculated_property_operands(self, *, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/property_expressions|def post_flow_sources_custom_properties_property_expressions(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/property_expressions|def get_flow_sources_custom_properties_property_expressions(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|DELETE /config/flow_sources/custom_properties/property_expressions/{expression_id}|def delete_flow_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, **kwargs):|text/plain|STABLE|
|GET /config/flow_sources/custom_properties/property_expressions/{expression_id}|def get_flow_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/property_expressions/{expression_id}|def post_flow_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_properties|def get_flow_sources_custom_properties_regex_properties(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/regex_properties|def post_flow_sources_custom_properties_regex_properties(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/flow_sources/custom_properties/regex_properties/{regex_property_id}|def delete_flow_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/regex_properties/{regex_property_id}|def post_flow_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}|def get_flow_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents|def get_flow_sources_custom_properties_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type|def get_flow_sources_custom_properties_regex_properties_dependents_change_field_type_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}/disabling_dependents|def get_flow_sources_custom_properties_regex_properties_disabling_dependents_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_property_delete_tasks/{task_id}|def get_flow_sources_custom_properties_regex_property_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}|def get_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}|def post_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results|def get_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}|def get_flow_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}|def post_flow_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results|def get_flow_sources_custom_properties_regex_property_dependent_tasks_disable_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}|def post_flow_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}|def get_flow_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results|def get_flow_sources_custom_properties_regex_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/log_sources/log_source_group_delete_tasks/{task_id}|def get_log_sources_log_source_group_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/log_sources/log_source_group_dependent_tasks/{task_id}|def post_log_sources_log_source_group_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/log_sources/log_source_group_dependent_tasks/{task_id}|def get_log_sources_log_source_group_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/log_sources/log_source_group_dependent_tasks/{task_id}/results|def get_log_sources_log_source_group_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/log_sources/log_source_groups|def get_log_sources_log_source_groups(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/log_sources/log_source_groups|def post_log_sources_log_source_groups(self, *, log_source_group, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/log_sources/log_source_groups/{group_id}|def delete_log_sources_log_source_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/log_sources/log_source_groups/{group_id}|def get_log_sources_log_source_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/log_sources/log_source_groups/{group_id}|def post_log_sources_log_source_groups_by_group_id(self, group_id, *, log_source_group, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/log_sources/log_source_groups/{group_id}/dependents|def get_log_sources_log_source_groups_dependents_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/network_hierarchy/networks|def get_network_hierarchy_networks(self, *, fields=None, **kwargs):|application/json|STABLE|
|PUT /config/network_hierarchy/staged_networks|def put_network_hierarchy_staged_networks(self, *, network_hierarchy, fields=None, **kwargs):|application/json|STABLE|
|GET /config/network_hierarchy/staged_networks|def get_network_hierarchy_staged_networks(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/remote_networks|def get_remote_networks(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/remote_networks/{network_id}|def get_remote_networks_by_network_id(self, network_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/remote_services|def get_remote_services(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/remote_services/{service_id}|def get_remote_services_by_service_id(self, service_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/resilient/connections|def get_resilient_connections(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/resilient/connections|def post_resilient_connections(self, *, resilientConnection, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/resilient/connections/{id}|def delete_resilient_connections_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|POST /config/resilient/connections/{id}|def post_resilient_connections_by_id(self, id, *, resilientConnection, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/resilient/connections/{id}|def get_resilient_connections_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/resilient/destinations|def get_resilient_destinations(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/resilient/destinations|def post_resilient_destinations(self, *, resilientDestination, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/resilient/destinations/{id}|def delete_resilient_destinations_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /config/resilient/destinations/{id}|def get_resilient_destinations_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/resilient/destinations/{id}|def post_resilient_destinations_by_id(self, id, *, resilientDestination, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/resilient/test|def post_resilient_test(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/resilient/test/{task_id}|def get_resilient_test_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /config/resource_restriction/users_by_tenant/{tenant_id}|def get_resource_restriction_users_by_tenant_by_tenant_id(self, tenant_id, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/resource_restrictions|def get_resource_restrictions(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /config/resource_restrictions|def post_resource_restrictions(self, *, resourceRestriction, fields=None, **kwargs):|application/json|STABLE|
|PUT /config/resource_restrictions/{resource_restriction_id}|def put_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, *, resourceRestriction, fields=None, **kwargs):|application/json|STABLE|
|GET /config/resource_restrictions/{resource_restriction_id}|def get_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/resource_restrictions/{resource_restriction_id}|def delete_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, **kwargs):|text/plain|STABLE|
|POST /config/selective_forwarding/destinations|def post_selective_forwarding_destinations(self, *, data, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/selective_forwarding/destinations|def get_selective_forwarding_destinations(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/selective_forwarding/destinations/{id}|def post_selective_forwarding_destinations_by_id(self, id, *, data, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/selective_forwarding/destinations/{id}|def delete_selective_forwarding_destinations_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /config/selective_forwarding/destinations/{id}|def get_selective_forwarding_destinations_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/selective_forwarding/routes|def post_selective_forwarding_routes(self, *, data, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/selective_forwarding/routes|def get_selective_forwarding_routes(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /config/selective_forwarding/routes/{id}|def post_selective_forwarding_routes_by_id(self, id, *, data, **kwargs):|application/json|UNDOCUMENTED|
|GET /config/selective_forwarding/routes/{id}|def get_selective_forwarding_routes_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /config/selective_forwarding/routes/{id}|def delete_selective_forwarding_routes_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /config/store_and_forward/policies|def get_store_and_forward_policies(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /config/store_and_forward/policies/{id}|def get_store_and_forward_policies_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /config/store_and_forward/policies/{id}|def post_store_and_forward_policies_by_id(self, id, *, policy, fields=None, **kwargs):|application/json|STABLE|
|DELETE /config/store_and_forward/policies/{id}|def delete_store_and_forward_policies_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /config/vpn/client_configuration|def get_vpn_client_configuration(self, **kwargs):|application/zip|UNDOCUMENTED|
|GET /config/vpn/client_configurations|def get_vpn_client_configurations(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# support

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /support/log_bundles|def get_log_bundles(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /support/log_bundles|def post_log_bundles(self, *, get_logs_args, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /support/log_bundles/{log_bundle_id}|def get_log_bundles_by_log_bundle_id(self, log_bundle_id, *, is_initial_id=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /support/log_bundles/{log_bundle_id}|def post_log_bundles_by_log_bundle_id(self, log_bundle_id, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /support/log_bundles/{log_bundle_id}|def delete_log_bundles_by_log_bundle_id(self, log_bundle_id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /support/log_bundles/{log_bundle_id}/result|def get_log_bundles_result_by_log_bundle_id(self, log_bundle_id, **kwargs):|application/octet-stream|UNDOCUMENTED|

# system

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /system/about|def get_about(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /system/authorization/capabilities|def get_authorization_capabilities(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/authorization/password_policies|def get_authorization_password_policies(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /system/authorization/password_policies/{id}|def get_authorization_password_policies_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /system/authorization/password_policies/{id}|def post_authorization_password_policies_by_id(self, id, *, policy, fields=None, **kwargs):|application/json|STABLE|
|POST /system/authorization/password_validators|def post_authorization_password_validators(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|POST /system/authorization/settings|def post_authorization_settings(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /system/authorization/settings|def get_authorization_settings(self, *, fields=None, **kwargs):|application/json|STABLE|
|POST /system/email_servers|def post_email_servers(self, *, email_server_details, **kwargs):|application/json|STABLE|
|GET /system/email_servers|def get_email_servers(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /system/email_servers/{email_server_id}|def post_email_servers_by_email_server_id(self, email_server_id, *, email_server_details, **kwargs):|application/json|STABLE|
|DELETE /system/email_servers/{email_server_id}|def delete_email_servers_by_email_server_id(self, email_server_id, **kwargs):|text/plain|STABLE|
|GET /system/email_servers/{email_server_id}|def get_email_servers_by_email_server_id(self, email_server_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /system/eula_acceptances|def get_eula_acceptances(self, **kwargs):|application/json|STABLE|
|GET /system/eula_acceptances/{id}|def get_eula_acceptances_by_id(self, id, **kwargs):|application/json|STABLE|
|POST /system/eula_acceptances/{id}|def post_eula_acceptances_by_id(self, id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /system/eulas|def get_eulas(self, **kwargs):|application/json|STABLE|
|GET /system/information/encodings|def get_information_encodings(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /system/information/locales|def get_information_locales(self, *, sample_type=None, filter=None, fields=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|GET /system/notifications|def get_notifications(self, *, since=None, limit=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/notifications/{qid}|def get_notifications_by_qid(self, qid, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /system/notifications/{qid}|def delete_notifications_by_qid(self, qid, **kwargs):|text/plain|UNDOCUMENTED|
|GET /system/proxy_servers|def get_proxy_servers(self, *, Range=None, fields=None, filter=None, **kwargs):|application/json|STABLE|
|POST /system/proxy_servers|def post_proxy_servers(self, *, proxy_server_details, **kwargs):|application/json|STABLE|
|POST /system/proxy_servers/{id}|def post_proxy_servers_by_id(self, id, *, proxy_server_details, fields=None, **kwargs):|application/json|STABLE|
|DELETE /system/proxy_servers/{id}|def delete_proxy_servers_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /system/proxy_servers/{id}|def get_proxy_servers_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /system/server_connection_validator|def post_server_connection_validator(self, *, request_details, fields=None, **kwargs):|application/json|STABLE|
|GET /system/servers|def get_servers(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /system/servers/{server_id}|def post_servers_by_server_id(self, server_id, *, details, **kwargs):|application/json|STABLE|
|GET /system/servers/{server_id}|def get_servers_by_server_id(self, server_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /system/servers/{server_id}/firewall_rules|def get_servers_firewall_rules_by_server_id(self, server_id, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|PUT /system/servers/{server_id}/firewall_rules|def put_servers_firewall_rules_by_server_id(self, server_id, *, rules, **kwargs):|application/json|STABLE|
|GET /system/servers/{server_id}/network_interfaces/bonded|def get_servers_network_interfaces_bonded_by_server_id(self, server_id, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /system/servers/{server_id}/network_interfaces/bonded|def post_servers_network_interfaces_bonded_by_server_id(self, server_id, *, details, **kwargs):|application/json|STABLE|
|DELETE /system/servers/{server_id}/network_interfaces/bonded/{device_name}|def delete_servers_server_id_network_interfaces_bonded_by_device_name(self, server_id, device_name, **kwargs):|text/plain|STABLE|
|POST /system/servers/{server_id}/network_interfaces/bonded/{device_name}|def post_servers_server_id_network_interfaces_bonded_by_device_name(self, server_id, device_name, *, details, **kwargs):|application/json|STABLE|
|GET /system/servers/{server_id}/network_interfaces/dag|def get_servers_network_interfaces_dag_by_server_id(self, server_id, *, Range=None, filter=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /system/servers/{server_id}/network_interfaces/dag/{device_name}|def post_servers_server_id_network_interfaces_dag_by_device_name(self, server_id, device_name, *, details, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/servers/{server_id}/network_interfaces/ethernet|def get_servers_network_interfaces_ethernet_by_server_id(self, server_id, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /system/servers/{server_id}/network_interfaces/ethernet/{device_name}|def post_servers_server_id_network_interfaces_ethernet_by_device_name(self, server_id, device_name, *, details, **kwargs):|application/json|STABLE|
|POST /system/servers/{server_id}/system_time_settings|def post_servers_system_time_settings_by_server_id(self, server_id, *, settings, fields=None, **kwargs):|application/json|STABLE|
|GET /system/servers/{server_id}/system_time_settings|def get_servers_system_time_settings_by_server_id(self, server_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /system/servers/{server_id}/timezones|def get_servers_timezones_by_server_id(self, server_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /system/summary|def get_summary(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /system/task_management/email_action|def post_task_management_email_action(self, *, task_id, email_addresses, **kwargs):|text/plain|UNDOCUMENTED|
|POST /system/task_management/internal_tasks/{id}|def post_task_management_internal_tasks_by_id(self, id, *, host_id=None, app_id=None, status_uuid=None, task_class=None, task_type=None, children_ids=None, sub_task_ids=None, task_state=None, task_name_local_info=None, message_local_info=None, progress=None, minimum=None, maximum=None, created_by=None, cancelled_by=None, created_time=None, started_time=None, modified_time=None, completed_time=None, retention=None, result_url=None, result_delete_task=None, is_cancel_requested=None, delete_task_id=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /system/task_management/subtasks|def post_task_management_subtasks(self, *, task_state, message_local_info, progress=None, minimum=None, maximum=None, created_time=None, started_time=None, modified_time=None, completed_time=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/task_management/subtasks|def get_task_management_subtasks(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/task_management/subtasks/{id}|def get_task_management_subtasks_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /system/task_management/subtasks/{id}|def post_task_management_subtasks_by_id(self, id, *, task_state=None, message_local_info=None, progress=None, minimum=None, maximum=None, created_time=None, started_time=None, modified_time=None, completed_time=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /system/task_management/subtasks/{id}|def delete_task_management_subtasks_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|POST /system/task_management/task|def post_task_management_task(self, *, app_id, task_type, task_state, task_name_local_info, message_local_info, created_by, host_id=None, status_uuid=None, children_ids=None, progress=None, minimum=None, maximum=None, cancelled_by=None, created=None, started=None, modified=None, completed=None, retention=None, result_url=None, result_delete_task=None, delete_task_id=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/task_management/task|def get_task_management_task(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/task_management/task/{id}|def get_task_management_task_by_id(self, id, *, id_type=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /system/task_management/task/{id}|def post_task_management_task_by_id(self, id, *, host_id=None, app_id=None, status_uuid=None, task_type=None, children_ids=None, task_state=None, task_name_local_info=None, message_local_info=None, progress=None, minimum=None, maximum=None, created_by=None, cancelled_by=None, created=None, started=None, modified=None, completed=None, retention=None, result_url=None, result_delete_task=None, is_cancel_requested=None, delete_task_id=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /system/task_management/task/{id}|def delete_task_management_task_by_id(self, id, *, delete_result=None, **kwargs):|text/plain|UNDOCUMENTED|
|DELETE /system/task_management/task/{id}/result|def delete_task_management_task_result_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|POST /system/task_management/task/{id}/resume_data|def post_task_management_task_resume_data_by_id(self, id, *, resume_data, **kwargs):|text/plain|UNDOCUMENTED|
|GET /system/task_management/task/{id}/resume_data|def get_task_management_task_resume_data_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|POST /system/task_management/task_id/{uuid}|def post_task_management_task_id_by_uuid(self, uuid, *, task_id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /system/task_management/task_id/{uuid}|def get_task_management_task_id_by_uuid(self, uuid, **kwargs):|text/plain|UNDOCUMENTED|
|DELETE /system/task_management/task_id/{uuid}|def delete_task_management_task_id_by_uuid(self, uuid, **kwargs):|text/plain|UNDOCUMENTED|
|POST /system/task_management/tasks|def post_task_management_tasks(self, *, app_id, task_class, task_type, task_state, task_name_local_info, message_local_info, created_by, host_id=None, status_uuid=None, children_ids=None, sub_task_ids=None, progress=None, minimum=None, maximum=None, cancelled_by=None, created_time=None, started_time=None, modified_time=None, completed_time=None, retention=None, result_url=None, result_delete_task=None, delete_task_id=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/task_management/tasks|def get_task_management_tasks(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /system/task_management/tasks/{id}|def post_task_management_tasks_by_id(self, id, *, is_cancel_requested=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /system/task_management/tasks/{id}|def get_task_management_tasks_by_id(self, id, *, id_type=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /system/task_management/tasks/{id}|def delete_task_management_tasks_by_id(self, id, *, delete_result=None, **kwargs):|text/plain|UNDOCUMENTED|
|GET /system/task_management/tasks/{id}/result|def get_task_management_tasks_result_by_id(self, id, **kwargs):|application/octet-stream|UNDOCUMENTED|
|POST /system/task_management/tasks/{id}/result|def post_task_management_tasks_result_by_id(self, id, *, result, **kwargs):|text/plain|UNDOCUMENTED|
|DELETE /system/task_management/tasks/{id}/result|def delete_task_management_tasks_result_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|

# services

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|POST /services/dig_lookups|def post_dig_lookups(self, *, IP, fields=None, **kwargs):|application/json|STABLE|
|GET /services/dig_lookups/{dig_lookup_id}|def get_dig_lookups_by_dig_lookup_id(self, dig_lookup_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /services/dns_lookups|def post_dns_lookups(self, *, IP, fields=None, **kwargs):|application/json|STABLE|
|GET /services/dns_lookups/{dns_lookup_id}|def get_dns_lookups_by_dns_lookup_id(self, dns_lookup_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /services/geolocations|def get_geolocations(self, *, fields=None, filter=None, **kwargs):|application/json|STABLE|
|POST /services/port_scans|def post_port_scans(self, *, IP, fields=None, **kwargs):|application/json|STABLE|
|GET /services/port_scans/{port_scan_id}|def get_port_scans_by_port_scan_id(self, port_scan_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /services/whois_lookups|def post_whois_lookups(self, *, IP, fields=None, **kwargs):|application/json|STABLE|
|GET /services/whois_lookups/{whois_lookup_id}|def get_whois_lookups_by_whois_lookup_id(self, whois_lookup_id, *, fields=None, **kwargs):|application/json|STABLE|

# g11n

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /g11n/locale|def get_locale(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|

# application

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|POST /application/data_ingestion/configuration|def post_data_ingestion_configuration(self, *, data, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /application/data_ingestion/custom_event_mapping|def delete_data_ingestion_custom_event_mapping(self, *, log_source_type_id=None, **kwargs):|text/plain|UNDOCUMENTED|
|POST /application/data_ingestion/custom_property_definitions|def post_data_ingestion_custom_property_definitions(self, *, data, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/event/regex_properties/{regex_property_id}|def get_data_ingestion_event_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/event/regex_properties/{regex_property_id}/dependents|def get_data_ingestion_event_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/event/regex_property_dependent_tasks/{task_id}|def get_data_ingestion_event_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /application/data_ingestion/event/regex_property_dependent_tasks/{task_id}|def post_data_ingestion_event_regex_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/event/regex_property_dependent_tasks/{task_id}/results|def get_data_ingestion_event_regex_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/flow/regex_properties/{regex_property_id}|def get_data_ingestion_flow_regex_properties_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/flow/regex_properties/{regex_property_id}/dependents|def get_data_ingestion_flow_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /application/data_ingestion/flow/regex_property_dependent_tasks/{task_id}|def post_data_ingestion_flow_regex_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/flow/regex_property_dependent_tasks/{task_id}|def get_data_ingestion_flow_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/flow/regex_property_dependent_tasks/{task_id}/results|def get_data_ingestion_flow_regex_property_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/identity_fields|def get_data_ingestion_identity_fields(self, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/keyNameMappings|def get_data_ingestion_keyNameMappings(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/mappings/{log_source_type_id}|def get_data_ingestion_mappings_by_log_source_type_id(self, log_source_type_id, *, produce_identity=None, custom_only=None, filter_text=None, override_only=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /application/data_ingestion/mappings/{log_source_type_id}|def post_data_ingestion_mappings_by_log_source_type_id(self, log_source_type_id, *, data, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /application/data_ingestion/mappings/{log_source_type_id}/{id}|def delete_data_ingestion_mappings_log_source_type_id_by_id(self, log_source_type_id, id, **kwargs):|text/plain|UNDOCUMENTED|
|PUT /application/data_ingestion/mappings/{log_source_type_id}/{id}|def put_data_ingestion_mappings_log_source_type_id_by_id(self, log_source_type_id, id, *, data, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/payloads|def get_data_ingestion_payloads(self, *, handle_id, ids, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/properties/{log_source_type_id}|def get_data_ingestion_properties_by_log_source_type_id(self, log_source_type_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/qid_records|def get_data_ingestion_qid_records(self, *, qid=None, name=None, low_level_category_id=None, high_level_category_id=None, log_source_type_id=None, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/data_ingestion/qid_records/{qid_record_id}|def get_data_ingestion_qid_records_by_qid_record_id(self, qid_record_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /application/data_ingestion/simulate|def post_data_ingestion_simulate(self, *, data, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/network_threat_analytics/hierarchical_clustering_algorithms|def get_network_threat_analytics_hierarchical_clustering_algorithms(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /application/network_threat_analytics/hierarchical_clustering_algorithms|def post_network_threat_analytics_hierarchical_clustering_algorithms(self, *, body, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /application/network_threat_analytics/hierarchical_clustering_algorithms/{id}|def post_network_threat_analytics_hierarchical_clustering_algorithms_by_id(self, id, *, body, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/network_threat_analytics/hierarchical_clustering_algorithms/{id}|def get_network_threat_analytics_hierarchical_clustering_algorithms_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /application/network_threat_analytics/hierarchical_clustering_algorithms/{id}|def delete_network_threat_analytics_hierarchical_clustering_algorithms_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /application/network_threat_analytics/hierarchical_clustering_algorithms/{id}/models|def get_network_threat_analytics_hierarchical_clustering_algorithms_models_by_id(self, id, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|PATCH /application/network_threat_analytics/hierarchical_clustering_algorithms/{id}/models|def patch_network_threat_analytics_hierarchical_clustering_algorithms_models_by_id(self, id, *, body, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /application/network_threat_analytics/hierarchical_clustering_algorithms/{id}/models/{model_index}|def get_network_threat_analytics_hierarchical_clustering_algorithms_id_models_by_model_index(self, id, model_index, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /application/network_threat_analytics/hierarchical_clustering_algorithms/{id}/models/{model_index}|def post_network_threat_analytics_hierarchical_clustering_algorithms_id_models_by_model_index(self, id, model_index, *, model, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# configuration

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /configuration/log_source_groups|def get_log_source_groups(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /configuration/log_source_groups/{id}|def get_log_source_groups_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /configuration/log_source_protocols|def get_log_source_protocols(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /configuration/log_source_types|def post_log_source_types(self, *, data, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /configuration/log_source_types|def get_log_source_types(self, *, excludeSystemTypes=None, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /configuration/log_source_types/{id}|def get_log_source_types_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /configuration/log_source_types/{id}|def post_log_source_types_by_id(self, id, *, data=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /configuration/log_sources|def get_log_sources(self, *, show_deleted=None, fields=None, Range=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /configuration/log_sources/{id}|def post_log_sources_by_id(self, id, *, data=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /configuration/log_sources/{id}|def get_log_sources_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /configuration/log_sources_health|def post_log_sources_health(self, *, host_name, token, name, arielAPIVersion=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# siem

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /siem/local_destination_addresses|def get_local_destination_addresses(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /siem/local_destination_addresses/{local_destination_address_id}|def get_local_destination_addresses_by_local_destination_address_id(self, local_destination_address_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_closing_reasons|def get_offense_closing_reasons(self, *, include_reserved=None, include_deleted=None, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /siem/offense_closing_reasons|def post_offense_closing_reasons(self, *, reason, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_closing_reasons/{closing_reason_id}|def get_offense_closing_reasons_by_closing_reason_id(self, closing_reason_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_search_delete_tasks/{task_id}|def get_offense_saved_search_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_search_dependent_tasks/{task_id}|def get_offense_saved_search_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /siem/offense_saved_search_dependent_tasks/{task_id}|def post_offense_saved_search_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_search_dependent_tasks/{task_id}/results|def get_offense_saved_search_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_search_groups|def get_offense_saved_search_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_search_groups/{group_id}|def get_offense_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /siem/offense_saved_search_groups/{group_id}|def delete_offense_saved_search_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|POST /siem/offense_saved_search_groups/{group_id}|def post_offense_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_searches|def get_offense_saved_searches(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /siem/offense_saved_searches/{id}|def delete_offense_saved_searches_by_id(self, id, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_searches/{id}|def get_offense_saved_searches_by_id(self, id, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /siem/offense_saved_searches/{id}|def post_offense_saved_searches_by_id(self, id, *, saved_search, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_saved_searches/{id}/dependents|def get_offense_saved_searches_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_types|def get_offense_types(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|GET /siem/offense_types/{offense_type_id}|def get_offense_types_by_offense_type_id(self, offense_type_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offenses|def get_offenses(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /siem/offenses/{offense_id}|def post_offenses_by_offense_id(self, offense_id, *, protected=None, follow_up=None, status=None, closing_reason_id=None, assigned_to=None, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offenses/{offense_id}|def get_offenses_by_offense_id(self, offense_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offenses/{offense_id}/assignable_actors|def get_offenses_assignable_actors_by_offense_id(self, offense_id, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /siem/offenses/{offense_id}/notes|def post_offenses_notes_by_offense_id(self, offense_id, *, note_text, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/offenses/{offense_id}/notes|def get_offenses_notes_by_offense_id(self, offense_id, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /siem/offenses/{offense_id}/notes/{note_id}|def get_offenses_offense_id_notes_by_note_id(self, offense_id, note_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /siem/remote_destination_addresses|def get_remote_destination_addresses(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /siem/source_addresses|def get_source_addresses(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /siem/source_addresses/{source_address_id}|def get_source_addresses_by_source_address_id(self, source_address_id, *, fields=None, **kwargs):|application/json|STABLE|

# reference_data

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /reference_data/map_delete_tasks/{task_id}|def get_map_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_dependent_tasks/{task_id}|def get_map_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/map_dependent_tasks/{task_id}|def post_map_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_dependent_tasks/{task_id}/results|def get_map_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/map_of_sets|def post_map_of_sets(self, *, name, element_type, key_label=None, value_label=None, timeout_type=None, time_to_live=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_of_sets|def get_map_of_sets(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data/map_of_sets/bulk_load/{namespace}/{name}/{domain_id}|def post_map_of_sets_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/map_of_sets/bulk_load/{name}|def post_map_of_sets_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/map_of_sets/{name}|def delete_map_of_sets_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/map_of_sets/{name}|def post_map_of_sets_by_name(self, name, *, key, value, namespace=None, source=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_of_sets/{name}|def get_map_of_sets_by_name(self, name, *, namespace=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_of_sets/{name}/dependents|def get_map_of_sets_dependents_by_name(self, name, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/map_of_sets/{name}/values/{key}|def delete_map_of_sets_name_values_by_key(self, name, key, *, value, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /reference_data/map_of_sets/{name}/{key}|def delete_map_of_sets_name_by_key(self, name, key, *, value, namespace=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_of_sets_delete_tasks/{task_id}|def get_map_of_sets_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/map_of_sets_dependent_tasks/{task_id}|def post_map_of_sets_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_of_sets_dependent_tasks/{task_id}|def get_map_of_sets_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/map_of_sets_dependent_tasks/{task_id}/results|def get_map_of_sets_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/maps|def post_maps(self, *, name, element_type, key_label=None, value_label=None, timeout_type=None, time_to_live=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/maps|def get_maps(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data/maps/bulk_load/{namespace}/{name}/{domain_id}|def post_maps_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/maps/bulk_load/{name}|def post_maps_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/maps/{name}|def delete_maps_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/maps/{name}|def get_maps_by_name(self, name, *, namespace=None, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data/maps/{name}|def post_maps_by_name(self, name, *, key, value, namespace=None, source=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/maps/{name}/dependents|def get_maps_dependents_by_name(self, name, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/maps/{name}/values/{key}|def delete_maps_name_values_by_key(self, name, key, *, value, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /reference_data/maps/{name}/{key}|def delete_maps_name_by_key(self, name, key, *, value, namespace=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/set_delete_tasks/{task_id}|def get_set_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/set_dependent_tasks/{task_id}|def post_set_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/set_dependent_tasks/{task_id}|def get_set_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/set_dependent_tasks/{task_id}/results|def get_set_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/sets|def get_sets(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data/sets|def post_sets(self, *, name, element_type, timeout_type=None, time_to_live=None, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/sets/bulk_load/{namespace}/{name}/{domain_id}|def post_sets_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/sets/bulk_load/{name}|def post_sets_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/sets/search|def get_sets_search(self, *, value, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /reference_data/sets/{name}|def get_sets_by_name(self, name, *, namespace=None, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data/sets/{name}|def post_sets_by_name(self, name, *, value, namespace=None, source=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/sets/{name}|def delete_sets_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/sets/{name}/dependents|def get_sets_dependents_by_name(self, name, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/sets/{name}/values/{value}|def delete_sets_name_values_by_value(self, name, value, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /reference_data/sets/{name}/{value}|def delete_sets_name_by_value(self, name, value, *, namespace=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/tables|def post_tables(self, *, name, element_type, outer_key_label=None, timeout_type=None, time_to_live=None, key_name_types=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/tables|def get_tables(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data/tables/bulk_load/{namespace}/{name}/{domain_id}|def post_tables_bulk_load_namespace_name_by_domain_id(self, namespace, name, domain_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/tables/bulk_load/{name}|def post_tables_bulk_load_by_name(self, name, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/tables/{name}|def post_tables_by_name(self, name, *, outer_key, inner_key, value, namespace=None, source=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/tables/{name}|def delete_tables_by_name(self, name, *, namespace=None, purge_only=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/tables/{name}|def get_tables_by_name(self, name, *, namespace=None, fields=None, Range=None, **kwargs):|application/json|STABLE|
|GET /reference_data/tables/{name}/dependents|def get_tables_dependents_by_name(self, name, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data/tables/{name}/values/{outer_key}/{inner_key}|def delete_tables_name_values_outer_key_by_inner_key(self, name, outer_key, inner_key, *, value, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /reference_data/tables/{name}/{outer_key}/{inner_key}|def delete_tables_name_outer_key_by_inner_key(self, name, outer_key, inner_key, *, value, namespace=None, domain_id=None, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/tables_delete_tasks/{task_id}|def get_tables_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/tables_dependent_tasks/{task_id}|def get_tables_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data/tables_dependent_tasks/{task_id}|def post_tables_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data/tables_dependent_tasks/{task_id}/results|def get_tables_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|

# analytics

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /analytics/ade_rules|def get_ade_rules(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /analytics/ade_rules/ade_rule_delete_tasks/{task_id}|def get_ade_rules_ade_rule_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/ade_rules/ade_rule_dependent_tasks/{task_id}|def get_ade_rules_ade_rule_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/ade_rules/ade_rule_dependent_tasks/{task_id}|def post_ade_rules_ade_rule_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/ade_rules/ade_rule_dependent_tasks/{task_id}/results|def get_ade_rules_ade_rule_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/ade_rules/{id}|def get_ade_rules_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/ade_rules/{id}|def post_ade_rules_by_id(self, id, *, ade_rule, fields=None, **kwargs):|application/json|STABLE|
|DELETE /analytics/ade_rules/{id}|def delete_ade_rules_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/ade_rules/{id}/dependents|def get_ade_rules_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/building_blocks|def get_building_blocks(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /analytics/building_blocks/building_block_delete_tasks/{task_id}|def get_building_blocks_building_block_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/building_blocks/building_block_dependent_tasks/{task_id}|def post_building_blocks_building_block_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/building_blocks/building_block_dependent_tasks/{task_id}|def get_building_blocks_building_block_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/building_blocks/building_block_dependent_tasks/{task_id}/results|def get_building_blocks_building_block_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/building_blocks/{id}|def get_building_blocks_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/building_blocks/{id}|def post_building_blocks_by_id(self, id, *, building_block, fields=None, **kwargs):|application/json|STABLE|
|DELETE /analytics/building_blocks/{id}|def delete_building_blocks_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/building_blocks/{id}/dependents|def get_building_blocks_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/building_blocks_with_data|def post_building_blocks_with_data(self, *, building_block, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /analytics/building_blocks_with_data|def get_building_blocks_with_data(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /analytics/building_blocks_with_data/{id}|def post_building_blocks_with_data_by_id(self, id, *, building_block, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /analytics/building_blocks_with_data/{id}|def get_building_blocks_with_data_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /analytics/custom_actions/actions|def post_custom_actions_actions(self, *, custom_action, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/custom_actions/actions|def get_custom_actions_actions(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /analytics/custom_actions/actions/{action_id}|def post_custom_actions_actions_by_action_id(self, action_id, *, custom_action, fields=None, **kwargs):|application/json|STABLE|
|DELETE /analytics/custom_actions/actions/{action_id}|def delete_custom_actions_actions_by_action_id(self, action_id, **kwargs):|text/plain|STABLE|
|GET /analytics/custom_actions/actions/{action_id}|def get_custom_actions_actions_by_action_id(self, action_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/custom_actions/interpreters|def get_custom_actions_interpreters(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /analytics/custom_actions/interpreters/{interpreter_id}|def get_custom_actions_interpreters_by_interpreter_id(self, interpreter_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/custom_actions/scripts|def post_custom_actions_scripts(self, *, file, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/custom_actions/scripts|def get_custom_actions_scripts(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /analytics/custom_actions/scripts/{script_id}|def get_custom_actions_scripts_by_script_id(self, script_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/custom_actions/scripts/{script_id}|def post_custom_actions_scripts_by_script_id(self, script_id, *, file, fields=None, **kwargs):|application/json|STABLE|
|DELETE /analytics/custom_actions/scripts/{script_id}|def delete_custom_actions_scripts_by_script_id(self, script_id, **kwargs):|text/plain|STABLE|
|POST /analytics/custom_actions/test|def post_custom_actions_test(self, *, custom_action_test_request, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /analytics/rule_groups|def get_rule_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /analytics/rule_groups/{group_id}|def get_rule_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /analytics/rule_groups/{group_id}|def delete_rule_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|POST /analytics/rule_groups/{group_id}|def post_rule_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/rules|def get_rules(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /analytics/rules/rule_delete_tasks/{task_id}|def get_rules_rule_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/rules/rule_dependent_tasks/{task_id}|def get_rules_rule_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/rules/rule_dependent_tasks/{task_id}|def post_rules_rule_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/rules/rule_dependent_tasks/{task_id}/results|def get_rules_rule_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/rules/{id}|def get_rules_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /analytics/rules/{id}|def post_rules_by_id(self, id, *, rule, fields=None, **kwargs):|application/json|STABLE|
|DELETE /analytics/rules/{id}|def delete_rules_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/rules/{id}/dependents|def get_rules_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /analytics/rules_offense_contributions|def get_rules_offense_contributions(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /analytics/rules_with_data|def post_rules_with_data(self, *, rule, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /analytics/rules_with_data|def get_rules_with_data(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /analytics/rules_with_data/{id}|def post_rules_with_data_by_id(self, id, *, rule, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /analytics/rules_with_data/{id}|def get_rules_with_data_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# reference_data_collections

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /reference_data_collections/set_bulk_update_tasks/{task_status_id}|def get_set_bulk_update_tasks_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/set_bulk_update_tasks/{task_status_id}/results|def get_set_bulk_update_tasks_results_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/set_delete_tasks/{task_status_id}|def get_set_delete_tasks_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/set_dependents_tasks/{task_status_id}|def get_set_dependents_tasks_by_task_status_id(self, task_status_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data_collections/set_dependents_tasks/{task_status_id}|def post_set_dependents_tasks_by_task_status_id(self, task_status_id, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/set_dependents_tasks/{task_status_id}/results|def get_set_dependents_tasks_results_by_task_status_id(self, task_status_id, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data_collections/set_entries|def post_set_entries(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|PATCH /reference_data_collections/set_entries|def patch_set_entries(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/set_entries|def get_set_entries(self, *, entry_type=None, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data_collections/set_entries/{id}|def delete_set_entries_by_id(self, id, **kwargs):|text/plain|STABLE|
|POST /reference_data_collections/set_entries/{id}|def post_set_entries_by_id(self, id, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/set_entries/{id}|def get_set_entries_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/sets|def get_sets(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /reference_data_collections/sets|def post_sets(self, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/sets/{id}|def get_sets_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /reference_data_collections/sets/{id}|def delete_sets_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /reference_data_collections/sets/{id}|def post_sets_by_id(self, id, *, body, fields=None, **kwargs):|application/json|STABLE|
|GET /reference_data_collections/sets/{id}/dependents|def get_sets_dependents_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|

# qrm

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /qrm/model_groups|def get_model_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /qrm/model_groups/{group_id}|def delete_model_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|POST /qrm/model_groups/{group_id}|def post_model_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /qrm/model_groups/{group_id}|def get_model_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /qrm/qrm_saved_search_groups|def get_qrm_saved_search_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /qrm/qrm_saved_search_groups/{group_id}|def delete_qrm_saved_search_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|GET /qrm/qrm_saved_search_groups/{group_id}|def get_qrm_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /qrm/qrm_saved_search_groups/{group_id}|def post_qrm_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /qrm/question_groups|def get_question_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /qrm/question_groups/{group_id}|def delete_question_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|POST /qrm/question_groups/{group_id}|def post_question_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /qrm/question_groups/{group_id}|def get_question_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /qrm/simulation_groups|def get_simulation_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /qrm/simulation_groups/{group_id}|def delete_simulation_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|
|GET /qrm/simulation_groups/{group_id}|def get_simulation_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /qrm/simulation_groups/{group_id}|def post_simulation_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|GET /qrm/topology_saved_search_groups|def get_topology_saved_search_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /qrm/topology_saved_search_groups/{group_id}|def get_topology_saved_search_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /qrm/topology_saved_search_groups/{group_id}|def post_topology_saved_search_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|STABLE|
|DELETE /qrm/topology_saved_search_groups/{group_id}|def delete_topology_saved_search_groups_by_group_id(self, group_id, **kwargs):|text/plain|STABLE|

# dashboards

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /dashboards|def get(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /dashboards/{id}|def delete_by_id(self, id, **kwargs):|text/plain|UNDOCUMENTED|
|POST /dashboards/{id}|def post_by_id(self, id, *, dashboard, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /dashboards/{id}|def get_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# dynamic_search

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|POST /dynamic_search/saved_queries|def post_saved_queries(self, *, query, **kwargs):|application/json|STABLE|
|GET /dynamic_search/saved_queries|def get_saved_queries(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /dynamic_search/saved_queries/{id}|def get_saved_queries_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /dynamic_search/saved_queries/{id}|def delete_saved_queries_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /dynamic_search/schemas|def get_schemas(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /dynamic_search/schemas/{name}|def get_schemas_by_name(self, name, *, fields=None, **kwargs):|application/json|STABLE|
|GET /dynamic_search/schemas/{name}/fields|def get_schemas_fields_by_name(self, name, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /dynamic_search/schemas/{name}/functions|def get_schemas_functions_by_name(self, name, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /dynamic_search/schemas/{name}/operators|def get_schemas_operators_by_name(self, name, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /dynamic_search/searches|def post_searches(self, *, search, **kwargs):|application/json|STABLE|
|GET /dynamic_search/searches|def get_searches(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|DELETE /dynamic_search/searches/{handle}|def delete_searches_by_handle(self, handle, **kwargs):|text/plain|STABLE|
|GET /dynamic_search/searches/{handle}|def get_searches_by_handle(self, handle, *, fields=None, **kwargs):|application/json|STABLE|
|GET /dynamic_search/searches/{handle}/results|def get_searches_results_by_handle(self, handle, *, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|

# health

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /health/alerts|def get_alerts(self, *, since=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /health/metrics/config|def get_metrics_config(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /health/metrics/config/{metric_id}|def get_metrics_config_by_metric_id(self, metric_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /health/metrics/meta|def get_metrics_meta(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /health/metrics/meta/{metric_id}|def get_metrics_meta_by_metric_id(self, metric_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /health/metrics/qradar_metrics|def get_metrics_qradar_metrics(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|POST /health/metrics/qradar_metrics/{id}|def post_metrics_qradar_metrics_by_id(self, id, *, qradar_metric, fields=None, **kwargs):|application/json|STABLE|
|GET /health/metrics/qradar_metrics/{id}|def get_metrics_qradar_metrics_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /health/metrics/qradar_metrics_global_config|def post_metrics_qradar_metrics_global_config(self, *, global_config, fields=None, **kwargs):|application/json|STABLE|
|GET /health/metrics/system_metrics|def get_metrics_system_metrics(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /health/metrics/system_metrics/{id}|def get_metrics_system_metrics_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /health/metrics/system_metrics/{id}|def post_metrics_system_metrics_by_id(self, id, *, system_metric, fields=None, **kwargs):|application/json|STABLE|
|POST /health/metrics/system_metrics_global_config|def post_metrics_system_metrics_global_config(self, *, global_config, fields=None, **kwargs):|application/json|STABLE|

# bandwidth_manager

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /bandwidth_manager/configurations|def get_configurations(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /bandwidth_manager/configurations|def post_configurations(self, *, configuration, fields=None, **kwargs):|application/json|STABLE|
|POST /bandwidth_manager/configurations/{id}|def post_configurations_by_id(self, id, *, configuration, fields=None, **kwargs):|application/json|STABLE|
|GET /bandwidth_manager/configurations/{id}|def get_configurations_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /bandwidth_manager/configurations/{id}|def delete_configurations_by_id(self, id, **kwargs):|text/plain|STABLE|
|GET /bandwidth_manager/filters|def get_filters(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|
|POST /bandwidth_manager/filters|def post_filters(self, *, class, fields=None, **kwargs):|application/json|STABLE|
|GET /bandwidth_manager/filters/{id}|def get_filters_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /bandwidth_manager/filters/{id}|def post_filters_by_id(self, id, *, filter, fields=None, **kwargs):|application/json|STABLE|
|DELETE /bandwidth_manager/filters/{id}|def delete_filters_by_id(self, id, **kwargs):|text/plain|STABLE|

# reports

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /reports/groups|def get_groups(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /reports/groups/{id}|def post_groups_by_id(self, id, *, data, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /reports/groups/{id}|def get_groups_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# usermanagement

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /usermanagement/users|def get_users(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /usermanagement/users/{username}|def get_users_by_username(self, username, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /usermanagement/users/{username}/access/cidr/{cidr}|def get_users_username_access_cidr_by_cidr(self, username, cidr, **kwargs):|text/plain|UNDOCUMENTED|
|GET /usermanagement/users/{username}/access/cidrs|def get_users_access_cidrs_by_username(self, username, *, filter=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|

# health_data

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /health_data/security_data_count|def get_security_data_count(self, *, fields=None, **kwargs):|application/json|STABLE|
|GET /health_data/top_offenses|def get_top_offenses(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|
|GET /health_data/top_rules|def get_top_rules(self, *, fields=None, filter=None, Range=None, **kwargs):|application/json|STABLE|

# access

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /access/login_attempts|def get_login_attempts(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):|application/json|STABLE|

# data_classification

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /data_classification/dsm_event_mappings|def get_dsm_event_mappings(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /data_classification/dsm_event_mappings|def post_dsm_event_mappings(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /data_classification/dsm_event_mappings/{dsm_event_mapping_id}|def get_dsm_event_mappings_by_dsm_event_mapping_id(self, dsm_event_mapping_id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /data_classification/dsm_event_mappings/{dsm_event_mapping_id}|def post_dsm_event_mappings_by_dsm_event_mapping_id(self, dsm_event_mapping_id, *, data, fields=None, **kwargs):|application/json|STABLE|
|GET /data_classification/high_level_categories|def get_high_level_categories(self, *, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|STABLE|
|GET /data_classification/high_level_categories/{high_level_category_id}|def get_high_level_categories_by_high_level_category_id(self, high_level_category_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /data_classification/low_level_categories|def get_low_level_categories(self, *, fields=None, Range=None, filter=None, sort=None, **kwargs):|application/json|STABLE|
|GET /data_classification/low_level_categories/{low_level_category_id}|def get_low_level_categories_by_low_level_category_id(self, low_level_category_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /data_classification/qid_records|def get_qid_records(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /data_classification/qid_records|def post_qid_records(self, *, data, fields=None, **kwargs):|application/json|STABLE|
|POST /data_classification/qid_records/{qid_record_id}|def post_qid_records_by_qid_record_id(self, qid_record_id, *, qid_record, fields=None, **kwargs):|application/json|STABLE|
|GET /data_classification/qid_records/{qid_record_id}|def get_qid_records_by_qid_record_id(self, qid_record_id, *, fields=None, **kwargs):|application/json|STABLE|

# forensics

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|POST /forensics/alerting_jobs/{id}|def post_alerting_jobs_by_id(self, id, *, alerting_job, **kwargs):|application/json|UNDOCUMENTED|
|GET /forensics/capture/recoveries|def get_capture_recoveries(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /forensics/capture/recoveries|def post_capture_recoveries(self, *, recovery, fields=None, **kwargs):|application/json|STABLE|
|GET /forensics/capture/recoveries/{id}|def get_capture_recoveries_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /forensics/capture/recovery_tasks|def get_capture_recovery_tasks(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|GET /forensics/capture/recovery_tasks/{id}|def get_capture_recovery_tasks_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /forensics/case_management/case_create_tasks/{id}|def get_case_management_case_create_tasks_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /forensics/case_management/cases|def get_case_management_cases(self, *, fields=None, Range=None, filter=None, **kwargs):|application/json|STABLE|
|POST /forensics/case_management/cases|def post_case_management_cases(self, *, case, fields=None, **kwargs):|application/json|STABLE|
|GET /forensics/case_management/cases/{id}|def get_case_management_cases_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /forensics/managed_updates/{host}|def get_managed_updates_by_host(self, host, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /forensics/recovery_jobs/{id}|def post_recovery_jobs_by_id(self, id, *, recovery_job, **kwargs):|application/json|UNDOCUMENTED|
|POST /forensics/scheduledactions/statuses/{id}/{host}|def post_scheduledactions_statuses_id_by_host(self, id, host, *, status, **kwargs):|application/json|UNDOCUMENTED|
|GET /forensics/usermanagement/users/{username}|def get_usermanagement_users_by_username(self, username, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# internal

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /internal/historical_correlation/hc_profiles|def get_historical_correlation_hc_profiles(self, *, filter=None, sort=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /internal/historical_correlation/hc_profiles/{id}|def get_historical_correlation_hc_profiles_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /internal/system/servers/{server_id}|def get_system_servers_by_server_id(self, server_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|PUT /internal/system/servers/{server_id}/firewall_rules|def put_system_servers_firewall_rules_by_server_id(self, server_id, *, rules, **kwargs):|application/json|UNDOCUMENTED|
|GET /internal/system/servers/{server_id}/firewall_rules|def get_system_servers_firewall_rules_by_server_id(self, server_id, **kwargs):|application/json|UNDOCUMENTED|
|GET /internal/system/servers/{server_id}/network_interfaces|def get_system_servers_network_interfaces_by_server_id(self, server_id, *, interface_types=None, Range=None, filter=None, sort=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# historical_correlation

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /historical_correlation/hc_offense_info|def get_hc_offense_info(self, *, offense_id, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/potential_event_rules|def get_potential_event_rules(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/potential_event_saved_searches|def get_potential_event_saved_searches(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/potential_flow_rules|def get_potential_flow_rules(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/potential_flow_saved_searches|def get_potential_flow_saved_searches(self, *, filter=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /historical_correlation/profiles|def post_profiles(self, *, profileData, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/profiles|def get_profiles(self, *, filter=None, sort=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /historical_correlation/profiles/{id}|def post_profiles_by_id(self, id, *, profileData, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /historical_correlation/profiles/{id}|def delete_profiles_by_id(self, id, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/profiles/{id}|def get_profiles_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /historical_correlation/profiles/{id}/runs|def post_profiles_runs_by_id(self, id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/profiles/{id}/runs|def get_profiles_runs_by_id(self, id, *, filter=None, sort=None, fields=None, Range=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /historical_correlation/profiles/{id}/runs/{run_id}|def get_profiles_id_runs_by_run_id(self, id, run_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|

# backup_and_restore

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /backup_and_restore/backups|def get_backups(self, *, sort=None, filter=None, Range=None, fields=None, **kwargs):|application/json|STABLE|
|POST /backup_and_restore/backups|def post_backups(self, *, backup_type, backup, fields=None, **kwargs):|application/json|STABLE|
|GET /backup_and_restore/backups/{id}|def get_backups_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /backup_and_restore/backups/{id}|def post_backups_by_id(self, id, *, backup, fields=None, **kwargs):|application/json|STABLE|
|DELETE /backup_and_restore/backups/{id}|def delete_backups_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|POST /backup_and_restore/restores|def post_restores(self, *, restore, fields=None, **kwargs):|application/json|STABLE|
|GET /backup_and_restore/restores|def get_restores(self, *, sort=None, filter=None, Range=None, fields=None, **kwargs):|application/json|STABLE|
|GET /backup_and_restore/restores/{id}|def get_restores_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /backup_and_restore/restores/{id}|def delete_restores_by_id(self, id, **kwargs):|text/plain|STABLE|
|POST /backup_and_restore/restores/{id}|def post_restores_by_id(self, id, *, restore, fields=None, **kwargs):|application/json|STABLE|

# disaster_recovery

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /disaster_recovery/ariel_copy_profiles|def get_ariel_copy_profiles(self, *, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /disaster_recovery/ariel_copy_profiles|def post_ariel_copy_profiles(self, *, arielCopyProfileDTO, fields=None, **kwargs):|application/json|STABLE|
|POST /disaster_recovery/ariel_copy_profiles/{id}|def post_ariel_copy_profiles_by_id(self, id, *, arielCopyProfileDTO, fields=None, **kwargs):|application/json|STABLE|
|GET /disaster_recovery/ariel_copy_profiles/{id}|def get_ariel_copy_profiles_by_id(self, id, *, fields=None, **kwargs):|application/json|STABLE|
|DELETE /disaster_recovery/ariel_copy_profiles/{id}|def delete_ariel_copy_profiles_by_id(self, id, **kwargs):|text/plain|STABLE|

# scanner

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /scanner/profiles|def get_profiles(self, **kwargs):|application/json|STABLE|
|POST /scanner/profiles/create|def post_profiles_create(self, *, scanProfile, **kwargs):|text/plain|STABLE|
|POST /scanner/profiles/start|def post_profiles_start(self, *, scanProfileId, **kwargs):|text/plain|STABLE|
|POST /scanner/scanprofiles|def post_scanprofiles(self, *, scanProfile, **kwargs):|text/plain|STABLE|
|GET /scanner/scanprofiles|def get_scanprofiles(self, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|GET /scanner/scanprofiles/{profileid}|def get_scanprofiles_by_profileid(self, profileid, *, Range=None, filter=None, fields=None, **kwargs):|application/json|STABLE|
|POST /scanner/scanprofiles/{profileid}|def post_scanprofiles_by_profileid(self, profileid, *, scanProfile, **kwargs):|application/json|STABLE|
|DELETE /scanner/scanprofiles/{profileid}|def delete_scanprofiles_by_profileid(self, profileid, **kwargs):|text/plain|STABLE|
|GET /scanner/scanprofiles/{profileid}/runs|def get_scanprofiles_runs_by_profileid(self, profileid, *, Range=None, fields=None, **kwargs):|application/json|STABLE|
|GET /scanner/scanprofiles/{profileid}/runs/{run_id}|def get_scanprofiles_profileid_runs_by_run_id(self, profileid, run_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /scanner/scanprofiles/{profileid}/runs/{run_id}/results|def get_scanprofiles_profileid_runs_results_by_run_id(self, profileid, run_id, *, Range=None, fields=None, **kwargs):|application/json|STABLE|
|POST /scanner/scanprofiles/{profileid}/start|def post_scanprofiles_start_by_profileid(self, profileid, *, ips=None, **kwargs):|text/plain|STABLE|

# reporting

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /reporting/groups|def get_groups(self, *, Range=None, fields=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /reporting/groups/{group_id}|def post_groups_by_group_id(self, group_id, *, group, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /reporting/groups/{group_id}|def get_groups_by_group_id(self, group_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /reporting/groups/{group_id}|def delete_groups_by_group_id(self, group_id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /reporting/templates|def get_templates(self, *, Range=None, fields=None, filter=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /reporting/templates/{template_id}|def get_templates_by_template_id(self, template_id, *, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|POST /reporting/templates/{template_id}|def post_templates_by_template_id(self, template_id, *, report_template, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|DELETE /reporting/templates/{template_id}|def delete_templates_by_template_id(self, template_id, **kwargs):|text/plain|UNDOCUMENTED|
|GET /reporting/templates/{template_id}/output_type/{output_type}|def get_templates_template_id_output_type_by_output_type(self, template_id, output_type, **kwargs):|text/plain|UNDOCUMENTED|

# auth

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|POST /auth/logout|def post_logout(self, **kwargs):|text/plain|STABLE|

# help

| API | QRadar4py | Return type | Visibility |
|-----|-----------|--------------|------------|
|GET /help/capabilities|def get_capabilities(self, *, full_content=None, Range=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /help/capabilities/{version}|def get_capabilities_by_version(self, version, *, full_content=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /help/capabilities/{version}/{path}|def get_capabilities_version_by_path(self, version, path, *, full_content=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /help/capabilities/{version}/{path}/{request_type}|def get_capabilities_version_path_by_request_type(self, version, path, request_type, *, full_content=None, fields=None, **kwargs):|application/json|UNDOCUMENTED|
|GET /help/endpoints|def get_endpoints(self, *, Range=None, fields=None, filter=None, **kwargs):|application/json|STABLE|
|GET /help/endpoints/{endpoint_id}|def get_endpoints_by_endpoint_id(self, endpoint_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /help/resources|def get_resources(self, *, Range=None, fields=None, filter=None, **kwargs):|application/json|STABLE|
|GET /help/resources/{resource_id}|def get_resources_by_resource_id(self, resource_id, *, fields=None, **kwargs):|application/json|STABLE|
|GET /help/versions|def get_versions(self, *, Range=None, fields=None, filter=None, **kwargs):|application/json|STABLE|
|GET /help/versions/{version_id}|def get_versions_by_version_id(self, version_id, *, fields=None, **kwargs):|application/json|STABLE|

