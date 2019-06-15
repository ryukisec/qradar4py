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
    @request_vars('fields', 'filter')
    def get_access_authorized_services(self, *, Range=None, fields=None, filter=None, **kwargs):
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
    @request_vars('fields', 'filter')
    def get_access_roles(self, *, Range=None, fields=None, filter=None, **kwargs):
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
    @request_vars('fields', 'filter')
    def get_access_staged_authorized_services(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/access/staged_authorized_services
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_authorized_services')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_access_staged_roles(self, *, Range=None, fields=None, filter=None, **kwargs):
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
    def get_access_staged_roles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/staged_roles/{id}
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/staged_roles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

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

    @header_vars('fields')
    def post_access_tenant_management_tenants(self, *, tenant, fields=None, **kwargs):
        """
        POST /config/access/tenant_management/tenants
        Create a new tenant.
        """
        function_endpoint = urljoin(self._baseurl, 'access/tenant_management/tenants')
        return self._call('POST', function_endpoint, json=tenant, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_access_tenant_management_tenants(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/access/tenant_management/tenants
        Retrieve the list of all tenants ordered by tenant id.
        """
        function_endpoint = urljoin(self._baseurl, 'access/tenant_management/tenants')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_access_tenant_management_tenants_by_tenant_id(self, tenant_id, **kwargs):
        """
        DELETE /config/access/tenant_management/tenants/{tenant_id}
        Delete a tenant.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'access/tenant_management/tenants/{tenant_id}'.format(tenant_id=tenant_id))
        return self._call('DELETE', function_endpoint, **kwargs)

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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_access_users(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/access/users
        Retrieves a list of deployed users.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_users_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/users/{id}
        Retrieves a deployed user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_access_users_dependents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/access/users/{id}/dependents
        Retrieves the objects that depend on the user.
        """
        function_endpoint = urljoin(self._baseurl, 'access/users/{id}/dependents'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('capabilities', 'fields', 'filter')
    def get_access_users_with_capability_filter(self, *, capabilities, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/access/users_with_capability_filter
        Retrieves a list of deployed users.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'access/users_with_capability_filter')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_access_control_roles(self, *, Range=None, fields=None, filter=None, **kwargs):
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
    @request_vars('fields', 'filter')
    def get_access_control_users(self, *, Range=None, fields=None, filter=None, **kwargs):
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
    @request_vars('fields', 'filter')
    def get_deployment_components(self, *, fields=None, filter=None, Range=None, **kwargs):
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
    @request_vars('fields', 'filter')
    def get_deployment_hosts(self, *, fields=None, filter=None, Range=None, **kwargs):
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

    @request_vars('fields')
    def get_deployment_license_pool(self, *, fields=None, **kwargs):
        """
        GET /config/deployment/license_pool
        Retrieves the deployed license pool information.
        """
        function_endpoint = urljoin(self._baseurl, 'deployment/license_pool')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_deployment_licenses(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/deployment/licenses
        Get a list of License and information form the encrypted file.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/licenses')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_deployment_natgroups(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/deployment/natgroups
        Get deployment NAT groups.  If no NAT groups exist an empty list will be returned.

        Nat Group Structure

        id
        - The unique id of the NAT group in the deployment.

        name
        - The unique name of the NAT group in the deployment.

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

        id
        - The unique id of the NAT group in the deployment.

        name
        - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/natgroups/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_node_details_by_node_ip(self, node_ip, *, fields=None, **kwargs):
        """
        GET /config/deployment/node_details/{node_ip}
        Retrieves the node installation details
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/node_details/{node_ip}'.format(node_ip=node_ip))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_node_modification_task_by_task_id(self, task_id, *, fields=None, **kwargs):
        """
        GET /config/deployment/node_modification_task/{task_id}
        Retrieves the task status for a node task
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'deployment/node_modification_task/{task_id}'.format(task_id=task_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_deployment_nodes(self, *, node, fields=None, **kwargs):
        """
        POST /config/deployment/nodes
        Create and deploy a node
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/nodes')
        return self._call('POST', function_endpoint, json=node, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_deployment_nodes(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /config/deployment/nodes
        Retrieve a list of nodes.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/nodes')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_nodes_hostkeys_by_ip(self, ip, *, fields=None, **kwargs):
        """
        GET /config/deployment/nodes/hostkeys/{ip}
        Retrieves the node host key
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/nodes/hostkeys/{ip}'.format(ip=ip))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_nodes_by_node_id(self, node_id, *, fields=None, **kwargs):
        """
        GET /config/deployment/nodes/{node_id}
        Retrieves a node based on the supplied node_id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/nodes/{node_id}'.format(node_id=node_id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def delete_deployment_nodes_by_node_id(self, node_id, *, removal_type, fields=None, **kwargs):
        """
        DELETE /config/deployment/nodes/{node_id}
        Delete a node
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/nodes/{node_id}'.format(node_id=node_id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_deployment_staged_components(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/deployment/staged_components
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_components')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

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
    def get_deployment_staged_components_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/staged_components/{id}
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_components/{id}'.format(id=id))
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

    @header_vars('Range')
    @request_vars('showall', 'fields', 'filter')
    def get_deployment_staged_hosts(self, *, showall=None, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/deployment/staged_hosts
        See api_mapping.xml
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_hosts')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_deployment_staged_natgroups(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/deployment/staged_natgroups
        See api_mapping.xml
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

        id
        - The unique id of the NAT group in the deployment.

        name
        - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_deployment_staged_natgroups_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/deployment/staged_natgroups/{id}
        Get NAT group by id. If staging directory does not exist will return the deployed NAT group.

        Nat Group Structure

        id
        - The unique id of the NAT group in the deployment.

        name
        - The unique name of the NAT group in the deployment.

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

        id
        - The unique id of the NAT group in the deployment.

        name
        - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('name', 'fields')
    def post_deployment_staged_natgroups_by_id(self, id, *, name, fields=None, **kwargs):
        """
        POST /config/deployment/staged_natgroups/{id}
        Edit a NAT group.

        Nat Group Structure

        id
        - The unique id of the NAT group in the deployment.

        name
        - The unique name of the NAT group in the deployment.

        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'deployment/staged_natgroups/{id}'.format(id=id))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

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

    @header_vars('fields')
    def post_domain_management_domains(self, *, domain, fields=None, **kwargs):
        """
        POST /config/domain_management/domains
        Creates a new domain.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains')
        return self._call('POST', function_endpoint, json=domain, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_domain_management_domains(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/domain_management/domains
        Retrieves the list of all domains, active and deleted (including the default one).
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_domain_management_domains_by_domain_id(self, domain_id, *, fields=None, **kwargs):
        """
        DELETE /config/domain_management/domains/{domain_id}
        Deletes a domain by domain id.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains/{domain_id}'.format(domain_id=domain_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_domain_management_domains_by_domain_id(self, domain_id, *, fields=None, **kwargs):
        """
        GET /config/domain_management/domains/{domain_id}
        Retrieves a domain by domain id.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains/{domain_id}'.format(domain_id=domain_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_domain_management_domains_by_domain_id(self, domain_id, *, domain, fields=None, **kwargs):
        """
        POST /config/domain_management/domains/{domain_id}
        Updates an existing domain.
        """
        function_endpoint = urljoin(self._baseurl, 'domain_management/domains/{domain_id}'.format(domain_id=domain_id))
        return self._call('POST', function_endpoint, json=domain, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_retention_buckets(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/event_retention_buckets
        Retrieves a list of event retention buckets.
        """
        function_endpoint = urljoin(self._baseurl, 'event_retention_buckets')
        return self._call('GET', function_endpoint, **kwargs)

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

    @header_vars('fields')
    def post_event_retention_buckets_by_id(self, id, *, retention_bucket, fields=None, **kwargs):
        """
        POST /config/event_retention_buckets/{id}
        Updates the event retention bucket owner or enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl, 'event_retention_buckets/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=retention_bucket, **kwargs)

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
    @request_vars('fields', 'filter')
    def get_event_sources_custom_properties_calculated_properties(self, *, fields=None, filter=None, Range=None,
                                                                  **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties
        Retrieves a list of calculated event properties.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/calculated_properties')
        return self._call('GET', function_endpoint, **kwargs)

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
    def get_event_sources_custom_properties_calculated_properties_by_calculated_property_id(self,
                                                                                            calculated_property_id, *,
                                                                                            fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/calculated_properties/{calculated_property_id}
        Retrieves a calculated event property based on the supplied calculated property ID.
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

    @header_vars('fields')
    def post_event_sources_custom_properties_property_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_expressions
        Creates a new event regex property expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_custom_properties_property_expressions(self, *, fields=None, filter=None, Range=None,
                                                                 **kwargs):
        """
        GET /config/event_sources/custom_properties/property_expressions
        Retrieves a list of event regex property expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_expressions')
        return self._call('GET', function_endpoint, **kwargs)

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

    def delete_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_expressions/{expression_id}
        Deletes an event regex property expression based on the supplied expression ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, *, fields=None,
                                                                                  **kwargs):
        """
        GET /config/event_sources/custom_properties/property_expressions/{expression_id}
        Retrieves an event regex property expression based on the supplied expression ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_custom_properties_property_json_expressions(self, *, fields=None, filter=None, Range=None,
                                                                      **kwargs):
        """
        GET /config/event_sources/custom_properties/property_json_expressions
        Retrieves a list of Ariel property JSON expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_json_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_json_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_json_expressions
        Creates a new Ariel property JSON expression.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/custom_properties/property_json_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('fields')
    def post_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id, *, data,
                                                                                        fields=None, **kwargs):
        """
        POST /config/event_sources/custom_properties/property_json_expressions/{expression_id}
        Updates an existing Ariel property JSON expression.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_json_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @request_vars('fields')
    def get_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id, *,
                                                                                       fields=None, **kwargs):
        """
        GET /config/event_sources/custom_properties/property_json_expressions/{expression_id}
        Retrieves an Ariel property JSON expression based on the supplied expression ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_json_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_event_sources_custom_properties_property_json_expressions_by_expression_id(self, expression_id,
                                                                                          **kwargs):
        """
        DELETE /config/event_sources/custom_properties/property_json_expressions/{expression_id}
        Deletes an Ariel property JSON expression based on the supplied expression ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/custom_properties/property_json_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_custom_properties_regex_properties(self, *, fields=None, filter=None, Range=None, **kwargs):
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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_event_collectors(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/event_sources/event_collectors
        Retrieves the list of event collectors.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/event_collectors')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_event_collectors_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/event_collectors/{id}
        Retrieves an individual event collector by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/event_collectors/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_log_source_extensions(self, *, fields=None, filter=None, Range=None, **kwargs):
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

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_event_sources_log_source_management_autodetection_config_records(self, *, filter=None, fields=None,
                                                                             Range=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/autodetection/config_records
        Retrieves the list of Autodetection Config Records.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/autodetection/config_records')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_autodetection_config_records_by_config_id(self, config_id, *,
                                                                                           config_record, fields=None,
                                                                                           **kwargs):
        """
        POST /config/event_sources/log_source_management/autodetection/config_records/{config_id}
        Updates the Autodetection Config Record enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/autodetection/config_records/{config_id}'.format(
                                        config_id=config_id))
        return self._call('POST', function_endpoint, json=config_record, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_autodetection_config_records_by_config_id(self, config_id, *,
                                                                                          fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/autodetection/config_records/{config_id}
        Retrieves an Autodetection Config Record.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/autodetection/config_records/{config_id}'.format(
                                        config_id=config_id))
        return self._call('GET', function_endpoint, **kwargs)

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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_log_source_management_log_source_extensions(self, *, fields=None, filter=None, Range=None,
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
    @request_vars('fields', 'filter')
    def get_event_sources_log_source_management_log_source_groups(self, *, fields=None, filter=None, Range=None,
                                                                  **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_groups
        Retrieves the list of log source groups.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_source_groups')
        return self._call('GET', function_endpoint, **kwargs)

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
    @request_vars('fields', 'filter')
    def get_event_sources_log_source_management_log_source_languages(self, *, fields=None, filter=None, Range=None,
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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_log_source_management_log_source_types(self, *, fields=None, filter=None, Range=None,
                                                                 **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types
        Retrieves the list of log source types.
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

    @header_vars('fields')
    def post_event_sources_log_source_management_log_source_types_by_id(self, id, *, log_source_type_data, fields=None,
                                                                        **kwargs):
        """
        POST /config/event_sources/log_source_management/log_source_types/{id}
        Update a log source type.

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
        Delete a custom log source type by ID. This is only permitted for custom log source types.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_source_types_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_source_types/{id}
        Retrieves a log source type by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/log_source_types/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_event_sources_log_source_management_log_sources(self, *, fields=None, filter=None, sort=None, Range=None,
                                                            **kwargs):
        """
        GET /config/event_sources/log_source_management/log_sources
        Retrieves the list of log sources.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_sources(self, *, log_source_data, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_sources
        See api_mapping.xml
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources')
        return self._call('POST', function_endpoint, json=log_source_data, **kwargs)

    def patch_event_sources_log_source_management_log_sources(self, *, log_source_data, **kwargs):
        """
        PATCH /config/event_sources/log_source_management/log_sources
        See api_mapping.xml
        """
        if not isinstance(log_source_data, list):
            log_source_data = [log_source_data]
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources')
        return self._call('PATCH', function_endpoint, response_type='text/plain', json=log_source_data, **kwargs)

    def delete_event_sources_log_source_management_log_sources_by_id(self, id, **kwargs):
        """
        DELETE /config/event_sources/log_source_management/log_sources/{id}
        Removes the specified log source from the system.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_event_sources_log_source_management_log_sources_by_id(self, id, *, log_source_data, fields=None, **kwargs):
        """
        POST /config/event_sources/log_source_management/log_sources/{id}
        Updates a log source.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=log_source_data, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_log_sources_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/log_sources/{id}
        Retrieves a log source by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/log_sources/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_log_source_management_protocol_types(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/protocol_types
        Retrieves the list of protocol types.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/log_source_management/protocol_types')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_log_source_management_protocol_types_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/log_source_management/protocol_types/{id}
        Retrieves a protocol type by ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/log_source_management/protocol_types/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_event_sources_property_discovery_profiles(self, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/property_discovery_profiles
        Creates a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile JSON object.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_property_discovery_profiles(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/event_sources/property_discovery_profiles
        Gets all PropertyDiscoveryProfiles currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_property_discovery_profiles_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/property_discovery_profiles/{id}
        Gets a PropertyDiscoveryProfile based on the information supplied by the property_discovery_profile corresponding to the supplied ID.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_event_sources_property_discovery_profiles_by_id(self, id, **kwargs):
        """
        DELETE /config/event_sources/property_discovery_profiles/{id}
        Deletes the specified PropertyDiscoveryProfile.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_event_sources_property_discovery_profiles_by_id(self, id, *, data, fields=None, **kwargs):
        """
        POST /config/event_sources/property_discovery_profiles/{id}
        Updates a PropertyDiscoveryProfile based on the information supplied via the property_discovery_profile JSON object.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/property_discovery_profiles/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_wincollect_wincollect_agents(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_agents
        Gets a list of WinCollectAgentDTO based on the rows in the ale_client table
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/wincollect/wincollect_agents')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_wincollect_wincollect_agents_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_agents/{id}
        Gets a WinCollectAgentDTO based on the information supplied via the ale_client
        corresponding to the supplied id.
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/wincollect/wincollect_agents/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_event_sources_wincollect_wincollect_destinations(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_destinations
        Gets a list of WinCollectDestinationDTO based on the rows in the ale_destination table
        """
        function_endpoint = urljoin(self._baseurl, 'event_sources/wincollect/wincollect_destinations')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_event_sources_wincollect_wincollect_destinations_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/event_sources/wincollect/wincollect_destinations/{id}
        Gets a WinCollectDestinationDTO based on the information supplied via the ale_destination
        corresponding to the supplied id.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'event_sources/wincollect/wincollect_destinations/{id}'.format(id=id))
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
    @request_vars('sort', 'fields', 'filter')
    def get_extension_management_extensions(self, *, Range=None, sort=None, fields=None, filter=None, **kwargs):
        """
        GET /config/extension_management/extensions
        Retrieve a list of extensions.
        """
        function_endpoint = urljoin(self._baseurl, 'extension_management/extensions')
        return self._call('GET', function_endpoint, **kwargs)

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
    def delete_extension_management_extensions_by_extension_id(self, extension_id, *, fields=None, **kwargs):
        """
        DELETE /config/extension_management/extensions/{extension_id}
        Uninstall an extension based on the supplied extension_id. This is an asynchronous action.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'extension_management/extensions/{extension_id}'.format(extension_id=extension_id))
        return self._call('DELETE', function_endpoint, **kwargs)

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
    @request_vars('fields', 'filter')
    def get_flow_retention_buckets(self, *, Range=None, fields=None, filter=None, **kwargs):
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

    @request_vars('fields')
    def get_flow_retention_buckets_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /config/flow_retention_buckets/{id}
        Retrieves a flow retention bucket.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_retention_buckets/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_retention_buckets_by_id(self, id, *, retention_bucket, fields=None, **kwargs):
        """
        POST /config/flow_retention_buckets/{id}
        Updates the flow retention bucket owner, or enabled/disabled only.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_retention_buckets/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=retention_bucket, **kwargs)

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
    @request_vars('fields', 'filter')
    def get_flow_sources_custom_properties_calculated_properties(self, *, fields=None, filter=None, Range=None,
                                                                 **kwargs):
        """
        GET /config/flow_sources/custom_properties/calculated_properties
        Retrieves a list of calculated flow properties.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/calculated_properties')
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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_flow_sources_custom_properties_property_expressions(self, *, fields=None, filter=None, Range=None,
                                                                **kwargs):
        """
        GET /config/flow_sources/custom_properties/property_expressions
        Retrieve a list of flow regex property expressions.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/property_expressions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_flow_sources_custom_properties_property_expressions(self, *, data, fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/property_expressions
        Creates a new flow regex property expression.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/property_expressions')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    def delete_flow_sources_custom_properties_property_expressions_by_expression_id(self, expression_id, **kwargs):
        """
        DELETE /config/flow_sources/custom_properties/property_expressions/{expression_id}
        Deletes a flow regex property expression based on the supplied expression ID.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'flow_sources/custom_properties/property_expressions/{expression_id}'.format(
                                        expression_id=expression_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

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

    @header_vars('fields')
    def post_flow_sources_custom_properties_regex_properties(self, *, data, fields=None, **kwargs):
        """
        POST /config/flow_sources/custom_properties/regex_properties
        Creates a new flow regex property.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/regex_properties')
        return self._call('POST', function_endpoint, json=data, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_flow_sources_custom_properties_regex_properties(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/flow_sources/custom_properties/regex_properties
        Retrieves a list of flow regex properties.
        """
        function_endpoint = urljoin(self._baseurl, 'flow_sources/custom_properties/regex_properties')
        return self._call('GET', function_endpoint, **kwargs)

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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_global_system_notifications(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/global_system_notifications
        Retrieves a list of all deployed global system notifications.
        """
        function_endpoint = urljoin(self._baseurl, 'global_system_notifications')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_global_system_notifications_by_notification_id(self, notification_id, *, fields=None, **kwargs):
        """
        GET /config/global_system_notifications/{notification_id}
        Retrieves a deployed global system notification by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'global_system_notifications/{notification_id}'.format(
            notification_id=notification_id))
        return self._call('GET', function_endpoint, **kwargs)

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

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_log_sources_log_source_groups(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/log_sources/log_source_groups
        Retrieves a list of log source groups.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/log_source_groups')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

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

    @header_vars('fields')
    def put_network_hierarchy_staged_networks(self, *, network_hierarchy, fields=None, **kwargs):
        """
        PUT /config/network_hierarchy/staged_networks
        Replaces the current network hierarchy with the input that is provided.
        """
        function_endpoint = urljoin(self._baseurl, 'network_hierarchy/staged_networks')
        return self._call('PUT', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_network_hierarchy_staged_networks(self, *, fields=None, **kwargs):
        """
        GET /config/network_hierarchy/staged_networks
        Retrieves the staged network hierarchy.
        """
        function_endpoint = urljoin(self._baseurl, 'network_hierarchy/staged_networks')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_remote_networks(self, *, Range=None, fields=None, filter=None, **kwargs):
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
    @request_vars('fields', 'filter')
    def get_remote_services(self, *, Range=None, fields=None, filter=None, **kwargs):
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
    @request_vars('fields', 'filter')
    def get_resource_restriction_users_by_tenant_by_tenant_id(self, tenant_id, *, Range=None, fields=None, filter=None,
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

    @header_vars('fields')
    def post_resource_restrictions(self, *, resourceRestriction, fields=None, **kwargs):
        """
        POST /config/resource_restrictions
        Creates a new resource restriction.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions')
        return self._call('POST', function_endpoint, json=resourceRestriction, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_resource_restrictions(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/resource_restrictions
        Retrieves a list of all resource restrictions.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions')
        return self._call('GET', function_endpoint, **kwargs)

    def delete_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, **kwargs):
        """
        DELETE /config/resource_restrictions/{resource_restriction_id}
        Deletes a resource restriction consumer by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions/{resource_restriction_id}'.format(
            resource_restriction_id=resource_restriction_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

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

    @request_vars('fields')
    def get_resource_restrictions_by_resource_restriction_id(self, resource_restriction_id, *, fields=None, **kwargs):
        """
        GET /config/resource_restrictions/{resource_restriction_id}
        Retrieves a resource restriction consumer by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'resource_restrictions/{resource_restriction_id}'.format(
            resource_restriction_id=resource_restriction_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_selective_forwarding_destinations(self, *, Range=None, fields=None, filter=None, **kwargs):
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

    def delete_selective_forwarding_destinations_by_id(self, id, **kwargs):
        """
        DELETE /config/selective_forwarding/destinations/{id}
        delete a Selective Forwarding Destination
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/destinations/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    def post_selective_forwarding_destinations_by_id(self, id, *, data, **kwargs):
        """
        POST /config/selective_forwarding/destinations/{id}
        delete a Selective Forwarding Destination
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/destinations/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    def post_selective_forwarding_routes(self, *, data, **kwargs):
        """
        POST /config/selective_forwarding/routes
        Creates a new Routing Rule with the fields supplied in the body parameter
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes')
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_selective_forwarding_routes(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /config/selective_forwarding/routes
        Returns all Routing Rules in the system, ordered by creation date
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes')
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

    def delete_selective_forwarding_routes_by_id(self, id, **kwargs):
        """
        DELETE /config/selective_forwarding/routes/{id}
        Deletes a Routing Rule with the the given ID
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'selective_forwarding/routes/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_store_and_forward_policies(self, *, Range=None, fields=None, filter=None, **kwargs):
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

    def delete_store_and_forward_policies_by_id(self, id, **kwargs):
        """
        DELETE /config/store_and_forward/policies/{id}
        Deletes a store and forward policy.
        """
        function_endpoint = urljoin(self._baseurl, 'store_and_forward/policies/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def post_store_and_forward_policies_by_id(self, id, *, policy, fields=None, **kwargs):
        """
        POST /config/store_and_forward/policies/{id}
        Updates the store and forward policy owner only.
        """
        function_endpoint = urljoin(self._baseurl, 'store_and_forward/policies/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=policy, **kwargs)

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
    @request_vars('fields', 'filter')
    def get_vpn_client_configurations(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /config/vpn/client_configurations
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'vpn/client_configurations')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
