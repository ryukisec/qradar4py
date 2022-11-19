from urllib.parse import urljoin

from qradar4py.endpoints.api_endpoint import QRadarAPIEndpoint
from qradar4py.endpoints.api_endpoint import request_vars
from qradar4py.endpoints.api_endpoint import header_vars


class Usermanagement(QRadarAPIEndpoint):
    """
    The QRadar API endpoint group /usermanagement and its endpoints.
    UNDOCUMENTED
    """
    __baseurl = 'usermanagement/'

    def __init__(self, url, header, verify):
        super().__init__(urljoin(url, self.__baseurl),
                         header,
                         verify)

    @header_vars('Range')
    @request_vars('fields', 'filter')
    def get_users(self, *, fields=None, filter=None, Range=None, **kwargs):
        """
        GET /usermanagement/users
        Retrieve a list of all QRadar users.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'users')
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    @request_vars('fields')
    def get_users_by_username(self, username, *, fields=None, **kwargs):
        """
        GET /usermanagement/users/{username}
        Retrieve a specific user by username
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'users/{username}'.format(username=username))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)

    def get_users_username_access_cidr_by_cidr(self, username, cidr, **kwargs):
        """
        GET /usermanagement/users/{username}/access/cidr/{cidr}
        Check if a user has access to an IP or CIDR.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl,
                                    'users/{username}/access/cidr/{cidr}'.format(username=username, cidr=cidr))
        return self._call('GET', function_endpoint, response_type='text/plain', headers=headers, **kwargs)

    @header_vars('Range')
    @request_vars('filter')
    def get_users_access_cidrs_by_username(self, username, *, filter=None, Range=None, **kwargs):
        """
        GET /usermanagement/users/{username}/access/cidrs
        Retrieve the list of CIDRs a user has access to.
        UNDOCUMENTED
        """
        headers = kwargs.pop('headers', {})
        headers.update({'Allow-Hidden': 'True'})
        function_endpoint = urljoin(self._baseurl, 'users/{username}/access/cidrs'.format(username=username))
        return self._call('GET', function_endpoint, headers=headers, **kwargs)
