from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint


class Auth(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /auth and its endpoints.
    """
    __baseurl = 'auth/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    def post_logout(self, **kwargs):
        """
        POST /auth/logout
        Invoke this method as an authorized user and your session will be invalidated.
        """
        function_endpoint = urljoin(self._baseurl, 'logout')
        return self._call('POST', function_endpoint, response_type='text/plain', **kwargs)
