from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Access(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /access and its endpoints.
    """
    __baseurl = 'analytics/'

    def __init__(self, url, session):
        super().__init__(urljoin(url, self.__baseurl),
                         session)

    @header_vars('Range')
    @request_vars('filter', 'sort', 'fields')
    def get_login_attempts(self, *, Range=None, filter=None, sort=None, fields=None, **kwargs):
        """
        GET /access/login_attempts
        Gets the list of login attempts.
        """
        function_endpoint = urljoin(self._baseurl, 'login_attempts')
        return self._call('GET', function_endpoint, **kwargs)
