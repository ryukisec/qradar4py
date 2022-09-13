from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class GuiAppFramework(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /gui_app_framework and its endpoints.
    """
    __baseurl = 'gui_app_framework/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('user_id', 'security_profile_id')
    def delete_admin_override(self, *, user_id, security_profile_id, **kwargs):
        """
        DELETE /gui_app_framework/admin_override
        Deletes an augmented security profile from an user
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'admin_override')
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('user_id', 'security_profile_id')
    def post_admin_override(self, *, user_id, security_profile_id, **kwargs):
        """
        POST /gui_app_framework/admin_override
        Add an augment security profile to an applicable user

        Supported types of user are: admin or SAAS admin
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'admin_override')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    def get_admin_override(self, **kwargs):
        """
        GET /gui_app_framework/admin_override
        Retrieve list of augmented security profiles.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'admin_override')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_application_creation_task(self, *, package, fields=None, **kwargs):
        """
        POST /gui_app_framework/application_creation_task
        Installs a new application.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'application/zip'}, data=package,
                          **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_application_creation_task(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /gui_app_framework/application_creation_task
        Retrieves the status of all application installs.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('status', 'fields')
    def post_application_creation_task_by_application_id(self, application_id, *, status, fields=None, **kwargs):
        """
        POST /gui_app_framework/application_creation_task/{application_id}
        Cancels an application install.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'application_creation_task/{application_id}'.format(application_id=application_id))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_application_creation_task_by_application_id(self, application_id, *, fields=None, **kwargs):
        """
        GET /gui_app_framework/application_creation_task/{application_id}
        Retrieves the status of an application install.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'application_creation_task/{application_id}'.format(application_id=application_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_application_creation_task_auth_by_application_id(self, application_id, *, authorisation, fields=None,
                                                              **kwargs):
        """
        POST /gui_app_framework/application_creation_task/{application_id}/auth
        Responds to an authorisation request for an application install.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task/{application_id}/auth'.format(
            application_id=application_id))
        return self._call('POST', function_endpoint, json=authorisation, **kwargs)

    @request_vars('fields')
    def get_application_creation_task_auth_by_application_id(self, application_id, *, fields=None, **kwargs):
        """
        GET /gui_app_framework/application_creation_task/{application_id}/auth
        Retrieves an authorisation request for an application install.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task/{application_id}/auth'.format(
            application_id=application_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_application_definitions(self, *, package, fields=None, **kwargs):
        """
        POST /gui_app_framework/application_definitions
        Installs a new application.
        """
        function_endpoint = urljoin(self._baseurl, 'application_definitions')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'application/zip'}, data=package,
                          **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_application_definitions(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /gui_app_framework/application_definitions
        Retrieve list of application definitions.
        """
        function_endpoint = urljoin(self._baseurl, 'application_definitions')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('include_stopped_application', 'fields')
    def put_application_definitions_by_application_definition_id(self, application_definition_id, *, package,
                                                                 include_stopped_application=None, fields=None,
                                                                 **kwargs):
        """
        PUT /gui_app_framework/application_definitions/{application_definition_id}
        Upgrades an application definition.
        """
        function_endpoint = urljoin(self._baseurl, 'application_definitions/{application_definition_id}'.format(
            application_definition_id=application_definition_id))
        return self._call('PUT', function_endpoint, **kwargs)

    def delete_application_definitions_by_application_definition_id(self, application_definition_id, **kwargs):
        """
        DELETE /gui_app_framework/application_definitions/{application_definition_id}
        Deletes an application definition and its associated instances.
        """
        function_endpoint = urljoin(self._baseurl, 'application_definitions/{application_definition_id}'.format(
            application_definition_id=application_definition_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('status', 'fields')
    def post_application_definitions_by_application_definition_id(self, application_definition_id, *, status=None,
                                                                  fields=None, **kwargs):
        """
        POST /gui_app_framework/application_definitions/{application_definition_id}
        Cancels the creation or upgrade of an application definition
        """
        function_endpoint = urljoin(self._baseurl, 'application_definitions/{application_definition_id}'.format(
            application_definition_id=application_definition_id))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_application_definitions_by_application_definition_id(self, application_definition_id, *, fields=None,
                                                                 **kwargs):
        """
        GET /gui_app_framework/application_definitions/{application_definition_id}
        Retrieve an application definition.
        """
        function_endpoint = urljoin(self._baseurl, 'application_definitions/{application_definition_id}'.format(
            application_definition_id=application_definition_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_application_definitions_tenants_by_application_definition_id(self, application_definition_id, *, tenant_id,
                                                                          fields=None, **kwargs):
        """
        POST /gui_app_framework/application_definitions/{application_definition_id}/tenants
        Associates a tenant with an application definition
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'application_definitions/{application_definition_id}/tenants'.format(
            application_definition_id=application_definition_id))
        return self._call('POST', function_endpoint, json=tenant_id, headers=headers, **kwargs)

    @request_vars('fields')
    def delete_application_definitions_application_definition_id_tenants_by_tenant_id(self, application_definition_id,
                                                                                      tenant_id, *, fields=None,
                                                                                      **kwargs):
        """
        DELETE /gui_app_framework/application_definitions/{application_definition_id}/tenants/{tenant_id}
        Removes the association between a tenant and an application definition
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'application_definitions/{application_definition_id}/tenants/{tenant_id}'.format(
                                        application_definition_id=application_definition_id, tenant_id=tenant_id))
        return self._call('DELETE', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_application_definitions_user_role_id_by_application_definition_id(self, application_definition_id, *,
                                                                              fields=None, **kwargs):
        """
        GET /gui_app_framework/application_definitions/{application_definition_id}/user_role_id
        Retrieve all user roles associated with an application definition.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'application_definitions/{application_definition_id}/user_role_id'.format(
                                        application_definition_id=application_definition_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def delete_application_definitions_application_definition_id_user_role_id_by_user_role_id(self,
                                                                                              application_definition_id,
                                                                                              user_role_id, *,
                                                                                              fields=None, **kwargs):
        """
        DELETE /gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}
        No summary provided
        """
        function_endpoint = urljoin(self._baseurl,
                                    'application_definitions/{application_definition_id}/user_role_id/{user_role_id}'.format(
                                        application_definition_id=application_definition_id, user_role_id=user_role_id))
        return self._call('DELETE', function_endpoint, **kwargs)

    @request_vars('fields')
    def post_application_definitions_application_definition_id_user_role_id_by_user_role_id(self,
                                                                                            application_definition_id,
                                                                                            user_role_id, *,
                                                                                            fields=None, **kwargs):
        """
        POST /gui_app_framework/application_definitions/{application_definition_id}/user_role_id/{user_role_id}
        Add a user role to the list associated with an application definition
        """
        function_endpoint = urljoin(self._baseurl,
                                    'application_definitions/{application_definition_id}/user_role_id/{user_role_id}'.format(
                                        application_definition_id=application_definition_id, user_role_id=user_role_id))
        return self._call('POST', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_applications(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /gui_app_framework/applications
        Retrieve list of applications.
        """
        function_endpoint = urljoin(self._baseurl, 'applications')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('application_definition_id', 'security_profile_id', 'force_multitenancy_safe', 'fields')
    def post_applications(self, *, application_definition_id, security_profile_id=None, force_multitenancy_safe=None,
                          fields=None, **kwargs):
        """
        POST /gui_app_framework/applications
        Creates a new application instance.
        """
        function_endpoint = urljoin(self._baseurl, 'applications')
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('status', 'oauth_user_id', 'security_profile_id', 'fields')
    def post_applications_by_application_id(self, application_id, *, status=None, oauth_user_id=None,
                                            security_profile_id=None, fields=None, **kwargs):
        """
        POST /gui_app_framework/applications/{application_id}
        Updates an application.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('POST', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_applications_by_application_id(self, application_id, *, fields=None, **kwargs):
        """
        GET /gui_app_framework/applications/{application_id}
        Retrieve an installed application.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_applications_by_application_id(self, application_id, **kwargs):
        """
        DELETE /gui_app_framework/applications/{application_id}
        Deletes an application instance.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('fields')
    def put_applications_by_application_id(self, application_id, *, package, fields=None, **kwargs):
        """
        PUT /gui_app_framework/applications/{application_id}
        Upgrades an application.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('PUT', function_endpoint, **kwargs)

    def get_migration_sourcehost(self, **kwargs):
        """
        GET /gui_app_framework/migration/sourcehost
        Retrieves the current application source host
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'migration/sourcehost')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def get_migration_status(self, **kwargs):
        """
        GET /gui_app_framework/migration/status
        Retrieves the current migration status
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'migration/status')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def get_migration_check_by_type(self, type, **kwargs):
        """
        GET /gui_app_framework/migration/{type}/check
        Invokes a 'dry run' of a migration and returns any issues found.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'migration/{type}/check'.format(type=type))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def post_migration_start_by_type(self, type, **kwargs):
        """
        POST /gui_app_framework/migration/{type}/start
        Invokes the data migration based on the type specified.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'migration/{type}/start'.format(type=type))
        return self._call('POST', function_endpoint, headers=headers, **kwargs)

    def get_named_services(self, **kwargs):
        """
        GET /gui_app_framework/named_services
        Retrieves all named services.
        """
        function_endpoint = urljoin(self._baseurl, 'named_services')
        return self._call('GET', function_endpoint, **kwargs)

    def get_named_services_by_uuid(self, uuid, **kwargs):
        """
        GET /gui_app_framework/named_services/{uuid}
        Retrieves a named service.
        """
        function_endpoint = urljoin(self._baseurl, 'named_services/{uuid}'.format(uuid=uuid))
        return self._call('GET', function_endpoint, **kwargs)

    def get_resources(self, **kwargs):
        """
        GET /gui_app_framework/resources
        Returns workload resources
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'resources')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def get_resources_by_serviceName(self, serviceName, **kwargs):
        """
        GET /gui_app_framework/resources/{serviceName}
        Returns service resources
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'resources/{serviceName}'.format(serviceName=serviceName))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_runtime_status(self, *, fields=None, **kwargs):
        """
        GET /gui_app_framework/runtime/status
        Retrieves the status of cloud enablement.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'runtime/status')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_runtime_enable_by_type(self, type, *, hostTypeParams, fields=None, **kwargs):
        """
        POST /gui_app_framework/runtime/{type}/enable
        Responds to a request to enable cloud mode.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'runtime/{type}/enable'.format(type=type))
        return self._call('POST', function_endpoint, json=hostTypeParams, headers=headers, **kwargs)

    @request_vars('fields')
    def get_runtime_exclusions_by_type(self, type, *, fields=None, **kwargs):
        """
        GET /gui_app_framework/runtime/{type}/exclusions
        Returns a collection of exclusions for the provided runtime
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'runtime/{type}/exclusions'.format(type=type))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_runtime_exclusions_by_type(self, type, *, exclusion, fields=None, **kwargs):
        """
        POST /gui_app_framework/runtime/{type}/exclusions
        Adds an exclusion to the provided runtime
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'runtime/{type}/exclusions'.format(type=type))
        return self._call('POST', function_endpoint, json=exclusion, headers=headers, **kwargs)

    def delete_runtime_type_exclusions_by_uuid(self, type, uuid, **kwargs):
        """
        DELETE /gui_app_framework/runtime/{type}/exclusions/{uuid}
        Removes an exclusion from a runtime based upon its applications UUID
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'runtime/{type}/exclusions/{uuid}'.format(type=type, uuid=uuid))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @request_vars('fields')
    def get_runtime_type_exclusions_by_uuid(self, type, uuid, *, fields=None, **kwargs):
        """
        GET /gui_app_framework/runtime/{type}/exclusions/{uuid}
        Retrieves a specific exclusion based upon the supplied runtime and uuid
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'runtime/{type}/exclusions/{uuid}'.format(type=type, uuid=uuid))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter')
    def get_runtime_metrics_by_type(self, type, *, Range=None, filter=None, **kwargs):
        """
        GET /gui_app_framework/runtime/{type}/metrics
        Retrieves the metrics of apps in the cloud.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'runtime/{type}/metrics'.format(type=type))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def get_user_applications(self, **kwargs):
        """
        GET /gui_app_framework/user/applications
        Retrieve list of user specific applications.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'user/applications')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
