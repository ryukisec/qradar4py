from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Help(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /help and its endpoints.
    """
    __baseurl = 'help/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('full_content', 'fields')
    def get_capabilities(self, *, full_content=None, Range=None, fields=None, **kwargs):
        """
        GET /help/capabilities
        List all QRadar API capabilities.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'capabilities')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('full_content', 'fields')
    def get_capabilities_by_version(self, version, *, full_content=None, fields=None, **kwargs):
        """
        GET /help/capabilities/{version}
        List capabilities of this API server by providing a map of all endpoints for the given version, keyed on their
        category. Endpoints which your user account do not have access to use will not be displayed.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'capabilities/{version}'.format(version=version))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('full_content', 'fields')
    def get_capabilities_version_by_path(self, version, path, *, full_content=None, fields=None, **kwargs):
        """
        GET /help/capabilities/{version}/{path}
        List capabilities of this API server by providing a map of all endpoints for the given version, category, and
        path, keyed on their request type. Endpoints which your user account do not have access to use will not be
        displayed.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'capabilities/{version}/{path}'.format(version=version, path=path))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('full_content', 'fields')
    def get_capabilities_version_path_by_request_type(self, version, path, request_type, *, full_content=None,
                                                      fields=None, **kwargs):
        """
        GET /help/capabilities/{version}/{path}/{request_type}
        Provide the endpoint supported by this API server mapped to the given version, category, path, and request type.
        If you do not have access to the endpoint, nothing will be displayed.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl,
                                    'capabilities/{version}/{path}/{request_type}'.format(version=version, path=path,
                                                                                          request_type=request_type))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_endpoints(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /help/endpoints
        Retrieves a list of endpoint documentation objects that are currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'endpoints')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_endpoints_by_endpoint_id(self, endpoint_id, *, fields=None, **kwargs):
        """
        GET /help/endpoints/{endpoint_id}
        Retrieves a single endpoint documentation object.
        """
        function_endpoint = urljoin(self._baseurl, 'endpoints/{endpoint_id}'.format(endpoint_id=endpoint_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_resources(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /help/resources
        Retrieves a list of resource documentation objects currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'resources')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_resources_by_resource_id(self, resource_id, *, fields=None, **kwargs):
        """
        GET /help/resources/{resource_id}
        Retrieves a single resource documentation object.
        """
        function_endpoint = urljoin(self._baseurl, 'resources/{resource_id}'.format(resource_id=resource_id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_versions(self, *, Range=None, fields=None, filter=None, **kwargs):
        """
        GET /help/versions
        Retrieves a list of version documentation objects currently in the system.
        """
        function_endpoint = urljoin(self._baseurl, 'versions')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_versions_by_version_id(self, version_id, *, fields=None, **kwargs):
        """
        GET /help/versions/{version_id}
        Retrieves a single version documentation object.
        """
        function_endpoint = urljoin(self._baseurl, 'versions/{version_id}'.format(version_id=version_id))
        return self._call('GET', function_endpoint, **kwargs)
