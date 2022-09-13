from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class HealthData(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /health_data and its endpoints.
    """
    __baseurl = 'health_data/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @request_vars('fields')
    def get_security_data_count(self, *, fields=None, **kwargs):
        """
        GET /health_data/security_data_count
        Retrieves count of security artifacts in QRadar
        """
        function_endpoint = urljoin(self._baseurl, 'security_data_count')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_top_offenses(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /health_data/top_offenses
        Retrieves Top Offenses in the system sorted by update count.
        """
        function_endpoint = urljoin(self._baseurl, 'top_offenses')
        return self._call('GET', function_endpoint, **kwargs)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_top_rules(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /health_data/top_rules
        Retrieves Top Rules in the system sorted by response count.
        """
        function_endpoint = urljoin(self._baseurl, 'top_rules')
        return self._call('GET', function_endpoint, **kwargs)
