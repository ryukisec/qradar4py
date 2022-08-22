from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Config(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /config and its endpoints.
    """
    __baseurl = 'config/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_access_authorized_services(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/authorized_services
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/authorized_services')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_authorized_services_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/authorized_services/{id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/authorized_services/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_access_roles(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/roles
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/roles')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_roles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/roles/{id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/roles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('tenant_id', 'current_security_profile', 'filter', 'fields')
    def get_access_security_profiles(self, *, tenant_id=None, current_security_profile=None, filter=None, Range=None,
                                     fields=None, **kwargs):
        """
        GET /config/access/security_profiles
        Get the list of deployed security profiles available in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'access/security_profiles')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_security_profiles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/security_profiles/{id}
        Get a deployed security profile by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'access/security_profiles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('name', 'role_id', 'security_profile_id', 'expires', 'fields')
    def post_access_staged_authorized_services(self, *, name, role_id, security_profile_id, expires=None, fields=None,
                                               **kwargs):
        """
        POST /config/access/staged_authorized_services
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_authorized_services')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_access_staged_authorized_services(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/staged_authorized_services
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_authorized_services')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_access_staged_authorized_services_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /config/access/staged_authorized_services/{id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_authorized_services/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_staged_authorized_services_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/staged_authorized_services/{id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_authorized_services/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_access_staged_roles(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/staged_roles
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_roles')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('name', 'capabilities', 'fields')
    def post_access_staged_roles(self, *, name, capabilities, fields=None, **kwargs):
        """
        POST /config/access/staged_roles
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_roles')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_access_staged_roles_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /config/access/staged_roles/{id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_roles/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_staged_roles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/staged_roles/{id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_roles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_access_tenant_management_tenants(self, *, tenant, fields=None, **kwargs):
        """
        POST /config/access/tenant_management/tenants
        Create a new tenant.
        """
        function_endpoint = urljoin(self._baseurl, 'access/tenant_management/tenants')
        return self._call('POST', function_endpoint, json=tenant, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_access_tenant_management_tenants(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/tenant_management/tenants
        Retrieve the list of all tenants ordered by tenant id.
        """
        function_endpoint = urljoin(self._baseurl, 'access/tenant_management/tenants')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_tenant_management_tenants_by_tenant_id(self, tenant_id, *, fields=None, **kwargs):
        """
        GET /config/access/tenant_management/tenants/{tenant_id}
        Retrieve a tenant by tenant id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'access/tenant_management/tenants/{tenant_id}'.format(tenant_id=tenant_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_access_tenant_management_tenants_by_tenant_id(self, tenant_id, *, tenant, fields=None, **kwargs):
        """
        POST /config/access/tenant_management/tenants/{tenant_id}
        Update a tenant
        """
        function_endpoint = urljoin(self._baseurl,
                                    'access/tenant_management/tenants/{tenant_id}'.format(tenant_id=tenant_id))
        return self._call('POST', function_endpoint, json=tenant, **kwargs)

    def delete_access_tenant_management_tenants_by_tenant_id(self, tenant_id, **kwargs):
        """
        DELETE /config/access/tenant_management/tenants/{tenant_id}
        Delete a tenant.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'access/tenant_management/tenants/{tenant_id}'.format(tenant_id=tenant_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_access_user_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /config/access/user_dependent_tasks/{task_id}
        Cancels a dependent user task.
        """
        function_endpoint = urljoin(self._baseurl, 'access/user_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_access_user_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/access/user_dependent_tasks/{task_id}
        Retrieves the dependent user task status.
        """
        function_endpoint = urljoin(self._baseurl, 'access/user_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_user_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/access/user_dependent_tasks/{task_id}/results
        Retrieves the user dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'access/user_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('contains', 'filter', 'fields')
    def get_access_user_roles(self, *, contains=None, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/user_roles
        Get the list of deployed user roles available in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'access/user_roles')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_user_roles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/user_roles/{id}
        Get a deployed user role by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'access/user_roles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('current_user', 'sort', 'filter', 'fields')
    def get_access_users(self, *, current_user=None, sort=None, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/users
        Retrieve Deployed Users.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('user')
    def post_access_users(self, *, user, **kwargs):
        """
        POST /config/access/users
        Create (and deploy) a single QRadar user.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/users')
        return self._call('POST', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_users_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/users/{id}
        Retrieves a deployed user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_access_users_by_id(self, id, *, body, fields=None, **kwargs):
        """
        POST /config/access/users/{id}
        Update a deployed user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=body, **kwargs)

    @request_vars('fields')
    def get_access_users_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/users/{id}/dependents
        Retrieves the objects that depend on the user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('capabilities', 'filter', 'fields')
    def get_access_users_with_capability_filter(self, *, capabilities, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access/users_with_capability_filter
        Retrieves a list of deployed users.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/users_with_capability_filter')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_access_control_roles(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access_control/roles
        Retrieves a list of a list of deployed roles that are currently in the system.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/roles')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_control_roles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access_control/roles/{id}
        Retrieves a deployed role that is currently in the system by its ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/roles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_control_user_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/access_control/user_dependent_tasks/{task_id}
        Retrieve the dependent the User task status.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'access_control/user_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_access_control_user_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /config/access_control/user_dependent_tasks/{task_id}
        Cancel the dependent the User task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'access_control/user_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_control_user_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/access_control/user_dependent_tasks/{task_id}/results
        Retrieve the User Dependent Task Results
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'access_control/user_dependent_tasks/{task_id}/results'.format(task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_access_control_users(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/access_control/users
        Retrieve the Deployed Users
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/users')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_control_users_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access_control/users/{id}
        Retrieve the Deployed User
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/users/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_access_control_users_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access_control/users/{id}/dependents
        Find the objects that depend on the User
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access_control/users/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_backup_and_restore_scheduled_backup_configurations(self, *, fields=None, **kwargs):
        """
        GET /config/backup_and_restore/scheduled_backup_configurations
        Retrieves a list of Backup Configurations.
        """
        function_endpoint = urljoin(self._baseurl, 'backup_and_restore/scheduled_backup_configurations')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_backup_and_restore_scheduled_backup_configurations_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/backup_and_restore/scheduled_backup_configurations/{id}
        Retrieves a Backup Configuration by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'backup_and_restore/scheduled_backup_configurations/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields', 'sort')
    def get_certificates_components(self, *, filter=None, Range=None, fields=None, sort=None, **kwargs):
        """
        GET /config/certificates/components
        Gets the list of registered component names, paired with component ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/components')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_certificates_end_certificates(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/certificates/end_certificates
        Gets the list of all certificates that have been uploaded and deployed.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_certificates_end_certificates_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/certificates/end_certificates/{id}
        Gets information about a specific deployed certificate, which is identified by its ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_certificates_end_certificates_full_chain_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/certificates/end_certificates/{id}/full_chain
        Gets the full chain of the certificate.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/end_certificates/{id}/full_chain'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_certificates_root_certificates(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/certificates/root_certificates
        Gets the list of all root certificates that have been uploaded and deployed.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_certificates_root_certificates_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/certificates/root_certificates/{id}
        Gets details of a deployed root certificate by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'certificates/root_certificates/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def get_certificates_root_certificates_get_dependant_ids_by_id(self, id, **kwargs):
        """
        GET /config/certificates/root_certificates/{id}/get_dependant_ids
        Gets a list of end certificate IDs that depend on the root certificate. This endpoint might not return the dependent IDs of the certificates that were uploaded in the last 24 hours.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'certificates/root_certificates/{id}/get_dependant_ids'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_data_lake_properties(self, *, data_lake_property, fields=None, **kwargs):
        """
        POST /config/data_lake/properties
        Create a new Data Lake Property
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_lake/properties')
        return self._call('POST', function_endpoint, json=data_lake_property, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_data_lake_properties(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/data_lake/properties
        Retrieves a list of Data Lake Properties.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_lake/properties')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_data_lake_properties_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /config/data_lake/properties/{name}
        Retrieves a single Data Lake Property by Name.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_lake/properties/{name}'.format(name=name))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_data_lake_properties_by_name(self, name, **kwargs):
        """
        DELETE /config/data_lake/properties/{name}
        Deletes a single Data Lake Property by Name.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_lake/properties/{name}'.format(name=name))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_data_lake_properties_by_name(self, name, *, data_lake_property, fields=None, **kwargs):
        """
        POST /config/data_lake/properties/{name}
        Updates the Data Lake Property configuration.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'data_lake/properties/{name}'.format(name=name))
        return self._call('POST', function_endpoint, json=data_lake_property, headers=headers, **kwargs)

    def get_deploy_action(self, **kwargs):
        """
        GET /config/deploy_action
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deploy_action')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('type')
    def post_deploy_action(self, *, type=None, **kwargs):
        """
        POST /config/deploy_action
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deploy_action')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_components(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/components
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/components')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_components_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/components/{id}
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/components/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_hosts(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/hosts
        Retrieves a list of all deployed hosts.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_deployment_hosts_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/hosts/{id}
        Retrieves a deployed host by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_deployment_hosts_by_id(self, id, *, host, fields=None, **kwargs):
        """
        POST /config/deployment/hosts/{id}
        Updates a host by ID and sends a JMS message to update the pipeline.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=host, **kwargs)

    @request_vars('fields')
    def get_deployment_hosts_capabilities_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/hosts/{id}/capabilities
        Gets the EPS, FPS, EPSLimit, FPSLimit, and Max Log Source for a managed host
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts/{id}/capabilities'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_hosts_tunnels_by_id(self, id, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/hosts/{id}/tunnels
        Gets the list of tunnels for the host.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/hosts/{id}/tunnels'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_deployment_license_pool(self, *, fields=None, **kwargs):
        """
        GET /config/deployment/license_pool
        Retrieves the deployed license pool information.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/license_pool')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_licenses(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/licenses
        Get a list of License and information form the encrypted file.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/licenses')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_natgroups(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/natgroups
        Get deployment NAT groups.  If no NAT groups exist an empty list will be returned.

        Nat Group Structure


        id - The unique id of the NAT group in the deployment.
        name - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/natgroups')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_natgroups_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/natgroups/{id}
        Get NAT group by id.

        Nat Group Structure


        id - The unique id of the NAT group in the deployment.
        name - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/natgroups/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_staged_components(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/staged_components
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_components')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('hostid', 'type', 'properties', 'fields')
    def post_deployment_staged_components(self, *, type, hostid=None, properties=None, fields=None, **kwargs):
        """
        POST /config/deployment/staged_components
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_components')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('targetids', 'updated_properties', 'fields')
    def post_deployment_staged_components_by_id(self, id, *, targetids=None, updated_properties=None, fields=None,
                                                **kwargs):
        """
        POST /config/deployment/staged_components/{id}
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_components/{id}'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_deployment_staged_components_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /config/deployment/staged_components/{id}
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_components/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_staged_components_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/staged_components/{id}
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_components/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('showall', 'filter', 'fields')
    def get_deployment_staged_hosts(self, *, showall=None, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/staged_hosts
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_hosts')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_deployment_staged_hosts(self, *, deploymentHost, fields=None, **kwargs):
        """
        POST /config/deployment/staged_hosts
        Add a deployment host.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_hosts')
        return self._call('POST', function_endpoint, json=deploymentHost, headers=headers, **kwargs)

    @header_vars('fields')
    def post_deployment_staged_hosts_by_id(self, id, *, deploymentHost, fields=None, **kwargs):
        """
        POST /config/deployment/staged_hosts/{id}
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_hosts/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=deploymentHost, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_deployment_staged_hosts_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /config/deployment/staged_hosts/{id}
        Remove deployment host by id. Cannot remove hosts that are not not in the active state, hosts in a High
        Availability Pair, the console host, or the hosts with failed license pool validation.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_hosts/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_staged_hosts_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/staged_hosts/{id}
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_hosts/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_deployment_staged_natgroups(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/deployment/staged_natgroups
        Get deployment NAT groups.  If staging directory does not exist will return deployed NAT groups.
        If no NAT groups exist an empty list will be returned.

        Nat Group Structure


        id - The unique id of the NAT group in the deployment.
        name - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('name', 'fields')
    def post_deployment_staged_natgroups(self, *, name, fields=None, **kwargs):
        """
        POST /config/deployment/staged_natgroups
        Add a NAT group.

        Nat Group Structure


        id - The unique id of the NAT group in the deployment.
        name - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('name', 'fields')
    def post_deployment_staged_natgroups_by_id(self, id, *, name, fields=None, **kwargs):
        """
        POST /config/deployment/staged_natgroups/{id}
        Edit a NAT group.

        Nat Group Structure


        id - The unique id of the NAT group in the deployment.
        name - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups/{id}'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_staged_natgroups_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/staged_natgroups/{id}
        Get NAT group by id. If staging directory does not exist will return the deployed NAT group.

        Nat Group Structure


        id - The unique id of the NAT group in the deployment.
        name - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_deployment_staged_natgroups_by_id(self, id, *, fields=None, **kwargs):
        """
        DELETE /config/deployment/staged_natgroups/{id}
        Remove a NAT group by id.

        Nat Group Structure


        id - The unique id of the NAT group in the deployment.
        name - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_summary(self, *, fields=None, **kwargs):
        """
        GET /config/deployment/summary
        Get the deployment id.

        Deployment Summary Stucture


        deployment_id - the id of the this deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/summary')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_disaster_recovery_disaster_recovery_config(self, *, fields=None, **kwargs):
        """
        GET /config/disaster_recovery/disaster_recovery_config
        Retrieves the Deployed Disaster Recovery Config.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'disaster_recovery/disaster_recovery_config')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_domain_management_domains(self, *, domain, fields=None, **kwargs):
        """
        POST /config/domain_management/domains
        Creates a new domain.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains')
        return self._call('POST', function_endpoint, json=domain, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_domain_management_domains(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/domain_management/domains
        Gets the list of domains.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_domain_management_domains_by_domain_id(self, domain_id, *, fields=None, **kwargs):
        """
        GET /config/domain_management/domains/{domain_id}
        Gets an individual domain by ID
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains/{domain_id}'.format(domain_id=domain_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_domain_management_domains_by_domain_id(self, domain_id, *, fields=None, **kwargs):
        """
        DELETE /config/domain_management/domains/{domain_id}
        Deletes a domain by domain id.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains/{domain_id}'.format(domain_id=domain_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_domain_management_domains_by_domain_id(self, domain_id, *, domain, fields=None, **kwargs):
        """
        POST /config/domain_management/domains/{domain_id}
        Updates an existing domain.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains/{domain_id}'.format(domain_id=domain_id))
        return self._call('POST', function_endpoint, json=domain, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_retention_buckets(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_retention_buckets
        Retrieves a list of event retention buckets.
        """
        function_endpoint = urljoin(self._baseurl, 'event_retention_buckets')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_retention_buckets_by_id(self, id, *, retention_bucket, fields=None, **kwargs):
        """
        POST /config/event_retention_buckets/{id}
        Updates the event retention bucket owner or enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl, 'event_retention_buckets/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=retention_bucket, **kwargs)

    def delete_event_retention_buckets_by_id(self, id, **kwargs):
        """
        DELETE /config/event_retention_buckets/{id}
        Deletes an event retention bucket.
        """
        function_endpoint = urljoin(self._baseurl, 'event_retention_buckets/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_retention_buckets_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_retention_buckets/{id}
        Retrieves an event retention bucket.
        """
        function_endpoint = urljoin(self._baseurl, 'event_retention_buckets/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_properties_dep_by_aql_property_id(self, aql_property_id, *, fields=None,
                                                                                  **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_properties/dep/{aql_property_id}
        Retrieves a AQL event property based on the supplied AQL property aql_property_id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_properties/dep/{aql_property_id}'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_aql_properties_by_aql_property_id(self, aql_property_id, *, data,
                                                                               fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/aql_properties/{aql_property_id}
        Updates an existing custom AQL property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_properties/{aql_property_id}'.format(
                                        aql_property_id=aql_property_id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_properties_by_aql_property_id(self, aql_property_id, *, fields=None,
                                                                              **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_properties/{aql_property_id}
        Retrieves a AQL event property based on the supplied AQL property ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_properties/{aql_property_id}'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_properties_dependents_by_aql_property_id(self, aql_property_id, *,
                                                                                         fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_properties/{aql_property_id}/dependents
        Retrieves the objects that depend on the event AQL property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_properties/{aql_property_id}/dependents'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_properties_dependents_disable_by_aql_property_id(self, aql_property_id,
                                                                                                 *, fields=None,
                                                                                                 **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_properties/{aql_property_id}/dependents/disable
        Retrieves the objects that depend on the event AQL property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_properties/{aql_property_id}/dependents/disable'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_aql_property_by_aql_property_name(self, aql_property_name, *, filter=None,
                                                                              Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_property/{aql_property_name}
        Retrieves  an event AQL property by it's name.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_property/{aql_property_name}'.format(
                                        aql_property_name=aql_property_name))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *, task,
                                                                                             fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}
        Cancels the event AQL property dependent task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                            fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}
        Retrieves the status of the event AQL property dependents task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_property_dependent_tasks_disable_results_by_task_id(self, task_id, *,
                                                                                                    fields=None,
                                                                                                    **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}/results
        Retrieves the aql property dependent task results.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, task,
                                                                                     fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/aql_property_dependent_tasks/{task_id}
        Cancels the event AQL property dependent task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                    **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_property_dependent_tasks/{task_id}
        Retrieves the status of the event AQL property dependents task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_aql_property_dependent_tasks_results_by_task_id(self, task_id, *,
                                                                                            fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/aql_property_dependent_tasks/{task_id}/results
        Retrieves the aql property dependent task results.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/aql_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_calculated_properties(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/calculated_properties
        Creates a new calculated event property.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/calculated_properties')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_calculated_properties(self, *, filter=None, Range=None, fields=None,
                                                                  **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties
        Retrieves a list of calculated event properties.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/calculated_properties')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_properties_dep_by_calculated_property_id(self,
                                                                                                calculated_property_id,
                                                                                                *, fields=None,
                                                                                                **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties/dep/{calculated_property_id}
        Retrieves a calculated event property based on the supplied calculated property ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_properties/dep/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_properties_by_calculated_property_id(self,
                                                                                            calculated_property_id, *,
                                                                                            fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}
        Retrieves a calculated event property based on the supplied calculated property identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_properties/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_event_sources_custom_properties_calculated_properties_by_calculated_property_id(self,
                                                                                               calculated_property_id,
                                                                                               *, fields=None,
                                                                                               **kwargs):
        """
        DELETE /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}
        Deletes the event calculated property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_properties/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_calculated_properties_by_calculated_property_id(self,
                                                                                             calculated_property_id, *,
                                                                                             data, fields=None,
                                                                                             **kwargs):
        """
        POST /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}
        Updates an existing calculated event property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_properties/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_properties_dependents_by_calculated_property_id(self,
                                                                                                       calculated_property_id,
                                                                                                       *, fields=None,
                                                                                                       **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents
        Retrieves the objects that depend on the event calculated property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_properties_dependents_change_field_type_by_calculated_property_id(
            self, calculated_property_id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/change_field_type
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/change_field_type'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_properties_dependents_disable_by_calculated_property_id(self,
                                                                                                               calculated_property_id,
                                                                                                               *,
                                                                                                               fields=None,
                                                                                                               **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable
        Retrieves the objects that depend on the event calculated property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_calculated_property_by_calculated_property_name(self,
                                                                                            calculated_property_name, *,
                                                                                            filter=None, Range=None,
                                                                                            fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property/{calculated_property_name}
        Retrieves a list of event calculated properties.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property/{calculated_property_name}'.format(
                                        calculated_property_name=calculated_property_name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_property_delete_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                        **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_delete_tasks/{task_id}
        Retrieves the status of the event calculated property delete task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_delete_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self,
                                                                                                              task_id,
                                                                                                              *, task,
                                                                                                              fields=None,
                                                                                                              **kwargs):
        """
        POST /config/event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self,
                                                                                                             task_id, *,
                                                                                                             fields=None,
                                                                                                             **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_results_by_task_id(
            self, task_id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}/results
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                                   fields=None,
                                                                                                   **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}
        Retrieves the event calculated property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                                    task, fields=None,
                                                                                                    **kwargs):
        """
        POST /config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}
        Cancels the calculated property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_property_dependent_tasks_disable_results_by_task_id(self,
                                                                                                           task_id, *,
                                                                                                           fields=None,
                                                                                                           **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results
        Retrieves the calculated property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *, task,
                                                                                            fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}
        Cancels the event calculated property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *,
                                                                                           fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}
        Retrieves the status of the event calculated property dependents task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_calculated_property_dependent_tasks_results_by_task_id(self, task_id, *,
                                                                                                   fields=None,
                                                                                                   **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results
        Retrieves the calculated property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter')
    def get_event_sources_custom_properties_calculated_property_operands(self, *, filter=None, Range=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_property_operands
        Retrieves the list of available options for calculated event property operand.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/calculated_property_operands')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_property_cef_expressions(self, *, filter=None, Range=None, fields=None,
                                                                     **kwargs):
        """
        GET /config/event_sources/custom_properties/property_cef_expressions
        Retrieves a list of CEF expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_cef_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_cef_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_cef_expressions
        Creates a new CEF expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_cef_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_cef_expressions_by_expression_id(self, expression_id, *,
                                                                                      fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_cef_expressions/{expression_id}
        Retrieves a CEF expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_cef_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_cef_expressions_by_expression_id(self, expression_id, *, data,
                                                                                       fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_cef_expressions/{expression_id}
        Updates an existing CEF expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_cef_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def delete_event_sources_custom_properties_property_cef_expressions_by_expression_id(self, expression_id, **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_cef_expressions/{expression_id}
        Deletes a CEF expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_cef_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_property_expressions(self, *, filter=None, Range=None, fields=None,
                                                                 **kwargs):
        """
        GET /config/event_sources/custom_properties/property_expressions
        Retrieves a list of event regex property expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_expressions
        Creates a new event regex property expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def delete_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_expressions/{expression_id}
        Deletes an event regex property expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, data,
                                                                                   fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_expressions/{expression_id}
        Updates an existing event regex property expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, fields=None,
                                                                                  **kwargs):
        """
        GET /config/event_sources/custom_properties/property_expressions/{expression_id}
        Retrieves a event regex property expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_genericlist_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_genericlist_expressions
        Creates a new Generic List expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_genericlist_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_property_genericlist_expressions(self, *, filter=None, Range=None,
                                                                             fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_genericlist_expressions
        Retrieves a list of Generic List expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_genericlist_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_genericlist_expressions_by_expression_id(self, expression_id, *,
                                                                                               data, fields=None,
                                                                                               **kwargs):
        """
        POST /config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}
        Updates an existing Generic List expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_genericlist_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def delete_event_sources_custom_properties_property_genericlist_expressions_by_expression_id(self, expression_id,
                                                                                                 **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}
        Deletes a Generic List expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_genericlist_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_genericlist_expressions_by_expression_id(self, expression_id, *,
                                                                                              fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_genericlist_expressions/{expression_id}
        Retrieves a Generic List expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_genericlist_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_property_json_expressions(self, *, filter=None, Range=None, fields=None,
                                                                      **kwargs):
        """
        GET /config/event_sources/custom_properties/property_json_expressions
        Retrieves a list of JSON expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_json_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_json_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_json_expressions
        Creates a new JSON expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_json_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def delete_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id,
                                                                                          **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_json_expressions/{expression_id}
        Deletes a JSON expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_json_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id, *,
                                                                                       fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_json_expressions/{expression_id}
        Retrieves a JSON expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_json_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id, *, data,
                                                                                        fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_json_expressions/{expression_id}
        Updates an existing JSON expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_json_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_property_leef_expressions(self, *, filter=None, Range=None, fields=None,
                                                                      **kwargs):
        """
        GET /config/event_sources/custom_properties/property_leef_expressions
        Retrieves the list of LEEF Expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_leef_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_leef_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_leef_expressions
        Creates a new LEEF Expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_leef_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_leef_expressions_by_expression_id(self, expression_id, *,
                                                                                       fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_leef_expressions/{expression_id}
        Retrieves a LEEF Expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_leef_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_leef_expressions_by_expression_id(self, expression_id, *, data,
                                                                                        fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_leef_expressions/{expression_id}
        Updates an existing LEEF Expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_leef_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def delete_event_sources_custom_properties_property_leef_expressions_by_expression_id(self, expression_id,
                                                                                          **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_leef_expressions/{expression_id}
        Deletes a LEEF Expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_leef_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_nvp_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_nvp_expressions
        Creates a new Name Value Pair expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_nvp_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_property_nvp_expressions(self, *, filter=None, Range=None, fields=None,
                                                                     **kwargs):
        """
        GET /config/event_sources/custom_properties/property_nvp_expressions
        Retrieves a list of Name Value Pair expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_nvp_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_event_sources_custom_properties_property_nvp_expressions_by_expression_id(self, expression_id, **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_nvp_expressions/{expression_id}
        Deletes a Name Value Pair expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_nvp_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_nvp_expressions_by_expression_id(self, expression_id, *,
                                                                                      fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_nvp_expressions/{expression_id}
        Retrieves a Name Value Pair expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_nvp_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_nvp_expressions_by_expression_id(self, expression_id, *, data,
                                                                                       fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_nvp_expressions/{expression_id}
        Updates an existing Name Value Pair expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_nvp_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_xml_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_xml_expressions
        Creates a new XML expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_xml_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_property_xml_expressions(self, *, filter=None, Range=None, fields=None,
                                                                     **kwargs):
        """
        GET /config/event_sources/custom_properties/property_xml_expressions
        Retrieves a list of XML expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_xml_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_xml_expressions_by_expression_id(self, expression_id, *, data,
                                                                                       fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_xml_expressions/{expression_id}
        Updates an existing XML expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_xml_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_xml_expressions_by_expression_id(self, expression_id, *,
                                                                                      fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_xml_expressions/{expression_id}
        Retrieves a XML expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_xml_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_event_sources_custom_properties_property_xml_expressions_by_expression_id(self, expression_id, **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_xml_expressions/{expression_id}
        Deletes an XML expression based on the supplied identifier.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_xml_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_custom_properties_regex_properties(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_properties
        Retrieves a list of event regex properties.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/regex_properties')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_regex_properties(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/regex_properties
        Creates a new event regex property.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/regex_properties')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *,
                                                                                  fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}
        Retrieves a event regex property based on the supplied regex property ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_properties/{regex_property_id}'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, data,
                                                                                   fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/regex_properties/{regex_property_id}
        Updates an existing event regex property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_properties/{regex_property_id}'.format(
                                        regex_property_id=regex_property_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def delete_event_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *,
                                                                                     fields=None, **kwargs):
        """
        DELETE /config/event_sources/custom_properties/regex_properties/{regex_property_id}
        Deletes an event regex property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task is started to do this check.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_properties/{regex_property_id}'.format(
                                        regex_property_id=regex_property_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *,
                                                                                             fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents
        Retrieves the objects that depend on the event regex property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_properties/{regex_property_id}/dependents'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_properties_dependents_change_field_type_by_regex_property_id(self,
                                                                                                               regex_property_id,
                                                                                                               *,
                                                                                                               fields=None,
                                                                                                               **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type
        Retrieves the objects that depend on the event regex property for changing type of field for it.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_properties_dependents_disable_by_regex_property_id(self,
                                                                                                     regex_property_id,
                                                                                                     *, fields=None,
                                                                                                     **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/disable
        Retrieves the objects that depend on the event regex property for disabling it.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_properties/{regex_property_id}/dependents/disable'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_property_delete_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                   **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_property_delete_tasks/{task_id}
        Retrieves the event regex property delete task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_delete_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id,
                                                                                                         *, task,
                                                                                                         fields=None,
                                                                                                         **kwargs):
        """
        POST /config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}
        Cancels the regex property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id,
                                                                                                        *, fields=None,
                                                                                                        **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}
        Retrieves the event regex property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_property_dependent_tasks_change_field_type_results_by_task_id(self,
                                                                                                                task_id,
                                                                                                                *,
                                                                                                                fields=None,
                                                                                                                **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results
        Retrieves the regex property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *, task,
                                                                                               fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}
        Cancels the regex property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                              fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}
        Retrieves the event regex property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_property_dependent_tasks_disable_results_by_task_id(self, task_id, *,
                                                                                                      fields=None,
                                                                                                      **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results
        Retrieves the regex property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, task,
                                                                                       fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}
        Cancels the regex property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                      **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}
        Retrieves the event regex property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_regex_property_dependent_tasks_results_by_task_id(self, task_id, *,
                                                                                              fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results
        Retrieves the regex property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_disconnected_log_collectors(self, *, disconnected_log_collector, fields=None, **kwargs):
        """
        POST /config/event_sources/disconnected_log_collectors
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/disconnected_log_collectors')
        return self._call('POST', function_endpoint, json=disconnected_log_collector, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'sort', 'fields')
    def get_event_sources_disconnected_log_collectors(self, *, filter=None, sort=None, Range=None, fields=None,
                                                      **kwargs):
        """
        GET /config/event_sources/disconnected_log_collectors
        Retrieves a list of disconnected log collectors.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/disconnected_log_collectors')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_event_sources_disconnected_log_collectors_by_id(self, id, **kwargs):
        """
        DELETE /config/event_sources/disconnected_log_collectors/{id}
        Deletes a Disconnected Log Collector by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/disconnected_log_collectors/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_event_sources_disconnected_log_collectors_by_id(self, id, *, log_source_data, fields=None, **kwargs):
        """
        POST /config/event_sources/disconnected_log_collectors/{id}
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/disconnected_log_collectors/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=log_source_data, **kwargs)

    @request_vars('fields')
    def get_event_sources_disconnected_log_collectors_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/disconnected_log_collectors/{id}
        Retrieves an disconnected log collector by ID..
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/disconnected_log_collectors/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_event_collectors(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/event_collectors
        Retrieves a list of event collectors..
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/event_collectors')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_event_collectors_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/event_collectors/{id}
        Retrieves an event collector by ID..
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/event_collectors/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_generated_regexes(self, *, payload, fields=None, **kwargs):
        """
        POST /config/event_sources/generated_regexes
        Retrieves a regex pattern
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/generated_regexes')
        return self._call('POST', function_endpoint, json=payload, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_extensions(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_extensions
        Retrieve a list of all log source extensions.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_extensions')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_extensions(self, *, file, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_extensions
        Creates a log source extension. Expects a Multipart request consisting of several
        StringParts, that represent the name/description/enabled/use_condition, and then
        A single FilePart that is the Log Source Extension XML file.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_extensions')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'multipart/form-data'}, data=file,
                          headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_extensions_by_log_source_extension_id(self, log_source_extension_id, *,
                                                                           fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_extensions/{log_source_extension_id}
        Retrieves a log source extension associated with supplied ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_extensions/{log_source_extension_id}'.format(
                                        log_source_extension_id=log_source_extension_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_event_sources_log_source_extensions_by_log_source_extension_id(self, log_source_extension_id, **kwargs):
        """
        DELETE /config/event_sources/log_source_extensions/{log_source_extension_id}
        Deletes a log source extension corresponding to the supplied ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_extensions/{log_source_extension_id}'.format(
                                        log_source_extension_id=log_source_extension_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_extensions_by_log_source_extension_id(self, log_source_extension_id, *, data=None,
                                                                            fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_extensions/{log_source_extension_id}
        Updates a log source extension.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_extensions/{log_source_extension_id}'.format(
                                        log_source_extension_id=log_source_extension_id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    def get_event_sources_log_source_management_autodetection_autodetection_global_enabled_check(self, **kwargs):
        """
        GET /config/event_sources/log_source_management/autodetection/autodetection_global_enabled_check
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/autodetection/autodetection_global_enabled_check')
        return self._call('GET', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_autodetection_config_records(self, *, config_record, fields=None,
                                                                              **kwargs):
        """
        POST /config/event_sources/log_source_management/autodetection/config_records
        Creates an Autodetection Config Record.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/autodetection/config_records')
        return self._call('POST', function_endpoint, json=config_record, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'sort', 'fields')
    def get_event_sources_log_source_management_autodetection_config_records(self, *, filter=None, sort=None,
                                                                             Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/autodetection/config_records
        Retrieves the list of Autodetection Config Records.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/autodetection/config_records')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_autodetection_config_records_by_config_id(self, config_id, *,
                                                                                          fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/autodetection/config_records/{config_id}
        Gets an individual Autodetection Config Record by id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/autodetection/config_records/{config_id}'.format(
                                        config_id=config_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_autodetection_config_records_by_config_id(self, config_id, *,
                                                                                           config_record, fields=None,
                                                                                           **kwargs):
        """
        POST /config/event_sources/log_source_management/autodetection/config_records/{config_id}
        Updates an Autodetection Config Record.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/autodetection/config_records/{config_id}'.format(
                                        config_id=config_id))
        return self._call('POST', function_endpoint, json=config_record, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_bulk_tasks_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_bulk_tasks/{id}
        Retrieves a log source bulk task by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_bulk_tasks/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_bulk_tasks_by_id(self, id, *, updated_log_source_bulk_task,
                                                                             fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_bulk_tasks/{id}
        Updates a log source bulk task.

        The only field that can be updated is the 'status' field, and the only allowed value is 'CANCELLED'.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_bulk_tasks/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=updated_log_source_bulk_task, **kwargs)

    def get_event_sources_log_source_management_log_source_counter_by_id(self, id, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_counter/{id}
        Undocumented endpoint to get the number of log sources for a given log source type.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_counter/{id}'.format(id=id))
        return self._call('GET', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_extensions(self, *, filter=None, Range=None, fields=None,
                                                                      **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_extensions
        Retrieves the list of log source extensions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_extensions')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_extensions_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_extensions/{id}
        Retrieves a log source extension by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_extensions/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_groups(self, *, filter=None, Range=None, fields=None,
                                                                  **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_groups
        Retrieves the list of log source groups.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_groups')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_groups(self, *, log_source_data, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_groups
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_groups')
        return self._call('POST', function_endpoint, json=log_source_data, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_groups_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_groups/{id}
        Retrieves a log source group by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_groups/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_languages(self, *, filter=None, Range=None, fields=None,
                                                                     **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_languages
        Retrieves the list of log source languages.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_languages')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_languages_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_languages/{id}
        Retrieves a log source language by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_languages/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_statistics(self, *, statistics=None, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_statistics
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_statistics')
        return self._call('POST', function_endpoint, json=statistics, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_tests(self, *, test, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_tests
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_tests')
        return self._call('POST', function_endpoint, json=test, headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_tests_by_id(self, id, *, updated_log_source_test,
                                                                        fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_tests/{id}
        Updates a log source test.

        The only field that can be updated is the 'status' field, and the only allowed value is 'CANCELLED'.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_tests/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=updated_log_source_test, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_tests_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_tests/{id}
        Retrieves a log source test by ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_tests/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_types(self, *, filter=None, Range=None, fields=None,
                                                                 **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types
        Retrieves a list of log source types. If called by a user/authorized service with System Administrator, Security Admin, or Manage Log Source Types permissions, then all fields will be returned in each log source type. If called by a less privileged client, only name and ID are returned in each log source type.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_types')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_types(self, *, log_source_data, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_types
        Create a new custom log source type. Log source types do not need to be deployed.

        The following fields can be provided in the body of this request, all other log source type fields will be ignored:

        name - String - The name of the log source type. Cannot be empty. Must be 241 characters or less. Must not have been used before.
        protocol_types - Array - The optional protocols that can be used for the log source type. All protocol ids must exist, list cannot be empty. If this field is not provided, all protocols will be available for this log source type.
        default_protocol_id - Long - The protocol option that should be the default solution for this log source type.
        log_source_extension_id - Long - The optional log source extension that is associated with the log source type.  If specified, this must correspond to an existing log source extension.

        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_types')
        return self._call('POST', function_endpoint, json=log_source_data, **kwargs)

    @header_vars('filter', 'Range', 'fields')
    def patch_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values(self, *,
                                                                                                dsm_paramater_allowed_values,
                                                                                                filter=None, Range=None,
                                                                                                fields=None, **kwargs):
        """
        PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values
        Create new dsm parameter allowed values or Update available dsm parameter allowed values.

        The following fields can be provided in the body of this request, all other dsm parameter allowed value fields will be ignored:

        id - Long- The id of the dsm parameter allowed value. If field id exist it considers as an update otherwise it is a create action.
        value - String - The value of the dsm parameter allowed value. Cannot be empty. Must be 8192 characters or less.
        dsm_parameter_definition_id - Long - The id of the corresponding dsmparameterdefinition.
        name - String - The name of the dsm parameter allowed value.
        sort_index - Long - the index of the record for sorting.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        if not isinstance(dsm_paramater_allowed_values, list):
            dsm_paramater_allowed_values = [dsm_paramater_allowed_values]
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values')
        return self._call('PATCH', function_endpoint, json=dsm_paramater_allowed_values, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values(self, *, filter=None,
                                                                                              Range=None, fields=None,
                                                                                              **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values
        Retrieve dsm parameter allowed values.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values_by_id(self, id, *,
                                                                                                    fields=None,
                                                                                                    **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}
        Retrieve a dsm parameter allowed value by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}'.format(
                                        id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values_by_id(self, id, *,
                                                                                                     dsm_paramater_allowed_value,
                                                                                                     fields=None,
                                                                                                     **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}
        Update a dsm parameter allowed value by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}'.format(
                                        id=id))
        return self._call('POST', function_endpoint, json=dsm_paramater_allowed_value, headers=headers, **kwargs)

    def delete_event_sources_log_source_management_log_source_types_dsm_parameter_allowed_values_by_id(self, id,
                                                                                                       **kwargs):
        """
        DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}
        Deletes a dsm paramater allowed value by ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_allowed_values/{id}'.format(
                                        id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values(
            self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values
        Retrieve dsm parameter allowed values.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('filter', 'Range', 'fields')
    def patch_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values(
            self, *, dsm_paramater_allowed_values, filter=None, Range=None, fields=None, **kwargs):
        """
        PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values
        Create new dsm parameter allowed values or Update available dsm parameter allowed values.

        The following fields can be provided in the body of this request, all other dsm parameter allowed value fields will be ignored:

        id - Long- The id of the dsm parameter allowed value. If field id exist it considers as an update otherwise it is a create action.
        value - String - The value of the dsm parameter allowed value. Cannot be empty. Must be 8192 characters or less.
        dsm_parameter_definition_id - Long - The id of the corresponding dsmparameterdefinition.
        name - String - The name of the dsm parameter allowed value.
        sort_index - Long - the index of the record for sorting.

        """
        if not isinstance(dsm_paramater_allowed_values, list):
            dsm_paramater_allowed_values = [dsm_paramater_allowed_values]
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values')
        return self._call('PATCH', function_endpoint, json=dsm_paramater_allowed_values, **kwargs)

    def delete_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_by_id(
            self, id, **kwargs):
        """
        DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}
        Deletes a dsm paramater allowed value by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}'.format(
                                        id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_by_id(
            self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}
        Retrieve a dsm parameter allowed value by id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}'.format(
                                        id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_allowed_values_by_id(
            self, id, *, dsm_paramater_allowed_value, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}
        Update a dsm parameter allowed value by id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_allowed_values/{id}'.format(
                                        id=id))
        return self._call('POST', function_endpoint, json=dsm_paramater_allowed_value, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameter_definition(
            self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_definition
        Retrieve dsm parameter definitions.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameter_definition')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('filter', 'Range', 'fields')
    def patch_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters(self, *,
                                                                                                              dsm_paramaters,
                                                                                                              filter=None,
                                                                                                              Range=None,
                                                                                                              fields=None,
                                                                                                              **kwargs):
        """
        PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters
        Create new dsm parameters or Update available dsm parameters.

        The following fields can be provided in the body of this request, all other dsm parameter fields will be ignored:

        id - Long- The id of the dsm parameter. If field id exist it considers as an update otherwise it is a create action.
        value - String - The value of the dsm parameter. Cannot be empty. Must be 8192 characters or less.
        dsm_parameter_definition_id - Long - The id of the corresponding dsmparameterdefinition.
        sensor_device_type_id - Long - The id of the corresponding sensordevicetype.
        event_collector_id - Long - The id of the corresponding eventcollector component.

        """
        if not isinstance(dsm_paramaters, list):
            dsm_paramaters = [dsm_paramaters]
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters')
        return self._call('PATCH', function_endpoint, json=dsm_paramaters, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters(self, *,
                                                                                                            filter=None,
                                                                                                            Range=None,
                                                                                                            fields=None,
                                                                                                            **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters
        Retrieve dsm parameters.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_by_id(
            self, id, **kwargs):
        """
        DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}
        Deletes a dsm paramater by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}'.format(
                                        id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_by_id(self,
                                                                                                                   id,
                                                                                                                   *,
                                                                                                                   dsm_paramaters,
                                                                                                                   fields=None,
                                                                                                                   **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}
        Update a dsm parameter by id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}'.format(
                                        id=id))
        return self._call('POST', function_endpoint, json=dsm_paramaters, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_configuration_dsm_parameters_by_id(self,
                                                                                                                  id, *,
                                                                                                                  fields=None,
                                                                                                                  **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}
        Retrieve a dsm parameter by id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_configuration/dsm_parameters/{id}'.format(
                                        id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameter_definition(self, *, filter=None,
                                                                                          Range=None, fields=None,
                                                                                          **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameter_definition
        Retrieve dsm parameter definitions.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameter_definition')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('filter', 'Range', 'fields')
    def patch_event_sources_log_source_management_log_source_types_dsm_parameters(self, *, dsm_paramaters, filter=None,
                                                                                  Range=None, fields=None, **kwargs):
        """
        PATCH /config/event_sources/log_source_management/log_source_types/dsm_parameters
        Create new dsm parameters or Update available dsm parameters.

        The following fields can be provided in the body of this request, all other dsm parameter fields will be ignored:

        id - Long- The id of the dsm parameter. If field id exist it considers as an update otherwise it is a create action.
        value - String - The value of the dsm parameter. Cannot be empty. Must be 8192 characters or less.
        dsm_parameter_definition_id - Long - The id of the corresponding dsmparameterdefinition.
        sensor_device_type_id - Long - The id of the corresponding sensordevicetype.
        event_collector_id - Long - The id of the corresponding eventcollector component.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        if not isinstance(dsm_paramaters, list):
            dsm_paramaters = [dsm_paramaters]
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameters')
        return self._call('PATCH', function_endpoint, json=dsm_paramaters, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameters(self, *, filter=None, Range=None,
                                                                                fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameters
        Retrieve dsm parameters.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameters')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_event_sources_log_source_management_log_source_types_dsm_parameters_by_id(self, id, **kwargs):
        """
        DELETE /config/event_sources/log_source_management/log_source_types/dsm_parameters/{id}
        Deletes a dsm paramater by ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameters/{id}'.format(
                                        id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_types_dsm_parameters_by_id(self, id, *, dsm_paramaters,
                                                                                       fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_types/dsm_parameters/{id}
        Update a dsm parameter by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameters/{id}'.format(
                                        id=id))
        return self._call('POST', function_endpoint, json=dsm_paramaters, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_types_dsm_parameters_by_id(self, id, *, fields=None,
                                                                                      **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/dsm_parameters/{id}
        Retrieve a dsm parameter by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/dsm_parameters/{id}'.format(
                                        id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_types_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/{id}
        Retrieves a log source type by ID. If called by a user/authorized service with System Administrator, Security Admin, or Manage Log Source Types permissions, then all fields will be returned for the log source type. If called by a less privileged client, only name and ID are returned for the log source type.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_types_by_id(self, id, *, log_source_type_data, fields=None,
                                                                        **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_types/{id}
        Updates a log source type by ID.

        The following fields can be provided in the body of this request, all other log source type fields will be ignored:

        name - String - The name of the log source type. Cannot be empty. Must be 241 characters or less. Must not have been used before. This is only editable for custom log source types.
        protocol_types - Array - The protocols that can be used for the log source type. All protocol ids must exist, list cannot be empty. This is only editable for custom log source types.
        default_protocol_id - Long - The protocol option that should be the default solution for this log source type.
        log_source_extension_id - Long - The log source extension that is associated with the log source type. If specified, this must correspond to an existing log source extension. This field can have a value of 'null', which will remove the extension on this log source type.

        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=log_source_type_data, **kwargs)

    def delete_event_sources_log_source_management_log_source_types_by_id(self, id, **kwargs):
        """
        DELETE /config/event_sources/log_source_management/log_source_types/{id}
        Deletes a custom log source type by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('x_qrd-encryption_algorithm', 'x_qrd-encryption_password', 'Range')
    @request_vars('filter', 'sort', 'fields')
    def get_event_sources_log_source_management_log_sources(self, *, x_qrd_encryption_algorithm=None,
                                                            x_qrd_encryption_password=None, filter=None, sort=None,
                                                            Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_sources
        Retrieves a list of log sources.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources')
        return self._call('GET', function_endpoint, **kwargs)

    def patch_event_sources_log_source_management_log_sources(self, *, log_source_data, **kwargs):
        """
        PATCH /config/event_sources/log_source_management/log_sources
        See api_mapping.xml
        """
        if not isinstance(log_source_data, list):
            log_source_data = [log_source_data]
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources')
        return self._call('PATCH', function_endpoint, response_type='text/plain', json=log_source_data, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_sources(self, *, log_source_data, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_sources
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources')
        return self._call('POST', function_endpoint, json=log_source_data, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_sources_by_id(self, id, *, log_source_data, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_sources/{id}
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=log_source_data, **kwargs)

    @header_vars('x_qrd_encryption_algorithm', 'x_qrd_encryption_password')
    @request_vars('fields')
    def get_event_sources_log_source_management_log_sources_by_id(self, id, *, x_qrd_encryption_algorithm=None,
                                                                  x_qrd_encryption_password=None, fields=None,
                                                                  **kwargs):
        """
        GET /config/event_sources/log_source_management/log_sources/{id}
        Retrieves a log source by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_event_sources_log_source_management_log_sources_by_id(self, id, **kwargs):
        """
        DELETE /config/event_sources/log_source_management/log_sources/{id}
        Deletes a log source by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_protocol_types(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/protocol_types
        Retrieves the list of protocol types. Requires the System Administrator, Security Admin, or Manage Log Sources permission.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/protocol_types')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_protocol_types_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/protocol_types/{id}
        Retrieves a protocol type by ID. Requires the System Administrator, Security Admin, or Manage Log Sources permission.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/protocol_types/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_property_discovery_profiles(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/property_discovery_profiles
        Gets all PropertyDiscoveryProfiles currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_property_discovery_profiles(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/property_discovery_profiles
        Creates a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile JSON object.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_event_sources_property_discovery_profiles_by_id(self, id, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/property_discovery_profiles/{id}
        Updates a PropertyDiscoveryProfile based on the information supplied via the property_discovery_profile JSON object.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def delete_event_sources_property_discovery_profiles_by_id(self, id, **kwargs):
        """
        DELETE /config/event_sources/property_discovery_profiles/{id}
        Deletes the specified PropertyDiscoveryProfile.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_sources_property_discovery_profiles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/property_discovery_profiles/{id}
        Gets a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile corresponding to the supplied ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_wincollect_wincollect_agents(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_agents
        Retrieves a list of WinCollect agents.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/wincollect/wincollect_agents')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_wincollect_wincollect_agents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_agents/{id}
        Retrieves a WinCollect agent by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/wincollect/wincollect_agents/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_wincollect_wincollect_destinations(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_destinations
        Retrieves a list of WinCollect destinations.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/wincollect/wincollect_destinations')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_wincollect_wincollect_destinations_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_destinations/{id}
        Retrieves a WinCollect destination by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/wincollect/wincollect_destinations/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_extension_management_extension_export_tasks(self, *, configData, fields=None, **kwargs):
        """
        POST /config/extension_management/extension_export_tasks
        Exports an extension.
        """
        function_endpoint = urljoin(self._baseurl, 'extension_management/extension_export_tasks')
        return self._call('POST', function_endpoint, json=configData, **kwargs)

    @request_vars('fields')
    def get_extension_management_extension_export_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/extension_management/extension_export_tasks/{task_id}
        Retrieves the tasks status based on the task_id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extension_export_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    def get_extension_management_extension_export_tasks_extension_export_by_task_id(self, task_id, **kwargs):
        """
        GET /config/extension_management/extension_export_tasks/{task_id}/extension_export
        Retrieves the exported extension based on the task_id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extension_export_tasks/{task_id}/extension_export'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, response_type='application/zip', **kwargs)

    @request_vars('fields')
    def get_extension_management_extension_export_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/extension_management/extension_export_tasks/{task_id}/results
        Retrieves the tasks status results based on the task_id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extension_export_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_extension_management_extensions(self, *, file, fields=None, **kwargs):
        """
        POST /config/extension_management/extensions
        Uploads the supplied extension file to the QRadar system.
        """
        function_endpoint = urljoin(self._baseurl, 'extension_management/extensions')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'application/x-gzip'}, data=file,
                          **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'sort', 'fields')
    def get_extension_management_extensions(self, *, filter=None, sort=None, Range=None, fields=None, **kwargs):
        """
        GET /config/extension_management/extensions
        Retrieve a list of extensions.
        """
        function_endpoint = urljoin(self._baseurl, 'extension_management/extensions')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('action_type', 'overwrite', 'fields')
    def post_extension_management_extensions_v2_by_extension_id(self, extension_id, *, action_type, overwrite=None,
                                                                fields=None, **kwargs):
        """
        POST /config/extension_management/extensions/v2/{extension_id}
        Install an extension based on the supplied extension_id. This is an asynchronous action.
        """
        function_endpoint = urljoin(self._baseurl, 'extension_management/extensions/v2/{extension_id}'.format(
            extension_id=extension_id))
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('fields')
    def delete_extension_management_extensions_by_extension_id(self, extension_id, *, configData, fields=None,
                                                               **kwargs):
        """
        DELETE /config/extension_management/extensions/{extension_id}
        Uninstall an extension based on the supplied extension_id. This is an asynchronous action.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extensions/{extension_id}'.format(extension_id=extension_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('action_type', 'overwrite', 'fields')
    def post_extension_management_extensions_by_extension_id(self, extension_id, *, action_type, overwrite=None,
                                                             fields=None, **kwargs):
        """
        POST /config/extension_management/extensions/{extension_id}
        Install an extension based on the supplied extension_id. This is an asynchronous action.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extensions/{extension_id}'.format(extension_id=extension_id))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_extension_management_extensions_by_extension_id(self, extension_id, *, fields=None, **kwargs):
        """
        GET /config/extension_management/extensions/{extension_id}
        Retrieves an extension based on the supplied extension_id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extensions/{extension_id}'.format(extension_id=extension_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_extension_management_extensions_metadata_by_extension_id(self, extension_id, *, metadata, fields=None,
                                                                      **kwargs):
        """
        POST /config/extension_management/extensions/{extension_id}/metadata
        Adds metadata to the Extension corresponding to the supplied extension_id.
        """
        function_endpoint = urljoin(self._baseurl, 'extension_management/extensions/{extension_id}/metadata'.format(
            extension_id=extension_id))
        return self._call('POST', function_endpoint, json=metadata, **kwargs)

    @request_vars('fields')
    def get_extension_management_extensions_task_status_by_status_id(self, status_id, *, fields=None, **kwargs):
        """
        GET /config/extension_management/extensions_task_status/{status_id}
        Retrieves the tasks status based on the status_id.
        """
        function_endpoint = urljoin(self._baseurl, 'extension_management/extensions_task_status/{status_id}'.format(
            status_id=status_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_extension_management_extensions_task_status_results_by_status_id(self, status_id, *, fields=None, **kwargs):
        """
        GET /config/extension_management/extensions_task_status/{status_id}/results
        Retrieves the tasks status results based on the status_id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extensions_task_status/{status_id}/results'.format(
                                        status_id=status_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_retention_buckets(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/flow_retention_buckets
        Retrieves a list of flow retention buckets.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_retention_buckets')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_flow_retention_buckets_by_id(self, id, **kwargs):
        """
        DELETE /config/flow_retention_buckets/{id}
        Deletes a flow retention bucket.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_retention_buckets/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_flow_retention_buckets_by_id(self, id, *, retention_bucket, fields=None, **kwargs):
        """
        POST /config/flow_retention_buckets/{id}
        Updates the flow retention bucket owner, or enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_retention_buckets/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=retention_bucket, **kwargs)

    @request_vars('fields')
    def get_flow_retention_buckets_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/flow_retention_buckets/{id}
        Retrieves a flow retention bucket.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_retention_buckets/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_properties_dep_by_aql_property_id(self, aql_property_id, *, fields=None,
                                                                                 **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_properties/dep/{aql_property_id}
        Retrieves a AQL flow property based on the supplied AQL property ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_properties/dep/{aql_property_id}'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_properties_by_aql_property_id(self, aql_property_id, *, fields=None,
                                                                             **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_properties/{aql_property_id}
        Retrieves a AQL flow property based on the supplied AQL property ID.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_properties/{aql_property_id}'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_properties_dependents_by_aql_property_id(self, aql_property_id, *,
                                                                                        fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_properties/{aql_property_id}/dependents
        Retrieves the objects that depend on the flow AQL property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_properties/{aql_property_id}/dependents'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_properties_dependents_disable_by_aql_property_id(self, aql_property_id,
                                                                                                *, fields=None,
                                                                                                **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_properties/{aql_property_id}/dependents/disable
        Retrieves the objects that depend on the flow AQL property.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_properties/{aql_property_id}/dependents/disable'.format(
                                        aql_property_id=aql_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_sources_custom_properties_aql_property_by_aql_property_name(self, aql_property_name, *, filter=None,
                                                                             Range=None, fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_property/{aql_property_name}
        Retrieves a flow AQL property by it's name.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_property/{aql_property_name}'.format(
                                        aql_property_name=aql_property_name))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                           fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}
        Retrieves the status of the flow AQL property dependents task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_aql_property_dependent_tasks_disable_by_task_id(self, task_id, *, task,
                                                                                            fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}
        Cancels the flow AQL property dependent task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_property_dependent_tasks_disable_results_by_task_id(self, task_id, *,
                                                                                                   fields=None,
                                                                                                   **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}/results
        Retrieves the aql property dependent task results.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_property_dependent_tasks/disable/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, task, fields=None,
                                                                                    **kwargs):
        """
        POST /config/flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}
        Cancels the flow AQL property dependent task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_property_dependent_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                   **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}
        Retrieves the status of the flow AQL property dependents task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_aql_property_dependent_tasks_results_by_task_id(self, task_id, *,
                                                                                           fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}/results
        Retrieves the aql property dependent task results.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/aql_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_calculated_properties(self, *, data, fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/calculated_properties
        Creates a new calculated flow property.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/calculated_properties')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_sources_custom_properties_calculated_properties(self, *, filter=None, Range=None, fields=None,
                                                                 **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_properties
        Retrieves a list of calculated flow properties.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/calculated_properties')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_properties_dep_by_calculated_property_id(self,
                                                                                               calculated_property_id,
                                                                                               *, fields=None,
                                                                                               **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_properties/dep/{calculated_property_id}
        Retrieves a calculated flow property based on the supplied calculated property ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_properties/dep/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_flow_sources_custom_properties_calculated_properties_by_calculated_property_id(self,
                                                                                              calculated_property_id, *,
                                                                                              fields=None, **kwargs):
        """
        DELETE /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}
        Deletes the flow calculated property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task to do is started for this check.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_properties/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_properties_by_calculated_property_id(self, calculated_property_id,
                                                                                           *, fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}
        Retrieves a calculated flow property based on the supplied calculated property ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_properties/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_calculated_properties_by_calculated_property_id(self,
                                                                                            calculated_property_id, *,
                                                                                            data, fields=None,
                                                                                            **kwargs):
        """
        POST /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}
        Updates an existing calculated flow property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_properties/{calculated_property_id}'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_properties_dependents_by_calculated_property_id(self,
                                                                                                      calculated_property_id,
                                                                                                      *, fields=None,
                                                                                                      **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents
        Retrieves the objects that depend on the flow calculated property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_properties_dependents_change_field_type_by_calculated_property_id(
            self, calculated_property_id, *, fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/change_field_type
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/change_field_type'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_properties_dependents_disable_by_calculated_property_id(self,
                                                                                                              calculated_property_id,
                                                                                                              *,
                                                                                                              fields=None,
                                                                                                              **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable
        Retrieves the objects that depend on the flow calculated property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_properties/{calculated_property_id}/dependents/disable'.format(
                                        calculated_property_id=calculated_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_sources_custom_properties_calculated_property_by_calculated_property_name(self,
                                                                                           calculated_property_name, *,
                                                                                           filter=None, Range=None,
                                                                                           fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property/{calculated_property_name}
        Retrieves a list of flow calculated properties.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property/{calculated_property_name}'.format(
                                        calculated_property_name=calculated_property_name))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_property_delete_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                       **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_delete_tasks/{task_id}
        Retrieves the status of the flow calculated property delete task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_delete_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self,
                                                                                                             task_id, *,
                                                                                                             task,
                                                                                                             fields=None,
                                                                                                             **kwargs):
        """
        POST /config/flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_by_task_id(self,
                                                                                                            task_id, *,
                                                                                                            fields=None,
                                                                                                            **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_property_dependent_tasks_change_field_type_results_by_task_id(
            self, task_id, *, fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}/results
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/change_field_type/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                                  fields=None,
                                                                                                  **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}
        Retrieves the flow calculated property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                                   task, fields=None,
                                                                                                   **kwargs):
        """
        POST /config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}
        Cancels the calculated property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_property_dependent_tasks_disable_results_by_task_id(self, task_id,
                                                                                                          *,
                                                                                                          fields=None,
                                                                                                          **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results
        Retrieves the calculated property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/disable/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *, task,
                                                                                           fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}
        Cancels the flow calculated property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_property_dependent_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                          **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}
        Retrieves the status of the flow calculated property dependents task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_calculated_property_dependent_tasks_results_by_task_id(self, task_id, *,
                                                                                                  fields=None,
                                                                                                  **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results
        Retrieves the calculated property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/calculated_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter')
    def get_flow_sources_custom_properties_calculated_property_operands(self, *, filter=None, Range=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_property_operands
        Retrieves the list of available options for calculated flow property operand.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/calculated_property_operands')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_property_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/property_expressions
        Creates a new flow regex property expression.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/property_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_sources_custom_properties_property_expressions(self, *, filter=None, Range=None, fields=None,
                                                                **kwargs):
        """
        GET /config/flow_sources/custom_properties/property_expressions
        Retrieve a list of flow regex property expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/property_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, data,
                                                                                  fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/property_expressions/{expression_id}
        Updates an existing flow regex property expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, fields=None,
                                                                                 **kwargs):
        """
        GET /config/flow_sources/custom_properties/property_expressions/{expression_id}
        Retrieves a flow regex property expression based on the supplied expression ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_flow_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, **kwargs):
        """
        DELETE /config/flow_sources/custom_properties/property_expressions/{expression_id}
        Deletes a flow regex property expression based on the supplied expression ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_flow_sources_custom_properties_regex_properties(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_properties
        Retrieves a list of flow regex properties.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/regex_properties')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_regex_properties(self, *, data, fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/regex_properties
        Creates a new flow regex property.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/regex_properties')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *, data,
                                                                                  fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/regex_properties/{regex_property_id}
        Updates an existing flow regex property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_properties/{regex_property_id}'.format(
                                        regex_property_id=regex_property_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *,
                                                                                 fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}
        Retrieves a flow regex property based on the supplied regex property ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_properties/{regex_property_id}'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_flow_sources_custom_properties_regex_properties_by_regex_property_id(self, regex_property_id, *,
                                                                                    fields=None, **kwargs):
        """
        DELETE /config/flow_sources/custom_properties/regex_properties/{regex_property_id}
        Deletes a flow regex property. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task is started to do this check.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_properties/{regex_property_id}'.format(
                                        regex_property_id=regex_property_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_properties_dependents_by_regex_property_id(self, regex_property_id, *,
                                                                                            fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents
        Retrieves the objects that depend on the flow regex property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_properties_dependents_change_field_type_by_regex_property_id(self,
                                                                                                              regex_property_id,
                                                                                                              *,
                                                                                                              fields=None,
                                                                                                              **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type
        Retrieves the objects that depend on the flow regex property for changing type of field for it.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_properties/{regex_property_id}/dependents/change_field_type'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_properties_disabling_dependents_by_regex_property_id(self,
                                                                                                      regex_property_id,
                                                                                                      *, fields=None,
                                                                                                      **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_properties/{regex_property_id}/disabling_dependents
        Retrieves the objects that depend on the flow regex property.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_properties/{regex_property_id}/disabling_dependents'.format(
                                        regex_property_id=regex_property_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_property_delete_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                  **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_property_delete_tasks/{task_id}
        Retrieves the flow regex property delete task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_delete_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id,
                                                                                                        *, task,
                                                                                                        fields=None,
                                                                                                        **kwargs):
        """
        POST /config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}
        Cancels the regex property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_by_task_id(self, task_id, *,
                                                                                                       fields=None,
                                                                                                       **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}
        Retrieves the flow regex property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_property_dependent_tasks_change_field_type_results_by_task_id(self,
                                                                                                               task_id,
                                                                                                               *,
                                                                                                               fields=None,
                                                                                                               **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results
        Retrieves the regex property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/change_field_type/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *,
                                                                                             fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}
        Retrieves the flow regex property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_regex_property_dependent_tasks_disable_by_task_id(self, task_id, *, task,
                                                                                              fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}
        Cancels the regex property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_property_dependent_tasks_disable_results_by_task_id(self, task_id, *,
                                                                                                     fields=None,
                                                                                                     **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results
        Retrieves the regex property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/disable/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, fields=None,
                                                                                     **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}
        Retrieves the flow regex property dependent task status.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_regex_property_dependent_tasks_by_task_id(self, task_id, *, task,
                                                                                      fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}
        Cancels the flow regex property dependent task.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}'.format(
                                        task_id=task_id))
        return self._call('POST', function_endpoint, json=task, **kwargs)

    @request_vars('fields')
    def get_flow_sources_custom_properties_regex_property_dependent_tasks_results_by_task_id(self, task_id, *,
                                                                                             fields=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results
        Retrieves the regex property dependent task results.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/regex_property_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_gatewaytoken_client_configurations(self, *, fields=None, **kwargs):
        """
        GET /config/gatewaytoken/client_configurations
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'gatewaytoken/client_configurations')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_sources_log_source_group_delete_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/log_sources/log_source_group_delete_tasks/{task_id}
        Retrieves the delete log source group task status.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'log_sources/log_source_group_delete_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_sources_log_source_group_dependent_tasks_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/log_sources/log_source_group_dependent_tasks/{task_id}
        Retrieves the dependent log source group task status.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'log_sources/log_source_group_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_log_sources_log_source_group_dependent_tasks_by_task_id(self, task_id, *, task, fields=None, **kwargs):
        """
        POST /config/log_sources/log_source_group_dependent_tasks/{task_id}
        Cancels the dependent the log source group task.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'log_sources/log_source_group_dependent_tasks/{task_id}'.format(task_id=task_id))
        return self._call('POST', function_endpoint, json=task, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_sources_log_source_group_dependent_tasks_results_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/log_sources/log_source_group_dependent_tasks/{task_id}/results
        Retrieves the log source group dependent task results.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'log_sources/log_source_group_dependent_tasks/{task_id}/results'.format(
                                        task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_log_sources_log_source_groups(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/log_sources/log_source_groups
        Retrieves a list of log source groups.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/log_source_groups')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_log_sources_log_source_groups(self, *, log_source_group, fields=None, **kwargs):
        """
        POST /config/log_sources/log_source_groups
        Creates a log source group.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/log_source_groups')
        return self._call('POST', function_endpoint, json=log_source_group, headers=headers, **kwargs)

    @header_vars('fields')
    def post_log_sources_log_source_groups_by_group_id(self, group_id, *, log_source_group, fields=None, **kwargs):
        """
        POST /config/log_sources/log_source_groups/{group_id}
        Updates a log source group.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/log_source_groups/{group_id}'.format(group_id=group_id))
        return self._call('POST', function_endpoint, json=log_source_group, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_log_sources_log_source_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        DELETE /config/log_sources/log_source_groups/{group_id}
        Deletes a log source group. To ensure safe deletion, a dependency check is carried out. This check might take some time. An asynchronous task is started to do this check.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/log_source_groups/{group_id}'.format(group_id=group_id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_sources_log_source_groups_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /config/log_sources/log_source_groups/{group_id}
        Retrieves a log source group.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/log_source_groups/{group_id}'.format(group_id=group_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_sources_log_source_groups_dependents_by_group_id(self, group_id, *, fields=None, **kwargs):
        """
        GET /config/log_sources/log_source_groups/{group_id}/dependents
        Retrieves the objects that depend on the log source group.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'log_sources/log_source_groups/{group_id}/dependents'.format(group_id=group_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_network_hierarchy_networks(self, *, fields=None, **kwargs):
        """
        GET /config/network_hierarchy/networks
        Retrieves the deployed network hierarchy.
        """
        function_endpoint = urljoin(self._baseurl, 'network_hierarchy/networks')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_network_hierarchy_staged_networks(self, *, fields=None, **kwargs):
        """
        GET /config/network_hierarchy/staged_networks
        Retrieves the staged network hierarchy.
        """
        function_endpoint = urljoin(self._baseurl, 'network_hierarchy/staged_networks')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def put_network_hierarchy_staged_networks(self, *, network_hierarchy, fields=None, **kwargs):
        """
        PUT /config/network_hierarchy/staged_networks
        Replaces the current network hierarchy with the input that is provided.
        """
        function_endpoint = urljoin(self._baseurl, 'network_hierarchy/staged_networks')
        return self._call('PUT', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_remote_networks(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/remote_networks
        Retrieves a list of deployed remote networks.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_remote_networks_by_network_id(self, network_id, *, fields=None, **kwargs):
        """
        GET /config/remote_networks/{network_id}
        Retrieves a deployed remote network by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_networks/{network_id}'.format(network_id=network_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_remote_services(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/remote_services
        Retrieves a list of deployed remote services.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_remote_services_by_service_id(self, service_id, *, fields=None, **kwargs):
        """
        GET /config/remote_services/{service_id}
        Retrieves a deployed remote service by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'remote_services/{service_id}'.format(service_id=service_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_resource_restriction_users_by_tenant_by_tenant_id(self, tenant_id, *, filter=None, Range=None, fields=None,
                                                              **kwargs):
        """
        GET /config/resource_restriction/users_by_tenant/{tenant_id}
        Retrieve a list of all resource restrictions
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'resource_restriction/users_by_tenant/{tenant_id}'.format(tenant_id=tenant_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_resource_restrictions(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/resource_restrictions
        Retrieves a list of all resource restrictions.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_resource_restrictions(self, *, resourceRestriction, fields=None, **kwargs):
        """
        POST /config/resource_restrictions
        Creates a new resource restriction.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions')
        return self._call('POST', function_endpoint, json=resourceRestriction, **kwargs)

    @request_vars('fields')
    def get_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, *, fields=None, **kwargs):
        """
        GET /config/resource_restrictions/{resource_restriction_id}
        Retrieves a resource restriction consumer by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions/{resource_restriction_id}'.format(
            resource_restriction_id=resource_restriction_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def put_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, *, resourceRestriction,
                                                             fields=None, **kwargs):
        """
        PUT /config/resource_restrictions/{resource_restriction_id}
        Updates a resource restriction consumer by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions/{resource_restriction_id}'.format(
            resource_restriction_id=resource_restriction_id))
        return self._call('PUT', function_endpoint, **kwargs)

    def delete_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, **kwargs):
        """
        DELETE /config/resource_restrictions/{resource_restriction_id}
        Deletes a resource restriction consumer by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions/{resource_restriction_id}'.format(
            resource_restriction_id=resource_restriction_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_selective_forwarding_destinations(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/selective_forwarding/destinations
        Get all Selective Forwarding Destinations
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/destinations')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_selective_forwarding_destinations(self, *, data, **kwargs):
        """
        POST /config/selective_forwarding/destinations
        Creates a new Destination with the fields supplied in the body parameter
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/destinations')
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @request_vars('fields')
    def get_selective_forwarding_destinations_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/selective_forwarding/destinations/{id}
        Retrieve a destination by ID
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/destinations/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_selective_forwarding_destinations_by_id(self, id, *, data, **kwargs):
        """
        POST /config/selective_forwarding/destinations/{id}
        delete a Selective Forwarding Destination
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/destinations/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    def delete_selective_forwarding_destinations_by_id(self, id, **kwargs):
        """
        DELETE /config/selective_forwarding/destinations/{id}
        delete a Selective Forwarding Destination
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/destinations/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_selective_forwarding_routes(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/selective_forwarding/routes
        Returns all Routing Rules in the system, ordered by creation date
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_selective_forwarding_routes(self, *, data, **kwargs):
        """
        POST /config/selective_forwarding/routes
        Creates a new Routing Rule with the fields supplied in the body parameter
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes')
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    def delete_selective_forwarding_routes_by_id(self, id, **kwargs):
        """
        DELETE /config/selective_forwarding/routes/{id}
        Deletes a Routing Rule with the the given ID
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('fields')
    def get_selective_forwarding_routes_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/selective_forwarding/routes/{id}
        retrieve route by ID
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_selective_forwarding_routes_by_id(self, id, *, data, **kwargs):
        """
        POST /config/selective_forwarding/routes/{id}
        Updates a Routing Rule based on ID with the fields supplied in the body parameter
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_store_and_forward_policies(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/store_and_forward/policies
        Retrieves a list of store and forward policies.
        """
        function_endpoint = urljoin(self._baseurl, 'store_and_forward/policies')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_store_and_forward_policies_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/store_and_forward/policies/{id}
        Retrieves a store and forward policy.
        """
        function_endpoint = urljoin(self._baseurl, 'store_and_forward/policies/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_store_and_forward_policies_by_id(self, id, *, policy, fields=None, **kwargs):
        """
        POST /config/store_and_forward/policies/{id}
        Updates the store and forward policy owner only.
        """
        function_endpoint = urljoin(self._baseurl, 'store_and_forward/policies/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=policy, **kwargs)

    def delete_store_and_forward_policies_by_id(self, id, **kwargs):
        """
        DELETE /config/store_and_forward/policies/{id}
        Deletes a store and forward policy.
        """
        function_endpoint = urljoin(self._baseurl, 'store_and_forward/policies/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    def get_vpn_client_configuration(self, **kwargs):
        """
        GET /config/vpn/client_configuration
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'vpn/client_configuration')
        return self._call('GET', function_endpoint, response_type='application/zip', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_vpn_client_configurations(self, *, filter=None, Range=None, fields=None, **kwargs):
        """
        GET /config/vpn/client_configurations
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'vpn/client_configurations')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
