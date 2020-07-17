from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Reports(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /reports and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'reports/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_groups(self, *, Range=None, filter=None, fields=None, **kwargs):
        """
        GET /reports/groups
        Retrieve a list of securities associated to the shared groups available in the system
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'groups')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @header_vars('fields')
    def post_groups_by_id(self, id, *, data, fields=None, **kwargs):
        """
        POST /reports/groups/{id}
        Update the security structure associated to a shared group
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'groups/{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=data, headers=headers, **kwargs)

    @request_vars('fields')
    def get_groups_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /reports/groups/{id}
        Retrieve a security structure associated to a shared group
        UNDOCUMENTED
        """
        headers = kwargs.get('headers', {}).update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'groups/{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
