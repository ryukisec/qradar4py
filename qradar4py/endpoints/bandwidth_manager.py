from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class BandwidthManager(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /bandwidth_manager and its endpoints.
    """
    __baseurl = 'bandwidth_manager/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_configurations(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /bandwidth_manager/configurations
        Retrieves a list of configurations.
        """
        function_endpoint = urljoin(self._baseurl, 'configurations')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_configurations(self, *, configuration, fields=None, **kwargs):
        """
        POST /bandwidth_manager/configurations
        Creates a bandwidth manager configuration
        """
        function_endpoint = urljoin(self._baseurl, 'configurations')
        return self._call('POST', function_endpoint, json=configuration, **kwargs)

    @header_vars('fields')
    def post_configurations_by_id(self, id, *, configuration, fields=None, **kwargs):
        """
        POST /bandwidth_manager/configurations/{id}
        Update a bandwidth manager configuration by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'configurations/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=configuration, **kwargs)

    @request_vars('fields')
    def get_configurations_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /bandwidth_manager/configurations/{id}
        Retrieves a configuration.
        """
        function_endpoint = urljoin(self._baseurl, 'configurations/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    def delete_configurations_by_id(self, id, **kwargs):
        """
        DELETE /bandwidth_manager/configurations/{id}
        Delete a bandwidth manager configuration by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'configurations/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter', 'sort')
    def get_filters(self, *, fields=None, filter=None, sort=None, Range=None, **kwargs):
        """
        GET /bandwidth_manager/filters
        Retrieves a list of egress filters.
        """
        function_endpoint = urljoin(self._baseurl, 'filters')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_filters(self, *, class_, fields=None, **kwargs):
        """
        POST /bandwidth_manager/filters
        Creates a bandwidth manager filter
        """
        function_endpoint = urljoin(self._baseurl, 'filters')
        return self._call('POST', function_endpoint, json=class_, **kwargs)

    @request_vars('fields')
    def get_filters_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /bandwidth_manager/filters/{id}
        Retrieves a filter.
        """
        function_endpoint = urljoin(self._baseurl, 'filters/{id}'.format(id=id))
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('fields')
    def post_filters_by_id(self, id, *, filter, fields=None, **kwargs):
        """
        POST /bandwidth_manager/filters/{id}
        Delete a filter by sequence ID.
        """
        function_endpoint = urljoin(self._baseurl, 'filters/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=filter, **kwargs)

    def delete_filters_by_id(self, id, **kwargs):
        """
        DELETE /bandwidth_manager/filters/{id}
        Update a filter by ID.
        """
        function_endpoint = urljoin(self._baseurl, 'filters/{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', **kwargs)
