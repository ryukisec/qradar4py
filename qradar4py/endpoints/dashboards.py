from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Dashboards(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /siem and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'dashboards/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /dashboards
        Retrieves a list of dashboards.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, '')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def delete_by_id(self, id, **kwargs):
        """
        DELETE /dashboards/{id}
        Deletes a dashboard.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, '{id}'.format(id=id))
        return self._call('DELETE', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('fields')
    def post_by_id(self, id, *, dashboard, fields=None, **kwargs):
        """
        POST /dashboards/{id}
        Updates the dashboard owner only.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, '{id}'.format(id=id))
        return self._call('POST', function_endpoint, json=dashboard, headers=headers, **kwargs)

    @request_vars('fields')
    def get_by_id(self, id, *, fields=None, **kwargs):
        """
        GET /dashboards/{id}
        Retrieves a dashboard.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, '{id}'.format(id=id))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
