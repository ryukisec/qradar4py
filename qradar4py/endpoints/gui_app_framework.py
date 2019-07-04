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

    def post_application_creation_task(self, *, package, **kwargs):
        """
        POST /gui_app_framework/application_creation_task
        Installs a new application.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task')
        return self._call('POST', function_endpoint, mime_type={'Content-Type': 'application/zip'}, data=package,
                          **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_application_creation_task(self, *, fields=None, Range=None, filter=None, **kwargs):
        """
        GET /gui_app_framework/application_creation_task
        Retrieves the status of all application installs.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task')
        return self._call('GET', function_endpoint, **kwargs)

    def get_application_creation_task_by_application_id(self, application_id, **kwargs):
        """
        GET /gui_app_framework/application_creation_task/{application_id}
        Retrieves the status of an application install.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'application_creation_task/{application_id}'.format(application_id=application_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('status')
    def post_application_creation_task_by_application_id(self, application_id, *, status, **kwargs):
        """
        POST /gui_app_framework/application_creation_task/{application_id}
        Cancels an application install.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'application_creation_task/{application_id}'.format(application_id=application_id))
        return self._call('POST', function_endpoint, **kwargs)

    def post_application_creation_task_auth_by_application_id(self, application_id, *, authorisation, **kwargs):
        """
        POST /gui_app_framework/application_creation_task/{application_id}/auth
        Responds to an authorisation request for an application install.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task/{application_id}/auth'.format(
            application_id=application_id))
        return self._call('POST', function_endpoint, json=authorisation, **kwargs)

    def get_application_creation_task_auth_by_application_id(self, application_id, **kwargs):
        """
        GET /gui_app_framework/application_creation_task/{application_id}/auth
        Retrieves an authorisation request for an application install.
        """
        function_endpoint = urljoin(self._baseurl, 'application_creation_task/{application_id}/auth'.format(
            application_id=application_id))
        return self._call('GET', function_endpoint, **kwargs)

    def get_applications(self, **kwargs):
        """
        GET /gui_app_framework/applications
        Retrieve list of applications.
        """
        function_endpoint = urljoin(self._baseurl, 'applications')
        return self._call('GET', function_endpoint, **kwargs)

    def put_applications_by_application_id(self, application_id, *, package, **kwargs):
        """
        PUT /gui_app_framework/applications/{application_id}
        Upgrades an application.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('PUT', function_endpoint, **kwargs)

    def get_applications_by_application_id(self, application_id, **kwargs):
        """
        GET /gui_app_framework/applications/{application_id}
        Retrieve an installed application.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('status', 'oauth_user_id')
    def post_applications_by_application_id(self, application_id, *, status=None, oauth_user_id=None, **kwargs):
        """
        POST /gui_app_framework/applications/{application_id}
        Updates an application.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('POST', function_endpoint, **kwargs)

    def delete_applications_by_application_id(self, application_id, **kwargs):
        """
        DELETE /gui_app_framework/applications/{application_id}
        Deletes an application.
        """
        function_endpoint = urljoin(self._baseurl,
                                    'applications/{application_id}'.format(application_id=application_id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

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
