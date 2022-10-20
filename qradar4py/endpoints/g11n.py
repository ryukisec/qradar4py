from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class G11n(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /g11n and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'g11n/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('filter', 'fields')
    def get_locale(self, *, filter=None, fields=None, Range=None, **kwargs):
        """
        GET /g11n/locale
        No summary provided
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': True})
        function_endpoint = urljoin(self._baseurl, 'locale')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
