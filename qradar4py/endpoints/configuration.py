from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Configuration(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /configuration and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'configuration/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_log_source_groups(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /configuration/log_source_groups
        Retrieve a list of all log source groups
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_source_groups')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_source_groups_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /configuration/log_source_groups/{id}
        Retrieve a specific log source group
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_source_groups/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_log_source_protocols(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /configuration/log_source_protocols
        Retrieves all log source Protocol
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_source_protocols')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_log_source_types(self, *, data, fields=None, **kwargs):
        """
        POST /configuration/log_source_types
        Generates a new custom log-source-type. These can be used for making custom parsing configurations
        that utilize log-source-extensions and custom-properties. The log-source-type that results from
        this creation is essentially a blank slate. It will contain no default parsing logic, all
        parsing intelligence must be supplied via log-source-extensions or custom event properties.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_source_types')
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('excludeSystemTypes', 'filter', 'fields', 'sort')
    def get_log_source_types(self, *, excludeSystemTypes=None, filter=None, fields=None, Range=None, sort=None,
                             **kwargs):
        """
        GET /configuration/log_source_types
        Retrieve a list of all log source types
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_source_types')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_source_types_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /configuration/log_source_types/{id}
        Retrieve a single log source type using ID
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_source_types/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_log_source_types_by_id(self, id, *, data=None, fields=None, **kwargs):
        """
        POST /configuration/log_source_types/{id}
        Updates a log source type by id. Supply the JSON object containing the fields
        to update.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_source_types/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('show_deleted', 'filter', 'fields')
    def get_log_sources(self, *, show_deleted=None, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /configuration/log_sources
        Retrieve a set of all log sources
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_log_sources_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /configuration/log_sources/{id}
        Return the log source identified by id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_log_sources_by_id(self, id, *, data=None, fields=None, **kwargs):
        """
        POST /configuration/log_sources/{id}
        Update the properties of the log source using id.
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @request_vars('host_name', 'token', 'name', 'arielAPIVersion', 'fields')
    def post_log_sources_health(self, *, host_name, token, name, arielAPIVersion=None, fields=None, **kwargs):
        """
        POST /configuration/log_sources_health
        Create a Health Log Source to pull in health data
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'log_sources_health')
        return self._call('POST', function_endpoint, headers=headers, **kwargs)
