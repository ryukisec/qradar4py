from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class DynamicSearch(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /dynamic_search and its endpoints.
    """
    __baseurl = 'dynamic_search/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas
        Gets the list of all schemas available to the user.
        """
        function_endpoint = urljoin(self._baseurl, 'schemas')
        return self._call('GET', function_endpoint, **kwargs)

    @request_vars('fields')
    def get_schemas_by_name(self, name, *, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}
        Gets the list of all schemas available to the user.
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas_fields_by_name(self, name, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}/fields
        Gets the list of all available Fields
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}/fields'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas_functions_by_name(self, name, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}/functions
        Gets the list of all available Functions
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}/functions'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_schemas_operators_by_name(self, name, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /dynamic_search/schemas/{name}/operators
        Gets the list of all available relational Operators
        """
        function_endpoint = urljoin(self._baseurl, 'schemas/{name}/operators'.format(name=name))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_searches(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /dynamic_search/searches
        Gets the list of all searches performed by this user.
        """
        function_endpoint = urljoin(self._baseurl, 'searches')
        return self._call('GET', function_endpoint, **kwargs)

    def post_searches(self, *, search, **kwargs):
        """
        POST /dynamic_search/searches
        Posts a search to be performed by the service.
        """
        function_endpoint = urljoin(self._baseurl, 'searches')
        return self._call('POST', function_endpoint, json=search, **kwargs)

    def delete_searches_by_handle(self, handle, **kwargs):
        """
        DELETE /dynamic_search/searches/{handle}
        Deletes a search and any stored results.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{handle}'.format(handle=handle))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @request_vars('fields')
    def get_searches_by_handle(self, handle, *, fields=None, **kwargs):
        """
        GET /dynamic_search/searches/{handle}
        Gets the specific search performed by this user.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{handle}'.format(handle=handle))
        return self._call('GET', function_endpoint, **kwargs)

    def get_searches_results_by_handle(self, handle, **kwargs):
        """
        GET /dynamic_search/searches/{handle}/results
        Gets the specific search performed by this user.
        """
        function_endpoint = urljoin(self._baseurl, 'searches/{handle}/results'.format(handle=handle))
        return self._call('GET', function_endpoint, **kwargs)
